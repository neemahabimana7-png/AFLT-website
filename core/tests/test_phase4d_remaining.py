from django.test import TestCase
from django.urls import reverse

from services.page_content import SERVICE_DETAILS, VALID_CATEGORY_SLUGS, VALID_SERVICE_SLUGS


class Phase4DConversionTests(TestCase):
    """Phase 4D: remaining static pages converted to Django templates."""

    CATEGORY_ROUTES = (
        ("procurement-supply-chain", "Procurement &amp; Supply Chain Management"),
        ("general-trading-logistics", "General Trading &amp; Logistics"),
        ("digital-solutions", "Digital Solutions"),
    )

    SERVICE_DETAIL_ROUTES = (
        ("procurement-supply-chain", "woodworking-equipment-tools", "Woodworking Equipment &amp; Tools"),
        ("procurement-supply-chain", "strategic-sourcing-procurement", "Strategic Procurement"),
        ("procurement-supply-chain", "industrial-equipment-supplies", "Industrial Equipment Supply"),
        ("procurement-supply-chain", "laboratory-medical-equipment", "Laboratory Equipment"),
        ("procurement-supply-chain", "furniture-appliances", "Furniture"),
        ("procurement-supply-chain", "specialized-equipment", "Specialized Equipment"),
        ("general-trading-logistics", "petroleum-logistics", "Petroleum Logistics"),
        ("general-trading-logistics", "ocean-freight", "Ocean Freight Services"),
        ("general-trading-logistics", "agricultural-commodities", "Agricultural Commodities"),
        ("general-trading-logistics", "air-freight", "Air Freight Services"),
        ("general-trading-logistics", "inland-transportation", "Inland Transportation"),
        ("general-trading-logistics", "customs-clearance", "Customs Clearance"),
        ("general-trading-logistics", "warehousing-distribution", "Warehousing Solutions"),
        ("digital-solutions", "it-consulting-managed-services", "IT Solutions"),
        ("digital-solutions", "networking-infrastructure", "Network Solutions"),
        ("digital-solutions", "cctv-surveillance", "CCTV"),
        ("digital-solutions", "hardware-devices", "Hardware Systems"),
        ("digital-solutions", "software-solutions", "Software Solutions"),
        ("digital-solutions", "ai-data-science", "AI &amp; Data Science"),
    )

    BROKEN_LINK_PATTERNS = (
        "../index.html",
        "../contact.html",
        "../../navbar/services.html",
        "./images/Afrilott.png",
        'href="contact.html"',
        'href="service.html"',
        'href="afos.html"',
    )

    def _assert_shared_layout(self, response):
        self.assertContains(response, 'id="offcanvasNavbar"')
        self.assertContains(response, 'class="site-footer"')

    def _assert_no_legacy_links(self, response):
        content = response.content.decode()
        for pattern in self.BROKEN_LINK_PATTERNS:
            with self.subTest(pattern=pattern):
                self.assertNotIn(pattern, content)

    def test_all_category_routes_return_200(self):
        for slug, _ in self.CATEGORY_ROUTES:
            with self.subTest(slug=slug):
                response = self.client.get(
                    reverse("services:category_detail", kwargs={"category_slug": slug})
                )
                self.assertEqual(response.status_code, 200)

    def test_category_pages_include_category_css(self):
        for slug, _ in self.CATEGORY_ROUTES:
            with self.subTest(slug=slug):
                response = self.client.get(
                    reverse("services:category_detail", kwargs={"category_slug": slug})
                )
                self.assertContains(response, "/static/css/pages/service-category.css")

    def test_category_pages_contain_hero_and_cards(self):
        for slug, hero_text in self.CATEGORY_ROUTES:
            with self.subTest(slug=slug):
                response = self.client.get(
                    reverse("services:category_detail", kwargs={"category_slug": slug})
                )
                self._assert_shared_layout(response)
                self.assertContains(response, hero_text)
                self.assertContains(response, "psm-service-card")
                self.assertContains(response, "What We Do")

    def test_category_pages_link_to_service_details(self):
        for category_slug in VALID_CATEGORY_SLUGS:
            response = self.client.get(
                reverse("services:category_detail", kwargs={"category_slug": category_slug})
            )
            for service_slug in VALID_SERVICE_SLUGS[category_slug]:
                detail_url = reverse(
                    "services:service_detail",
                    kwargs={
                        "category_slug": category_slug,
                        "service_slug": service_slug,
                    },
                )
                with self.subTest(category=category_slug, service=service_slug):
                    self.assertContains(response, detail_url)

    def test_all_service_detail_routes_return_200(self):
        for category_slug, service_slug, _ in self.SERVICE_DETAIL_ROUTES:
            with self.subTest(category=category_slug, service=service_slug):
                response = self.client.get(
                    reverse(
                        "services:service_detail",
                        kwargs={
                            "category_slug": category_slug,
                            "service_slug": service_slug,
                        },
                    )
                )
                self.assertEqual(response.status_code, 200)

    def test_service_detail_pages_include_detail_css(self):
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

    def test_service_detail_pages_contain_key_content(self):
        for category_slug, service_slug, snippet in self.SERVICE_DETAIL_ROUTES:
            with self.subTest(category=category_slug, service=service_slug):
                response = self.client.get(
                    reverse(
                        "services:service_detail",
                        kwargs={
                            "category_slug": category_slug,
                            "service_slug": service_slug,
                        },
                    )
                )
                self._assert_shared_layout(response)
                self.assertContains(response, snippet)
                self.assertContains(response, "petroleum-section")
                self.assertContains(response, reverse("services:index"))
                self.assertContains(
                    response,
                    reverse("services:category_detail", kwargs={"category_slug": category_slug}),
                )

    def test_service_detail_count_matches_content_module(self):
        self.assertEqual(len(SERVICE_DETAILS), 19)

    def test_subsidiaries_list_returns_200(self):
        response = self.client.get(reverse("subsidiaries:list"))
        self.assertEqual(response.status_code, 200)

    def test_subsidiaries_list_includes_css_and_content(self):
        response = self.client.get(reverse("subsidiaries:list"))
        self._assert_shared_layout(response)
        self.assertContains(response, "/static/css/pages/subsidiaries.css")
        self.assertContains(response, "Our Subsidiaries")
        self.assertContains(response, "TransTrade Africa")
        self.assertContains(
            response,
            reverse("subsidiaries:detail", kwargs={"slug": "afrilott-overseas"}),
        )

    def test_subsidiary_detail_returns_200(self):
        response = self.client.get(
            reverse("subsidiaries:detail", kwargs={"slug": "afrilott-overseas"})
        )
        self.assertEqual(response.status_code, 200)

    def test_subsidiary_detail_includes_css_and_content(self):
        response = self.client.get(
            reverse("subsidiaries:detail", kwargs={"slug": "afrilott-overseas"})
        )
        self._assert_shared_layout(response)
        self.assertContains(response, "/static/css/pages/subsidiary-detail.css")
        self.assertContains(response, "AFRILOTT Overseas LLC")
        self.assertContains(response, "Our Core Activities")

    def test_contact_page_returns_200(self):
        response = self.client.get(reverse("contact:form"))
        self.assertEqual(response.status_code, 200)

    def test_contact_page_includes_css_and_form(self):
        response = self.client.get(reverse("contact:form"))
        self._assert_shared_layout(response)
        self.assertContains(response, "/static/css/pages/contact.css")
        self.assertContains(response, "GET IN TOUCH")
        self.assertContains(response, 'class="contact-form"')
        self.assertContains(response, "Kigali, Rwanda")

    def test_contact_page_has_no_broken_legacy_links(self):
        response = self.client.get(reverse("contact:form"))
        self._assert_no_legacy_links(response)
        self.assertContains(
            response,
            reverse("subsidiaries:detail", kwargs={"slug": "afrilott-overseas"}),
        )

    def test_converted_pages_have_no_broken_legacy_links(self):
        pages = [
            reverse("services:category_detail", kwargs={"category_slug": "digital-solutions"}),
            reverse(
                "services:service_detail",
                kwargs={
                    "category_slug": "digital-solutions",
                    "service_slug": "ai-data-science",
                },
            ),
            reverse("subsidiaries:list"),
            reverse("subsidiaries:detail", kwargs={"slug": "afrilott-overseas"}),
            reverse("contact:form"),
        ]
        for url in pages:
            with self.subTest(url=url):
                response = self.client.get(url)
                self._assert_no_legacy_links(response)

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
