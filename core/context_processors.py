from core.models import SiteSetting
from subsidiaries.models import Subsidiary


def site_settings(request):
    """Expose singleton site settings to templates with safe fallback."""
    try:
        settings_obj = SiteSetting.objects.get(pk=1)
    except SiteSetting.DoesNotExist:
        settings_obj = None

    if settings_obj is not None and not settings_obj.site_name:
        settings_obj = None

    return {
        "site_settings": settings_obj,
    }


def subsidiary_navigation(request):
    """Expose active subsidiaries for navbar and footer menus."""
    subsidiaries = list(
        Subsidiary.objects.filter(is_active=True).order_by("order", "name")
    )
    return {
        "subsidiary_nav_items": subsidiaries,
    }
