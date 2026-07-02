from django.contrib import admin

from .models import HeroSlide, TeamMember


@admin.register(HeroSlide)
class HeroSlideAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "is_active", "cta_label", "updated_at")
    list_filter = ("is_active",)
    search_fields = ("title", "subtitle", "cta_label")
    list_editable = ("order", "is_active")


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ("name", "role", "order", "is_active", "updated_at")
    list_filter = ("is_active",)
    search_fields = ("name", "role", "bio")
    list_editable = ("order", "is_active")
