from django.core.management import call_command
from django.test import TestCase

from contact.models import ContactSubmission
from core.models import NavigationItem, SiteSetting
from pages.models import HeroSlide, TeamMember
from services.models import Service, ServiceCategory, ServiceStat
from subsidiaries.models import Subsidiary


class SeedSiteContentCommandTests(TestCase):
    """Phase 5B: verify seed_site_content management command."""

    def run_seed(self, **kwargs):
        call_command("seed_site_content", **kwargs)

    def test_command_runs_successfully(self):
        self.run_seed()
        self.assertEqual(ServiceCategory.objects.count(), 3)
        self.assertEqual(Service.objects.count(), 19)

    def test_command_creates_site_setting(self):
        self.run_seed()
        setting = SiteSetting.load()
        self.assertEqual(setting.site_name, "AFRILOTT HOLDING LTD")
        self.assertEqual(setting.tagline, "Efficiency in motion")
        self.assertEqual(setting.email, "info@afrilott.com")

    def test_command_creates_navigation_items(self):
        self.run_seed()
        self.assertEqual(NavigationItem.objects.filter(parent__isnull=True).count(), 5)
        services = NavigationItem.objects.get(title="Services", parent=None)
        self.assertEqual(services.children.count(), 3)
        subsidiaries = NavigationItem.objects.get(title="Subsidiaries", parent=None)
        self.assertEqual(subsidiaries.children.count(), 3)
        transtrade_nav = NavigationItem.objects.get(
            title="TransTrade Africa", parent=subsidiaries
        )
        self.assertFalse(transtrade_nav.is_external)
        self.assertEqual(transtrade_nav.url_path, "/subsidiaries/transtrade-africa/")

    def test_command_creates_hero_slides(self):
        self.run_seed()
        self.assertEqual(HeroSlide.objects.count(), 4)
        self.assertTrue(
            HeroSlide.objects.filter(title="African Logistics Trading and Technology").exists()
        )

    def test_command_creates_team_members(self):
        self.run_seed()
        self.assertEqual(TeamMember.objects.count(), 5)
        self.assertTrue(TeamMember.objects.filter(name="Ferdy TURASENGA").exists())

    def test_command_creates_service_categories(self):
        self.run_seed()
        slugs = set(ServiceCategory.objects.values_list("slug", flat=True))
        self.assertEqual(
            slugs,
            {
                "procurement-supply-chain",
                "general-trading-logistics",
                "digital-solutions",
            },
        )

    def test_command_creates_services_and_stats(self):
        self.run_seed()
        self.assertEqual(Service.objects.count(), 19)
        self.assertEqual(ServiceStat.objects.count(), 57)
        service = Service.objects.get(
            category__slug="general-trading-logistics",
            slug="petroleum-logistics",
        )
        self.assertEqual(service.stats.count(), 3)
        self.assertTrue(service.is_featured)

    def test_command_creates_subsidiaries(self):
        self.run_seed()
        self.assertEqual(Subsidiary.objects.count(), 3)
        afos = Subsidiary.objects.get(slug="afrilott-overseas")
        self.assertIn("petroleum products", afos.description)
        transtrade = Subsidiary.objects.get(slug="transtrade-africa")
        self.assertTrue(transtrade.is_external)

    def test_running_command_twice_does_not_duplicate_records(self):
        self.run_seed()
        counts_after_first = {
            "categories": ServiceCategory.objects.count(),
            "services": Service.objects.count(),
            "stats": ServiceStat.objects.count(),
            "navigation": NavigationItem.objects.count(),
            "slides": HeroSlide.objects.count(),
            "team": TeamMember.objects.count(),
            "subsidiaries": Subsidiary.objects.count(),
        }
        self.run_seed()
        self.assertEqual(ServiceCategory.objects.count(), counts_after_first["categories"])
        self.assertEqual(Service.objects.count(), counts_after_first["services"])
        self.assertEqual(ServiceStat.objects.count(), counts_after_first["stats"])
        self.assertEqual(NavigationItem.objects.count(), counts_after_first["navigation"])
        self.assertEqual(HeroSlide.objects.count(), counts_after_first["slides"])
        self.assertEqual(TeamMember.objects.count(), counts_after_first["team"])
        self.assertEqual(Subsidiary.objects.count(), counts_after_first["subsidiaries"])
        self.assertEqual(SiteSetting.objects.count(), 1)

    def test_reset_deletes_seeded_content_but_not_contact_submissions(self):
        self.run_seed()
        ContactSubmission.objects.create(
            full_name="Test User",
            email="test@example.com",
            message="Hello",
        )
        self.run_seed(reset=True)
        self.assertEqual(ServiceCategory.objects.count(), 3)
        self.assertEqual(ContactSubmission.objects.count(), 1)


class SeedSiteContentPublicRoutesTests(TestCase):
    """Public routes must remain healthy after seeding."""

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

    def test_public_routes_still_return_200_after_seed(self):
        call_command("seed_site_content")
        for url in self.ROUTES:
            with self.subTest(url=url):
                response = self.client.get(url)
                self.assertEqual(response.status_code, 200)
