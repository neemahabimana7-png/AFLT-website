from django.test import TestCase
from django.urls import reverse


class HomepageConversionTests(TestCase):
    """Phase 4A: verify converted homepage content and links."""

    def test_home_returns_200(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_homepage_contains_hero_text(self):
        response = self.client.get(reverse("pages:home"))
        self.assertContains(response, "African Logistics Trading and Technology")

    def test_homepage_contains_static_carousel_image(self):
        response = self.client.get(reverse("pages:home"))
        self.assertContains(response, "/static/images/boat.jpg")
        self.assertContains(response, "/static/images/airplane.jpg")

    def test_homepage_contains_services_link(self):
        response = self.client.get(reverse("pages:home"))
        services_url = reverse("services:category_detail", kwargs={"category_slug": "procurement-supply-chain"})
        self.assertContains(response, services_url)

    def test_homepage_uses_shared_navbar_and_footer(self):
        response = self.client.get(reverse("pages:home"))
        self.assertContains(response, 'id="offcanvasNavbar"')
        self.assertContains(response, 'class="site-footer"')

    def test_homepage_has_no_broken_legacy_links(self):
        response = self.client.get(reverse("pages:home"))
        content = response.content.decode()
        self.assertNotIn('href="../index.html"', content)
        self.assertNotIn('href="../contact.html"', content)
        self.assertNotIn('href="../../navbar/services.html"', content)
        self.assertNotIn('href="../"', content)
        self.assertNotIn('href="about.html"', content)
        self.assertNotIn('href="contact.html"', content)
        self.assertNotIn('href="service.html"', content)
        self.assertNotIn('href="index.html"', content)

    def test_homepage_contains_company_intro(self):
        response = self.client.get(reverse("pages:home"))
        self.assertContains(response, "AFRILOTT HOLDING LTD")
        self.assertContains(response, "established in 2010")

    def test_homepage_contains_contact_section(self):
        response = self.client.get(reverse("pages:home"))
        self.assertContains(response, "CONTACT US")
        self.assertContains(response, "RWANDA")

    def test_homepage_contains_map_section(self):
        response = self.client.get(reverse("pages:home"))
        self.assertContains(response, 'class="map-section"')
        self.assertContains(response, "google.com/maps/embed")
