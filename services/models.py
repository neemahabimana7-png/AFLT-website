from django.db import models
from django.urls import reverse


class ServiceCategory(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)
    short_description = models.TextField(blank=True)
    hero_title = models.CharField(max_length=200, blank=True)
    hero_text = models.TextField(blank=True)
    icon_class = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to="service_categories/", blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "name"]
        verbose_name = "Service Category"
        verbose_name_plural = "Service Categories"

    def __str__(self):
        return self.name


class Service(models.Model):
    category = models.ForeignKey(
        ServiceCategory,
        on_delete=models.CASCADE,
        related_name="services",
    )
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100)
    short_description = models.TextField(blank=True)
    content = models.TextField(blank=True)
    main_image = models.ImageField(upload_to="services/main/", blank=True)
    secondary_image = models.ImageField(upload_to="services/secondary/", blank=True)
    hero_title = models.CharField(max_length=200, blank=True)
    hero_text = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["category", "order", "name"]
        constraints = [
            models.UniqueConstraint(
                fields=["category", "slug"],
                name="unique_service_slug_per_category",
            )
        ]
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self):
        return f"{self.category.name}: {self.name}"

    def get_absolute_url(self):
        return reverse(
            "services:service_detail",
            kwargs={
                "category_slug": self.category.slug,
                "service_slug": self.slug,
            },
        )


class ServiceStat(models.Model):
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name="stats",
    )
    label = models.CharField(max_length=100)
    value = models.CharField(max_length=50)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "label"]
        verbose_name = "Service Stat"
        verbose_name_plural = "Service Stats"

    def __str__(self):
        return f"{self.service.name}: {self.value} {self.label}"
