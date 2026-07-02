"""Helpers for DB-first service views with page_content fallbacks."""

from __future__ import annotations

from django.templatetags.static import static

from .models import Service, ServiceCategory
from .page_content import CATEGORY_PAGES, get_category_page, get_service_detail

DEFAULT_CARD_ICON = (
    '<path d="M12 3l8 4.5v9L12 21l-8-4.5v-9z" fill="none" '
    'stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"></path>'
)

FALLBACK_INDEX_ICONS = {
    "procurement-supply-chain": (
        '<path d="M6 5h12v14H6z" stroke="currentColor" stroke-width="2"/>'
        '<path d="M9 3h6v4H9z" stroke="currentColor" stroke-width="2"/>'
        '<path d="M9 12h6M9 16h4" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>'
    ),
    "general-trading-logistics": (
        '<path d="M3 7h11v8H3z" stroke="currentColor" stroke-width="2"/>'
        '<path d="M14 10h4l3 3v2h-7z" stroke="currentColor" stroke-width="2"/>'
        '<circle cx="7" cy="17" r="2" stroke="currentColor" stroke-width="2"/>'
        '<circle cx="17" cy="17" r="2" stroke="currentColor" stroke-width="2"/>'
    ),
    "digital-solutions": (
        '<rect x="3" y="4" width="18" height="12" rx="2" stroke="currentColor" stroke-width="2"/>'
        '<path d="M8 20h8" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>'
        '<path d="M12 16v4" stroke="currentColor" stroke-width="2"/>'
    ),
}

FALLBACK_SUBSIDIARY_IMAGES = {
    "afrilott-overseas": (
        "https://images.unsplash.com/photo-1565891741441-64926e441838?w=1200&q=80"
    ),
    "transtrade-africa": (
        "https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?w=1200&q=80"
    ),
    "grittech-resources": (
        "https://images.unsplash.com/photo-1555949963-ff9fe0c870eb?w=1200&q=80"
    ),
}

FALLBACK_TEAM_PHOTOS = {
    "Ferdy TURASENGA": (
        "https://static.wixstatic.com/media/6a77e1_0771cd6c774c48829e6ddc154a5db786~mv2.jpg/"
        "v1/fill/w_411,h_413,al_c,lg_1,q_80,enc_avif,quality_auto/ferdyturasengan.jpg"
    ),
    "Eugene MBONYINSHUTI": (
        "https://static.wixstatic.com/media/6a77e1_56d00763147948fd9cbce5e6aa2aa694~mv2.jpg/"
        "v1/fill/w_536,h_538,al_c,lg_1,q_80,enc_avif,quality_auto/EugeneMBONY.jpg"
    ),
    "Maurice NGENGANYI": (
        "https://static.wixstatic.com/media/6a77e1_e5e4cee3b7344687afedac953fa9f488~mv2.jpg/"
        "v1/fill/w_474,h_492,al_c,q_80,usm_0.66_1.00_0.01,enc_avif,quality_auto/MauriceNGENGANYI.jpg"
    ),
    "Bruce MBANZABUGABO": (
        "https://static.wixstatic.com/media/6a77e1_fb892ae2070146baaf14595e3ebca3d3~mv2.jpg/"
        "v1/fill/w_474,h_492,al_c,lg_1,q_80,enc_avif,quality_auto/b.jpg"
    ),
    "Alphonse MUGISHA": (
        "https://static.wixstatic.com/media/6a77e1_eb903e06a7094222b5bc08b53fc2fe49~mv2.jpg/"
        "v1/fill/w_243,h_252,al_c,lg_1,q_80,enc_avif,quality_auto/017bebd7.jpg"
    ),
}

FALLBACK_HERO_STATIC_IMAGES = [
    "images/boat.jpg",
    "images/airplane.jpg",
    "images/truck.jpg",
    "images/laptop.jpg",
]


def resolve_image_src(src: str) -> str:
    if src.startswith(("http://", "https://", "/")):
        return src
    return static(src)


def get_fallback_card_map(category_slug: str) -> dict[str, dict]:
    page = get_category_page(category_slug)
    if page is None:
        return {}
    return {card["service_slug"]: card for card in page.get("cards", [])}


def build_category_service_cards(category: ServiceCategory, services) -> list[dict]:
    fallback_cards = get_fallback_card_map(category.slug)
    cards = []
    for service in services:
        fallback = fallback_cards.get(service.slug, {})
        cards.append(
            {
                "service": service,
                "title": service.name,
                "text": service.short_description,
                "service_slug": service.slug,
                "aos_delay": fallback.get("aos_delay", service.order * 40),
                "icon_svg": fallback.get("icon_svg", DEFAULT_CARD_ICON),
            }
        )
    return cards


def prepare_fallback_service_detail(category_slug: str, service_slug: str) -> dict:
    detail = get_service_detail(category_slug, service_slug)
    if detail is None:
        return None

    prepared = dict(detail)
    for image_key in ("main_image", "small_image"):
        image = dict(prepared[image_key])
        image["src"] = resolve_image_src(image["src"])
        prepared[image_key] = image
    return prepared


def get_service_image_context(service: Service, category_slug: str, service_slug: str) -> dict:
    fallback = get_service_detail(category_slug, service_slug) or {}
    fallback_main = fallback.get("main_image", {})
    fallback_small = fallback.get("small_image", {})

    main_src = service.main_image.url if service.main_image else ""
    if not main_src and fallback_main.get("src"):
        main_src = resolve_image_src(fallback_main["src"])

    small_src = service.secondary_image.url if service.secondary_image else ""
    if not small_src and fallback_small.get("src"):
        small_src = resolve_image_src(fallback_small["src"])

    return {
        "main_image": {
            "src": main_src,
            "alt": fallback_main.get("alt", service.name),
        },
        "small_image": {
            "src": small_src,
            "alt": fallback_small.get("alt", service.name),
        },
    }


def get_service_paragraphs(service: Service) -> list[str]:
    if service.content:
        paragraphs = [part.strip() for part in service.content.split("\n\n") if part.strip()]
        if paragraphs:
            return paragraphs
    fallback = get_service_detail(service.category.slug, service.slug)
    if fallback:
        return fallback.get("paragraphs", [])
    return [service.short_description] if service.short_description else []
