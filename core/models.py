from django.db import models


class SiteSetting(models.Model):
    """Singleton site-wide settings."""

    site_name = models.CharField(max_length=200, blank=True)
    tagline = models.CharField(max_length=255, blank=True)
    logo = models.ImageField(upload_to="site_settings/", blank=True)
    email = models.EmailField(blank=True)
    phone_primary = models.CharField(max_length=50, blank=True)
    phone_secondary = models.CharField(max_length=50, blank=True)
    address = models.TextField(blank=True)
    map_embed_url = models.URLField(blank=True)
    footer_text = models.TextField(blank=True)
    facebook_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Site Setting"
        verbose_name_plural = "Site Settings"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, _created = cls.objects.get_or_create(pk=1)
        return obj

    def __str__(self):
        return self.site_name or "Site Settings"


class NavigationItem(models.Model):
    title = models.CharField(max_length=100)
    url_name = models.CharField(max_length=100, blank=True)
    url_path = models.CharField(max_length=255, blank=True)
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="children",
    )
    order = models.PositiveIntegerField(default=0)
    is_external = models.BooleanField(default=False)
    open_in_new_tab = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["parent_id", "order", "title"]
        verbose_name = "Navigation Item"
        verbose_name_plural = "Navigation Items"

    def __str__(self):
        if self.parent:
            return f"{self.parent.title} → {self.title}"
        return self.title
