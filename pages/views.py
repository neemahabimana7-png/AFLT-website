from django.shortcuts import render

from pages.models import HeroSlide, TeamMember
from services.view_helpers import FALLBACK_HERO_STATIC_IMAGES, FALLBACK_TEAM_PHOTOS


def home(request):
    hero_slides = list(HeroSlide.objects.filter(is_active=True).order_by("order"))
    for index, slide in enumerate(hero_slides):
        if index < len(FALLBACK_HERO_STATIC_IMAGES):
            slide.static_fallback = FALLBACK_HERO_STATIC_IMAGES[index]
        else:
            slide.static_fallback = FALLBACK_HERO_STATIC_IMAGES[0]
    return render(
        request,
        "pages/home.html",
        {
            "hero_slides": hero_slides,
            "use_database_hero": bool(hero_slides),
            "fallback_hero_images": FALLBACK_HERO_STATIC_IMAGES,
        },
    )


def about(request):
    team_members = list(
        TeamMember.objects.filter(is_active=True).order_by("order", "name")
    )
    for member in team_members:
        member.fallback_photo = FALLBACK_TEAM_PHOTOS.get(member.name, "")
    return render(
        request,
        "pages/about.html",
        {
            "team_members": team_members,
            "use_database_team": bool(team_members),
            "fallback_team_photos": FALLBACK_TEAM_PHOTOS,
        },
    )
