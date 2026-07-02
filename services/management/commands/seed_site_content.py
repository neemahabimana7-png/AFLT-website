"""
Seed database content from converted templates and services.page_content.

Image handling:
- Local static carousel/site images are copied into MEDIA_ROOT/seeded/.
- Remote service/team photos (Unsplash, Wix, etc.) are left blank on ImageFields.
  Source URLs remain in page_content.py until a future media-import phase.
"""

from __future__ import annotations

from django.core.management.base import BaseCommand
from django.db import transaction

from contact.models import ContactSubmission
from core.models import NavigationItem, SiteSetting
from pages.models import HeroSlide, TeamMember
from services.models import Service, ServiceCategory, ServiceStat
from services.page_content import CATEGORY_PAGES, SERVICE_DETAILS
from services.seed_utils import assign_image_if_empty
from subsidiaries.models import Subsidiary

CATEGORY_META = {
    "procurement-supply-chain": {
        "name": "Procurement & Supply Chain Management",
        "short_description": (
            "End-to-end procurement and supply chain solutions for governments, "
            "corporations, NGOs, and large-scale projects across Africa."
        ),
        "order": 1,
    },
    "general-trading-logistics": {
        "name": "General Trading & Logistics",
        "short_description": (
            "Commodity trading, freight, warehousing, customs clearance, and inland "
            "transportation for reliable regional and global delivery."
        ),
        "order": 2,
    },
    "digital-solutions": {
        "name": "Digital Solutions",
        "short_description": (
            "IT infrastructure, networking, software, hardware, CCTV, and data "
            "solutions to support modern business operations."
        ),
        "order": 3,
    },
}

FEATURED_SERVICE_SLUGS = frozenset(
    {
        "petroleum-logistics",
        "agricultural-commodities",
    }
)

MAP_EMBED_URL = (
    "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3987.5095749848395!"
    "2d30.080340!3d-1.966473!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!"
    "1s0x19dca5e5f8e1a8d%3A0x1234567890abcdef!2sKK%204%20Ave%20Gikondo%2C%20"
    "Kigugu%2C%20Kigali%2C%20Rwanda!5e0!3m2!1sen!2srw!4v1234567890"
)

AFOS_DESCRIPTION = (
    "AFRILOTT Overseas LLC is your premier partner in expert sourcing and logistic "
    "assistance for a wide range of commodities, with a particular emphasis on "
    "petroleum products. With an unwavering commitment to excellence, AFRILOTT is "
    "your ultimate partner for specialized wholesale and retail petroleum products "
    "solutions.\n\n"
    "We provide an unrivaled array of premium fuels and lubricants to fulfill a wide "
    "range of demands across the African markets.\n\n"
    "Leveraging our extensive network and industry expertise, our thorough supplier "
    "selection and quality control guarantees that only the finest products reach our "
    "clients.\n\n"
    "Our skilled logistics staff carefully plan and execute the movement, storage, and "
    "distribution of goods, ensuring that every shipment reaches its destination on "
    "time and in good condition.\n\n"
    "To facilitate our clients in remote areas with steadfast access to our products, "
    "AFRILOTT has partnered with AFRICOM SARL, a strong regional trader to create a "
    "wider supply network.\n\n"
    "Our partnership takes pride in its sole emphasis on petroleum products and serves "
    "both the wholesale and retail sectors."
)


class Command(BaseCommand):
    help = "Seed site content from hardcoded templates and services.page_content."

    def add_arguments(self, parser):
        parser.add_argument(
            "--reset",
            action="store_true",
            help=(
                "Delete seeded content for SiteSetting (fields cleared), NavigationItem, "
                "HeroSlide, TeamMember, ServiceCategory (with services/stats), and "
                "Subsidiary. Does not touch users, auth, or ContactSubmission."
            ),
        )

    def handle(self, *args, **options):
        if options["reset"]:
            self._reset_seeded_content()

        with transaction.atomic():
            summary = {
                "site_setting": self._seed_site_setting(),
                "navigation": self._seed_navigation(),
                "hero_slides": self._seed_hero_slides(),
                "team_members": self._seed_team_members(),
                "categories": self._seed_service_categories(),
                "services": self._seed_services(),
                "stats": self._seed_service_stats(),
                "subsidiaries": self._seed_subsidiaries(),
            }

        self.stdout.write(self.style.SUCCESS("Seed complete."))
        for label, count in summary.items():
            self.stdout.write(f"  {label}: {count} record(s) updated/created")

        self.stdout.write(
            self.style.WARNING(
                "Note: remote image URLs were not imported into ImageFields. "
                "Local carousel images were copied to media/seeded/ when available."
            )
        )

    def _reset_seeded_content(self):
        ServiceCategory.objects.all().delete()
        Subsidiary.objects.all().delete()
        HeroSlide.objects.all().delete()
        TeamMember.objects.all().delete()
        NavigationItem.objects.all().delete()

        setting = SiteSetting.objects.filter(pk=1).first()
        if setting is not None:
            if setting.logo:
                setting.logo.delete(save=False)
            SiteSetting.objects.filter(pk=1).update(
                site_name="",
                tagline="",
                email="",
                phone_primary="",
                phone_secondary="",
                address="",
                map_embed_url="",
                footer_text="",
                facebook_url="",
                linkedin_url="",
                twitter_url="",
                instagram_url="",
            )

        self.stdout.write(self.style.WARNING("Seeded content reset."))

    def _seed_site_setting(self) -> int:
        setting, _created = SiteSetting.objects.update_or_create(
            pk=1,
            defaults={
                "site_name": "AFRILOTT HOLDING LTD",
                "tagline": "Efficiency in motion",
                "email": "info@afrilott.com",
                "phone_primary": "+250 788 358 601",
                "phone_secondary": "+250 784 799 316",
                "address": "KK 4 Ave Gikondo, Kigali-Rwanda",
                "map_embed_url": MAP_EMBED_URL,
                "footer_text": (
                    "Logistics, Trades & Technologies. Commodity trading, procurement, "
                    "logistics, and IT solutions across Africa."
                ),
            },
        )
        assign_image_if_empty(setting.logo, "images/afrilott.png", "site")
        setting.save()
        return 1

    def _seed_navigation(self) -> int:
        count = 0
        top_level = [
            ("Home", "pages:home", "", 1, False, False),
            ("About", "pages:about", "", 2, False, False),
            ("Services", "services:index", "", 3, False, False),
            ("Subsidiaries", "subsidiaries:list", "", 4, False, False),
            ("Contact", "contact:form", "", 5, False, False),
        ]
        parents: dict[str, NavigationItem] = {}

        for title, url_name, url_path, order, is_external, open_in_new_tab in top_level:
            item, _ = NavigationItem.objects.update_or_create(
                title=title,
                parent=None,
                defaults={
                    "url_name": url_name,
                    "url_path": url_path,
                    "order": order,
                    "is_external": is_external,
                    "open_in_new_tab": open_in_new_tab,
                    "is_active": True,
                },
            )
            parents[title] = item
            count += 1

        service_children = [
            (
                "Procurement & Supply Chain",
                "",
                "/services/procurement-supply-chain/",
                1,
                False,
                False,
            ),
            (
                "General Trading & Logistics",
                "",
                "/services/general-trading-logistics/",
                2,
                False,
                False,
            ),
            (
                "Digital Solutions",
                "",
                "/services/digital-solutions/",
                3,
                False,
                False,
            ),
        ]
        for title, url_name, url_path, order, is_external, open_in_new_tab in service_children:
            NavigationItem.objects.update_or_create(
                title=title,
                parent=parents["Services"],
                defaults={
                    "url_name": url_name,
                    "url_path": url_path,
                    "order": order,
                    "is_external": is_external,
                    "open_in_new_tab": open_in_new_tab,
                    "is_active": True,
                },
            )
            count += 1

        subsidiary_children = [
            (
                "Afrilott Overseas",
                "subsidiaries:detail",
                "/subsidiaries/afrilott-overseas/",
                1,
                False,
                False,
            ),
            (
                "TransTrade Africa",
                "subsidiaries:detail",
                "/subsidiaries/transtrade-africa/",
                2,
                False,
                False,
            ),
            (
                "Grittech Resources",
                "subsidiaries:detail",
                "/subsidiaries/grittech-resources/",
                3,
                False,
                False,
            ),
        ]
        for title, url_name, url_path, order, is_external, open_in_new_tab in subsidiary_children:
            NavigationItem.objects.update_or_create(
                title=title,
                parent=parents["Subsidiaries"],
                defaults={
                    "url_name": url_name,
                    "url_path": url_path,
                    "order": order,
                    "is_external": is_external,
                    "open_in_new_tab": open_in_new_tab,
                    "is_active": True,
                },
            )
            count += 1

        return count

    def _seed_hero_slides(self) -> int:
        slides = [
            {
                "title": "African Logistics Trading and Technology",
                "subtitle": "Efficiency in motion",
                "static_image": "images/boat.jpg",
                "cta_label": "Learn more",
                "cta_url_name": "pages:about",
                "order": 1,
            },
            {
                "title": "African Logistics Trading and Technology",
                "subtitle": "Efficiency in motion",
                "static_image": "images/airplane.jpg",
                "cta_label": "Learn more",
                "cta_url_name": "pages:about",
                "order": 2,
            },
            {
                "title": "African Logistics Trading and Technology",
                "subtitle": "Efficiency in motion",
                "static_image": "images/truck.jpg",
                "cta_label": "Learn more",
                "cta_url_name": "pages:about",
                "order": 3,
            },
            {
                "title": "African Logistics Trading and Technology",
                "subtitle": "Efficiency in motion",
                "static_image": "images/laptop.jpg",
                "cta_label": "Contact us",
                "cta_url_name": "contact:form",
                "order": 4,
            },
        ]

        count = 0
        for slide_data in slides:
            slide, _ = HeroSlide.objects.update_or_create(
                order=slide_data["order"],
                defaults={
                    "title": slide_data["title"],
                    "subtitle": slide_data["subtitle"],
                    "cta_label": slide_data["cta_label"],
                    "cta_url_name": slide_data["cta_url_name"],
                    "cta_url": "",
                    "is_active": True,
                },
            )
            assign_image_if_empty(
                slide.image,
                slide_data["static_image"],
                "hero",
            )
            slide.save()
            count += 1
        return count

    def _seed_team_members(self) -> int:
        members = [
            ("Ferdy TURASENGA", "Executive Chairman", 1),
            ("Eugene MBONYINSHUTI", "Managing Director", 2),
            ("Maurice NGENGANYI", "Bidding and Aquisitions Manager", 3),
            ("Bruce MBANZABUGABO", "Sales and Marketing Manager", 4),
            ("Alphonse MUGISHA", "Project Analyst", 5),
        ]
        count = 0
        for name, role, order in members:
            TeamMember.objects.update_or_create(
                name=name,
                defaults={
                    "role": role,
                    "order": order,
                    "bio": "",
                    "linkedin_url": "",
                    "is_active": True,
                },
            )
            count += 1
        return count

    def _seed_service_categories(self) -> int:
        count = 0
        for slug, meta in CATEGORY_META.items():
            page = CATEGORY_PAGES[slug]
            ServiceCategory.objects.update_or_create(
                slug=slug,
                defaults={
                    "name": meta["name"],
                    "short_description": meta["short_description"],
                    "hero_title": page["hero_title"],
                    "hero_text": "",
                    "icon_class": "",
                    "order": meta["order"],
                    "is_active": True,
                },
            )
            count += 1
        return count

    def _card_lookup(self) -> dict[tuple[str, str], dict]:
        lookup: dict[tuple[str, str], dict] = {}
        for category_slug, page in CATEGORY_PAGES.items():
            for index, card in enumerate(page["cards"], start=1):
                lookup[(category_slug, card["service_slug"])] = {
                    "card": card,
                    "order": index,
                }
        return lookup

    def _seed_services(self) -> int:
        card_lookup = self._card_lookup()
        count = 0

        for (category_slug, service_slug), detail in SERVICE_DETAILS.items():
            category = ServiceCategory.objects.get(slug=category_slug)
            card_info = card_lookup.get((category_slug, service_slug), {})
            card = card_info.get("card", {})
            order = card_info.get("order", 0)
            paragraphs = detail.get("paragraphs", [])
            content = "\n\n".join(paragraphs)

            service, _ = Service.objects.update_or_create(
                category=category,
                slug=service_slug,
                defaults={
                    "name": detail["title"],
                    "short_description": card.get("text", paragraphs[0] if paragraphs else ""),
                    "content": content,
                    "hero_title": detail["title"],
                    "hero_text": card.get("text", ""),
                    "order": order,
                    "is_featured": service_slug in FEATURED_SERVICE_SLUGS,
                    "is_active": True,
                },
            )

            main_src = detail.get("main_image", {}).get("src", "")
            if main_src.startswith("images/"):
                assign_image_if_empty(service.main_image, main_src, "services/main")
            if detail.get("small_image", {}).get("src", "").startswith("images/"):
                assign_image_if_empty(
                    service.secondary_image,
                    detail["small_image"]["src"],
                    "services/secondary",
                )
            service.save()
            count += 1

        return count

    def _seed_service_stats(self) -> int:
        count = 0
        for (category_slug, service_slug), detail in SERVICE_DETAILS.items():
            service = Service.objects.get(
                category__slug=category_slug,
                slug=service_slug,
            )
            for index, stat in enumerate(detail.get("stats", []), start=1):
                ServiceStat.objects.update_or_create(
                    service=service,
                    order=index,
                    defaults={
                        "label": stat["label"],
                        "value": stat["value"],
                    },
                )
                count += 1
        return count

    def _seed_subsidiaries(self) -> int:
        subsidiaries = [
            {
                "slug": "afrilott-overseas",
                "name": "Afrilott Overseas LLC",
                "summary": (
                    "Specialized in petroleum sourcing, procurement, and regional "
                    "distribution support."
                ),
                "description": AFOS_DESCRIPTION,
                "website_url": "",
                "is_external": False,
                "order": 1,
            },
            {
                "slug": "transtrade-africa",
                "name": "TransTrade Africa",
                "summary": (
                    "Cross-border commodity flow, warehousing, and freight coordination "
                    "for growth markets."
                ),
                "description": (
                    "TransTrade Africa supports cross-border commodity flow, warehousing, "
                    "and freight coordination for growth markets across the region. The "
                    "company works as part of the AFRILOTT ecosystem to connect suppliers, "
                    "storage, and distribution channels for reliable trade outcomes."
                ),
                "website_url": "https://transtradeafrica.rw/",
                "is_external": True,
                "order": 2,
            },
            {
                "slug": "grittech-resources",
                "name": "Grittech Resources Ltd",
                "summary": (
                    "Industrial tools, technical solutions, and project support tailored "
                    "for enterprise operations."
                ),
                "description": (
                    "Grittech Resources Ltd provides industrial tools, technical solutions, "
                    "and project support tailored for enterprise operations. The subsidiary "
                    "helps clients source, deploy, and maintain equipment and technical "
                    "resources needed for demanding industrial environments."
                ),
                "website_url": "https://grittechresources.com/",
                "is_external": True,
                "order": 3,
            },
        ]

        count = 0
        for data in subsidiaries:
            Subsidiary.objects.update_or_create(
                slug=data["slug"],
                defaults={
                    "name": data["name"],
                    "summary": data["summary"],
                    "description": data["description"],
                    "website_url": data["website_url"],
                    "is_external": data["is_external"],
                    "order": data["order"],
                    "is_active": True,
                },
            )
            count += 1
        return count
