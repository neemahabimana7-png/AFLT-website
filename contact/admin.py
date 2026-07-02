from django.contrib import admin

from .models import ContactSubmission


@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "email",
        "status",
        "is_read",
        "source_page",
        "created_at",
    )
    list_filter = ("status", "is_read", "created_at")
    search_fields = ("full_name", "email", "company", "message", "source_page")
    readonly_fields = ("created_at",)
    list_editable = ("status", "is_read")
