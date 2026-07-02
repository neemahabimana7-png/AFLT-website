from django.http import Http404
from django.shortcuts import render

from .models import Service, ServiceCategory
from .page_content import get_category_page, is_valid_category, is_valid_service
from .view_helpers import (
    build_category_service_cards,
    get_service_image_context,
    get_service_paragraphs,
    prepare_fallback_service_detail,
)


def index(request):
    categories = list(
        ServiceCategory.objects.filter(is_active=True).order_by("order", "name")
    )
    return render(
        request,
        "services/index.html",
        {
            "categories": categories,
            "use_database": bool(categories),
        },
    )


def category_detail(request, category_slug):
    try:
        category = ServiceCategory.objects.get(slug=category_slug, is_active=True)
    except ServiceCategory.DoesNotExist:
        category = None

    if category is not None:
        services = category.services.filter(is_active=True).order_by("order", "name")
        return render(
            request,
            "services/category.html",
            {
                "category_slug": category_slug,
                "category": category,
                "services": services,
                "service_cards": build_category_service_cards(category, services),
                "use_database": True,
            },
        )

    if not is_valid_category(category_slug):
        raise Http404("Service category not found")

    category_page = get_category_page(category_slug)
    if category_page is None:
        raise Http404("Service category not found")

    return render(
        request,
        "services/category.html",
        {
            "category_slug": category_slug,
            "category_page": category_page,
            "use_database": False,
        },
    )


def service_detail(request, category_slug, service_slug):
    try:
        service = (
            Service.objects.select_related("category")
            .prefetch_related("stats")
            .get(
                category__slug=category_slug,
                slug=service_slug,
                is_active=True,
                category__is_active=True,
            )
        )
    except Service.DoesNotExist:
        service = None

    if service is not None:
        images = get_service_image_context(service, category_slug, service_slug)
        return render(
            request,
            "services/detail.html",
            {
                "category_slug": category_slug,
                "service_slug": service_slug,
                "service": service,
                "category": service.category,
                "stats": service.stats.all(),
                "paragraphs": get_service_paragraphs(service),
                "main_image": images["main_image"],
                "small_image": images["small_image"],
                "category_page_label": service.category.hero_title or service.category.name,
                "use_database": True,
            },
        )

    if not is_valid_service(category_slug, service_slug):
        raise Http404("Service not found")

    category_page = get_category_page(category_slug)
    if category_page is None:
        raise Http404("Service category not found")

    fallback_service = prepare_fallback_service_detail(category_slug, service_slug)
    if fallback_service is None:
        raise Http404("Service not found")

    return render(
        request,
        "services/detail.html",
        {
            "category_slug": category_slug,
            "service_slug": service_slug,
            "service": fallback_service,
            "stats": fallback_service.get("stats", []),
            "paragraphs": fallback_service.get("paragraphs", []),
            "main_image": fallback_service["main_image"],
            "small_image": fallback_service["small_image"],
            "category_page_label": category_page["hero_title"],
            "use_database": False,
        },
    )
