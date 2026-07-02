from pathlib import Path

from django.conf import settings
from django.test import SimpleTestCase


class StaticAssetTests(SimpleTestCase):
    """Verify Phase 2 static files exist in the Django static directory."""

    static_root = Path(settings.STATICFILES_DIRS[0])

    required_css = [
    "css/base.css",
    "css/main.css",
    "css/pages/about.css",
    "css/pages/contact.css",
    "css/pages/home.css",
    "css/pages/service-category.css",
    "css/pages/service-detail.css",
    "css/pages/services.css",
    "css/pages/subsidiaries.css",
    "css/pages/subsidiary-detail.css",
    ]

    required_js = [
    "js/main.js",
    "js/aos-init.js",
    "js/reveal-observer.js",
    "js/service-detail-effects.js",
    "js/home-slider.js",
    ]

    required_images = [
    "images/afrilott.png",
    "images/aflt-1.jpg",
    "images/aflt-2.jpg",
    "images/aflt-3.png",
    "images/airplane.jpg",
    "images/boat.jpg",
    "images/laptop.jpg",
    "images/truck.jpg",
    ]

    def test_required_css_files_exist(self):
        for relative_path in self.required_css:
            with self.subTest(path=relative_path):
                self.assertTrue((self.static_root / relative_path).is_file())

    def test_required_js_files_exist(self):
        for relative_path in self.required_js:
            with self.subTest(path=relative_path):
                self.assertTrue((self.static_root / relative_path).is_file())

    def test_required_image_files_exist(self):
        for relative_path in self.required_images:
            with self.subTest(path=relative_path):
                self.assertTrue((self.static_root / relative_path).is_file())

    def test_original_static_site_untouched(self):
        project_root = Path(settings.BASE_DIR)
        self.assertTrue((project_root / "navbar" / "index.html").is_file())
        self.assertTrue((project_root / "images" / "Afrilott.png").is_file())
