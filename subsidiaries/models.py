from django.db import models
from django.urls import reverse


class Subsidiary(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)
    summary = models.TextField(blank=True)
    description = models.TextField(blank=True)
    logo = models.ImageField(upload_to="subsidiaries/logos/", blank=True)
    cover_image = models.ImageField(upload_to="subsidiaries/covers/", blank=True)
    website_url = models.URLField(blank=True)
    is_external = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "name"]
        verbose_name = "Subsidiary"
        verbose_name_plural = "Subsidiaries"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("subsidiaries:detail", kwargs={"slug": self.slug})
