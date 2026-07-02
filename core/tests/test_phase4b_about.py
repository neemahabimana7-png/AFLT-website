from django.test import TestCase
from django.urls import reverse


class AboutPageConversionTests(TestCase):
    """Phase 4B: verify converted About page content and links."""

    def test_about_returns_200(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_about_page_contains_who_we_are_content(self):
        response = self.client.get(reverse("pages:about"))
        self.assertContains(response, "ABOUT US")
        self.assertContains(response, "Efficiency")
        self.assertContains(response, "in motion.")

    def test_about_page_includes_about_css(self):
        response = self.client.get(reverse("pages:about"))
        self.assertContains(response, "/static/css/pages/about.css")

    def test_about_page_uses_shared_navbar_and_footer(self):
        response = self.client.get(reverse("pages:about"))
        self.assertContains(response, 'id="offcanvasNavbar"')
        self.assertContains(response, 'class="site-footer"')

    def test_about_page_contains_mission_vision(self):
        response = self.client.get(reverse("pages:about"))
        self.assertContains(response, "Mission &amp; Vision")
        self.assertContains(response, "Our Mission")
        self.assertContains(response, "Our Vision")
        self.assertContains(response, "Transforming African trade")

    def test_about_page_contains_team_section(self):
        response = self.client.get(reverse("pages:about"))
        self.assertContains(response, "Meet Our Team")
        self.assertContains(response, "Ferdy TURASENGA")
        self.assertContains(response, "Executive Chairman")
        self.assertContains(response, "history-card-title")

    def test_about_page_has_no_broken_legacy_links(self):
        response = self.client.get(reverse("pages:about"))
        content = response.content.decode()
        self.assertNotIn('href="../contact.html"', content)
        self.assertNotIn('href="service.html"', content)
        self.assertNotIn('href="services.html"', content)
        self.assertNotIn('href="../../navbar/services.html"', content)
        self.assertNotIn('href="about.html"', content)
        self.assertNotIn('href="index.html"', content)

    def test_about_page_contains_history_slider_markup(self):
        response = self.client.get(reverse("pages:about"))
        self.assertContains(response, "Our Journey")
        self.assertContains(response, "history-dots")
        self.assertContains(response, "Since 2010: 14+ years of excellence.")

    def test_about_page_loads_history_slider_js(self):
        response = self.client.get(reverse("pages:about"))
        self.assertContains(response, "/static/js/home-slider.js")
