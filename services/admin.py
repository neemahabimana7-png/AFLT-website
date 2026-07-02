from django.contrib import admin

from .models import Service, ServiceCategory, ServiceStat


class ServiceStatInline(admin.TabularInline):
    model = ServiceStat
    extra = 1
    fields = ("value", "label", "order")
    ordering = ("order",)


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "order", "is_active", "updated_at")
    list_filter = ("is_active",)
    search_fields = ("name", "slug", "short_description")
    prepopulated_fields = {"slug": ("name",)}
    list_editable = ("order", "is_active")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "slug",
        "order",
        "is_featured",
        "is_active",
        "updated_at",
    )
    list_filter = ("category", "is_featured", "is_active")
    search_fields = ("name", "slug", "short_description", "content")
    prepopulated_fields = {"slug": ("name",)}
    list_editable = ("order", "is_featured", "is_active")
    inlines = [ServiceStatInline]
    autocomplete_fields = ("category",)


@admin.register(ServiceStat)
class ServiceStatAdmin(admin.ModelAdmin):
    list_display = ("service", "value", "label", "order")
    list_filter = ("service__category",)
    search_fields = ("label", "value", "service__name")
    list_editable = ("order",)
