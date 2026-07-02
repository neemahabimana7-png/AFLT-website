from django.contrib import admin

from .models import NavigationItem, SiteSetting


@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ("site_name", "email", "phone_primary", "updated_at")

    def has_add_permission(self, request):
        return not SiteSetting.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(NavigationItem)
class NavigationItemAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "parent",
        "order",
        "url_name",
        "url_path",
        "is_external",
        "is_active",
    )
    list_filter = ("is_active", "is_external", "parent")
    search_fields = ("title", "url_name", "url_path")
    list_editable = ("order", "is_active")
