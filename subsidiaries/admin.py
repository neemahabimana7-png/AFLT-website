from django.contrib import admin

from .models import Subsidiary


@admin.register(Subsidiary)
class SubsidiaryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "slug",
        "order",
        "is_external",
        "is_active",
        "updated_at",
    )
    list_filter = ("is_active", "is_external")
    search_fields = ("name", "slug", "summary", "description")
    prepopulated_fields = {"slug": ("name",)}
    list_editable = ("order", "is_active")
