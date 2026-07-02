from django.contrib import admin
from django.db import IntegrityError
from django.test import SimpleTestCase, TestCase
from django.urls import reverse

from contact.models import ContactSubmission
from core.models import NavigationItem, SiteSetting
from pages.models import HeroSlide, TeamMember
from services.models import Service, ServiceCategory, ServiceStat
from subsidiaries.models import Subsidiary


class Phase5AModelTests(TestCase):
  """Phase 5A: verify dynamic content models and constraints."""

  def test_site_setting_singleton_can_be_created(self):
    setting = SiteSetting.load()
    setting.site_name = "AFRILOTT Holding Ltd"
    setting.save()
    self.assertEqual(SiteSetting.objects.count(), 1)
    self.assertEqual(str(setting), "AFRILOTT Holding Ltd")

  def test_navigation_item_can_be_created_with_parent(self):
    parent = NavigationItem.objects.create(title="Services", order=1)
    child = NavigationItem.objects.create(
      title="Digital Solutions",
      parent=parent,
      url_name="services:category_detail",
      order=1,
    )
    self.assertIn(child, parent.children.all())
    self.assertEqual(str(child), "Services → Digital Solutions")

  def test_service_category_slug_is_unique(self):
    ServiceCategory.objects.create(name="Procurement", slug="procurement-supply-chain")
    with self.assertRaises(IntegrityError):
      ServiceCategory.objects.create(name="Duplicate", slug="procurement-supply-chain")

  def test_service_unique_constraint_per_category(self):
    category = ServiceCategory.objects.create(
      name="Procurement",
      slug="procurement-supply-chain",
    )
    Service.objects.create(
      category=category,
      name="Woodworking",
      slug="woodworking-equipment-tools",
    )
    with self.assertRaises(IntegrityError):
      Service.objects.create(
        category=category,
        name="Duplicate Woodworking",
        slug="woodworking-equipment-tools",
      )

  def test_service_slug_can_repeat_across_categories(self):
    cat_a = ServiceCategory.objects.create(name="Category A", slug="category-a")
    cat_b = ServiceCategory.objects.create(name="Category B", slug="category-b")
    Service.objects.create(category=cat_a, name="Shared Slug A", slug="shared-slug")
    service_b = Service.objects.create(
      category=cat_b,
      name="Shared Slug B",
      slug="shared-slug",
    )
    self.assertEqual(service_b.slug, "shared-slug")

  def test_service_get_absolute_url(self):
    category = ServiceCategory.objects.create(
      name="Digital Solutions",
      slug="digital-solutions",
    )
    service = Service.objects.create(
      category=category,
      name="AI & Data Science",
      slug="ai-data-science",
    )
    self.assertEqual(
      service.get_absolute_url(),
      reverse(
        "services:service_detail",
        kwargs={
          "category_slug": "digital-solutions",
          "service_slug": "ai-data-science",
        },
      ),
    )

  def test_service_stat_related_name(self):
    category = ServiceCategory.objects.create(name="GTL", slug="general-trading-logistics")
    service = Service.objects.create(
      category=category,
      name="Petroleum Logistics",
      slug="petroleum-logistics",
    )
    stat = ServiceStat.objects.create(
      service=service,
      label="Fleet Units",
      value="50+",
      order=1,
    )
    self.assertEqual(list(service.stats.all()), [stat])

  def test_subsidiary_get_absolute_url(self):
    subsidiary = Subsidiary.objects.create(
      name="Afrilott Overseas LLC",
      slug="afrilott-overseas",
    )
    self.assertEqual(
      subsidiary.get_absolute_url(),
      reverse("subsidiaries:detail", kwargs={"slug": "afrilott-overseas"}),
    )

  def test_contact_submission_default_status_is_new(self):
    submission = ContactSubmission.objects.create(
      full_name="Jane Doe",
      email="jane@example.com",
      message="Hello",
    )
    self.assertEqual(submission.status, ContactSubmission.Status.NEW)
    self.assertFalse(submission.is_read)

  def test_hero_slide_and_team_member_can_be_created(self):
    slide = HeroSlide.objects.create(title="Welcome", order=1)
    member = TeamMember.objects.create(name="John Smith", role="CEO", order=1)
    self.assertEqual(str(slide), "Welcome")
    self.assertEqual(str(member), "John Smith")


class Phase5AAdminRegistrationTests(SimpleTestCase):
  """Verify all Phase 5A models are registered in Django admin."""

  MODELS = (
    SiteSetting,
    NavigationItem,
    HeroSlide,
    TeamMember,
    ServiceCategory,
    Service,
    ServiceStat,
    Subsidiary,
    ContactSubmission,
  )

  def test_all_models_registered_in_admin(self):
    for model in self.MODELS:
      with self.subTest(model=model.__name__):
        self.assertTrue(admin.site.is_registered(model))


class Phase5APublicRoutesUnchangedTests(TestCase):
  """Public pages must still return 200 after Phase 5A model work."""

  ROUTES = [
    "/",
    "/about/",
    "/services/",
    "/services/procurement-supply-chain/",
    "/services/digital-solutions/ai-data-science/",
    "/subsidiaries/",
    "/subsidiaries/afrilott-overseas/",
    "/contact/",
  ]

  def test_public_routes_still_return_200(self):
    for url in self.ROUTES:
      with self.subTest(url=url):
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
