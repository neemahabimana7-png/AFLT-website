from django.http import Http404
from django.shortcuts import render

from services.view_helpers import FALLBACK_SUBSIDIARY_IMAGES

from .fallback_content import FALLBACK_SUBSIDIARY_DETAILS
from .models import Subsidiary


def _attach_fallback_image(subsidiary):
    subsidiary.fallback_image = FALLBACK_SUBSIDIARY_IMAGES.get(subsidiary.slug, "")
    return subsidiary


def list_view(request):
    subsidiaries = list(
        Subsidiary.objects.filter(is_active=True).order_by("order", "name")
    )
    for subsidiary in subsidiaries:
        _attach_fallback_image(subsidiary)
    return render(
        request,
        "subsidiaries/list.html",
        {
            "subsidiaries": subsidiaries,
            "use_database": bool(subsidiaries),
            "fallback_subsidiary_images": FALLBACK_SUBSIDIARY_IMAGES,
        },
    )


def detail(request, slug):
    try:
        subsidiary = Subsidiary.objects.get(slug=slug, is_active=True)
        _attach_fallback_image(subsidiary)
        return render(
            request,
            "subsidiaries/detail.html",
            {
                "slug": slug,
                "subsidiary": subsidiary,
                "use_database": True,
                "is_afos": slug == "afrilott-overseas",
            },
        )
    except Subsidiary.DoesNotExist:
        pass

    if slug == "afrilott-overseas":
        return render(
            request,
            "subsidiaries/detail.html",
            {
                "slug": slug,
                "use_database": False,
                "is_afos": True,
            },
        )

    fallback = FALLBACK_SUBSIDIARY_DETAILS.get(slug)
    if fallback is not None:
        return render(
            request,
            "subsidiaries/detail.html",
            {
                "slug": slug,
                "subsidiary": type(
                    "FallbackSubsidiary",
                    (),
                    {
                        **fallback,
                        "fallback_image": FALLBACK_SUBSIDIARY_IMAGES.get(slug, ""),
                        "cover_image": None,
                    },
                )(),
                "use_database": False,
                "is_afos": False,
            },
        )

    raise Http404("Subsidiary not found")
