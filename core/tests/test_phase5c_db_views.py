from django.core.management import call_command
from django.test import TestCase
from django.urls import reverse

from pages.models import HeroSlide, TeamMember
from services.models import ServiceCategory


class Phase5CDatabaseViewTests(TestCase):
    """Phase 5C: public views use database content with safe fallback."""

    @classmethod
    def setUpTestData(cls):
        call_command("seed_site_content")

    def test_services_index_renders_db_categories(self):
        response = self.client.get(reverse("services:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Procurement &amp; Supply Chain Management")
        self.assertContains(response, "General Trading &amp; Logistics")
        self.assertContains(response, "Digital Solutions")

    def test_category_page_renders_db_services(self):
        response = self.client.get(
            reverse(
                "services:category_detail",
                kwargs={"category_slug": "procurement-supply-chain"},
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Woodworking Equipment &amp; Tools")
        self.assertContains(response, "Strategic Procurement")

    def test_service_detail_renders_db_content_and_stats(self):
        response = self.client.get(
            reverse(
                "services:service_detail",
                kwargs={
                    "category_slug": "general-trading-logistics",
                    "service_slug": "petroleum-logistics",
                },
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Petroleum Logistics")
        self.assertContains(response, "Fleet Units")
        self.assertContains(response, "petroleum-section")

    def test_subsidiaries_list_renders_db_subsidiaries(self):
        response = self.client.get(reverse("subsidiaries:list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Afrilott Overseas LLC")
        self.assertContains(response, "TransTrade Africa")
        self.assertContains(response, "Grittech Resources Ltd")

    def test_subsidiary_detail_renders_db_afos(self):
        response = self.client.get(
            reverse("subsidiaries:detail", kwargs={"slug": "afrilott-overseas"})
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "AFRILOTT Overseas LLC")
        self.assertContains(response, "Our Core Activities")

    def test_homepage_renders_db_hero_slides(self):
        response = self.client.get(reverse("pages:home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "African Logistics Trading and Technology")
        self.assertEqual(HeroSlide.objects.filter(is_active=True).count(), 4)

    def test_about_page_renders_db_team_members(self):
        response = self.client.get(reverse("pages:about"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ferdy TURASENGA")
        self.assertContains(response, "Alphonse MUGISHA")
        self.assertEqual(TeamMember.objects.filter(is_active=True).count(), 5)

    def test_footer_uses_site_settings_when_seeded(self):
        response = self.client.get(reverse("pages:home"))
        self.assertContains(response, "AFRILOTT HOLDING LTD")
        self.assertContains(response, "info@afrilott.com")

    def test_unknown_category_returns_404(self):
        response = self.client.get("/services/unknown-category/")
        self.assertEqual(response.status_code, 404)

    def test_unknown_service_returns_404(self):
        response = self.client.get(
            "/services/procurement-supply-chain/unknown-service/"
        )
        self.assertEqual(response.status_code, 404)

    def test_unknown_subsidiary_returns_404(self):
        response = self.client.get("/subsidiaries/unknown-subsidiary/")
        self.assertEqual(response.status_code, 404)

    def test_subsidiary_detail_renders_db_external_subsidiaries(self):
        for slug, name in (
            ("transtrade-africa", "TransTrade Africa"),
            ("grittech-resources", "Grittech Resources Ltd"),
        ):
            with self.subTest(slug=slug):
                response = self.client.get(
                    reverse("subsidiaries:detail", kwargs={"slug": slug})
                )
                self.assertEqual(response.status_code, 200)
                self.assertContains(response, name)
                self.assertContains(response, "Visit Website")


class Phase5CFallbackViewTests(TestCase):
    """Verify fallback rendering when database content is absent."""

    def test_services_index_fallback_without_categories(self):
        response = self.client.get(reverse("services:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Procurement &amp; Supply Chain Management")

    def test_category_fallback_without_db_category(self):
        ServiceCategory.objects.create(
            name="Inactive",
            slug="procurement-supply-chain",
            is_active=False,
        )
        response = self.client.get(
            reverse(
                "services:category_detail",
                kwargs={"category_slug": "procurement-supply-chain"},
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Woodworking Machinery")

    def test_service_detail_fallback_without_db_service(self):
        category = ServiceCategory.objects.create(
            name="Procurement",
            slug="procurement-supply-chain",
            hero_title="Procurement & Supply Chain Management",
            is_active=True,
        )
        response = self.client.get(
            reverse(
                "services:service_detail",
                kwargs={
                    "category_slug": category.slug,
                    "service_slug": "woodworking-equipment-tools",
                },
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Woodworking Equipment &amp; Tools")

    def test_homepage_fallback_without_hero_slides(self):
        response = self.client.get(reverse("pages:home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "images/boat.jpg")

    def test_about_fallback_without_team_members(self):
        response = self.client.get(reverse("pages:about"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Meet Our Team")

    def test_subsidiaries_list_fallback_without_db_records(self):
        response = self.client.get(reverse("subsidiaries:list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Our Subsidiaries")

    def test_afos_detail_fallback_without_db_record(self):
        response = self.client.get(
            reverse("subsidiaries:detail", kwargs={"slug": "afrilott-overseas"})
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Deep-Sea Commodity Trading")

    def test_external_subsidiary_detail_fallback_without_db_record(self):
        for slug, name in (
            ("transtrade-africa", "TransTrade Africa"),
            ("grittech-resources", "Grittech Resources Ltd"),
        ):
            with self.subTest(slug=slug):
                response = self.client.get(
                    reverse("subsidiaries:detail", kwargs={"slug": slug})
                )
                self.assertEqual(response.status_code, 200)
                self.assertContains(response, name)


class Phase5CPublicRoutesTests(TestCase):
    """All key public routes remain healthy."""

    ROUTES = [
        "/",
        "/about/",
        "/services/",
        "/services/procurement-supply-chain/",
        "/services/general-trading-logistics/petroleum-logistics/",
        "/services/digital-solutions/ai-data-science/",
        "/subsidiaries/",
        "/subsidiaries/afrilott-overseas/",
        "/subsidiaries/transtrade-africa/",
        "/subsidiaries/grittech-resources/",
        "/contact/",
    ]

    BROKEN_LINK_PATTERNS = (
        "../index.html",
        "../contact.html",
        "../../navbar/services.html",
        "./images/Afrilott.png",
        'href="contact.html"',
        'href="service.html"',
    )

    @classmethod
    def setUpTestData(cls):
        call_command("seed_site_content")

    def test_all_public_routes_return_200(self):
        for url in self.ROUTES:
            with self.subTest(url=url):
                response = self.client.get(url)
                self.assertEqual(response.status_code, 200)

    def test_navbar_and_footer_render(self):
        response = self.client.get("/")
        self.assertContains(response, 'id="offcanvasNavbar"')
        self.assertContains(response, 'class="site-footer"')

    def test_subsidiary_menu_links_go_to_detail_pages(self):
        response = self.client.get("/")
        self.assertContains(response, "/subsidiaries/transtrade-africa/")
        self.assertContains(response, "/subsidiaries/grittech-resources/")
        self.assertNotContains(response, "https://transtradeafrica.rw/")
        self.assertNotContains(response, "https://grittechresources.com/")

    def test_no_legacy_broken_links(self):
        for url in self.ROUTES:
            with self.subTest(url=url):
                response = self.client.get(url)
                content = response.content.decode()
                for pattern in self.BROKEN_LINK_PATTERNS:
                    self.assertNotIn(pattern, content)
