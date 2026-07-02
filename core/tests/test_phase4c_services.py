from django.test import TestCase
from django.urls import reverse


class ServicesIndexConversionTests(TestCase):
    """Phase 4C: verify converted Services index page content and links."""

    CATEGORY_SLUGS = (
        "procurement-supply-chain",
        "general-trading-logistics",
        "digital-solutions",
    )

    def test_services_index_returns_200(self):
        response = self.client.get("/services/")
        self.assertEqual(response.status_code, 200)

    def test_services_page_contains_expected_headings(self):
        response = self.client.get(reverse("services:index"))
        self.assertContains(response, "Our Services")
        self.assertContains(response, "What We Do")

    def test_services_page_includes_services_css(self):
        response = self.client.get(reverse("services:index"))
        self.assertContains(response, "/static/css/pages/services.css")

    def test_services_page_uses_shared_navbar_and_footer(self):
        response = self.client.get(reverse("services:index"))
        self.assertContains(response, 'id="offcanvasNavbar"')
        self.assertContains(response, 'class="site-footer"')

    def test_services_page_includes_all_category_routes(self):
        response = self.client.get(reverse("services:index"))
        for slug in self.CATEGORY_SLUGS:
            with self.subTest(slug=slug):
                self.assertContains(response, reverse("services:category_detail", kwargs={"category_slug": slug}))

    def test_services_page_has_no_broken_legacy_links(self):
        response = self.client.get(reverse("services:index"))
        content = response.content.decode()
        self.assertNotIn("./images/Afrilott.png", content)
        self.assertNotIn('href="service.html"', content)
        self.assertNotIn('href="services.html"', content)
        self.assertNotIn('href="../index.html"', content)
        self.assertNotIn('href="../contact.html"', content)
        self.assertNotIn('href="../../navbar/services.html"', content)

    def test_services_page_contains_hero_section(self):
        response = self.client.get(reverse("services:index"))
        self.assertContains(response, 'class="services-hero"')
        self.assertContains(response, 'class="services-hero-text"')

    def test_services_page_contains_category_cards(self):
        response = self.client.get(reverse("services:index"))
        self.assertContains(response, "Procurement &amp; Supply Chain Management")
        self.assertContains(response, "General Trading &amp; Logistics")
        self.assertContains(response, "Digital Solutions")
        self.assertContains(response, "service-card")
