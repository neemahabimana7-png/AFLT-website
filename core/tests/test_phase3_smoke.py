from django.test import TestCase
from django.urls import reverse


class Phase3RouteSmokeTests(TestCase):
    """Verify Phase 3 placeholder routes render shared layout."""

    routes = [
        ("pages:home", []),
        ("pages:about", []),
        ("services:index", []),
        (
            "services:category_detail",
            [],
            {"category_slug": "procurement-supply-chain"},
        ),
        (
            "services:service_detail",
            [],
            {"category_slug": "digital-solutions", "service_slug": "ai-data-science"},
        ),
        ("subsidiaries:list", []),
        ("subsidiaries:detail", [], {"slug": "afrilott-overseas"}),
        ("contact:form", []),
    ]

    def test_all_phase3_routes_return_200(self):
        for route in self.routes:
            name = route[0]
            args = route[1]
            kwargs = route[2] if len(route) > 2 else {}
            with self.subTest(route=name):
                url = reverse(name, args=args, kwargs=kwargs)
                response = self.client.get(url)
                self.assertEqual(response.status_code, 200)

    def test_rendered_pages_include_navbar(self):
        response = self.client.get(reverse("pages:home"))
        self.assertContains(response, 'class="navbar')
        self.assertContains(response, 'id="offcanvasNavbar"')

    def test_rendered_pages_include_footer(self):
        response = self.client.get(reverse("pages:home"))
        self.assertContains(response, 'class="site-footer"')
        self.assertContains(response, "AFRILOTT HOLDING LTD")

    def test_rendered_pages_include_main_css(self):
        response = self.client.get(reverse("pages:home"))
        self.assertContains(response, "/static/css/main.css")

    def test_services_page_includes_services_navigation_url(self):
        response = self.client.get(reverse("services:index"))
        services_url = reverse("services:index")
        self.assertContains(response, services_url)
        self.assertContains(response, reverse("services:category_detail", kwargs={"category_slug": "digital-solutions"}))

    def test_contact_page_includes_contact_url(self):
        response = self.client.get(reverse("contact:form"))
        self.assertContains(response, reverse("contact:form"))

    def test_about_page_includes_page_css(self):
        response = self.client.get(reverse("pages:about"))
        self.assertContains(response, "/static/css/pages/about.css")

    def test_service_detail_page_includes_detail_css(self):
        response = self.client.get(
            reverse(
                "services:service_detail",
                kwargs={
                    "category_slug": "general-trading-logistics",
                    "service_slug": "petroleum-logistics",
                },
            )
        )
        self.assertContains(response, "/static/css/pages/service-detail.css")
