"""Helpers for seeding media files from static assets."""

from __future__ import annotations

import shutil
from pathlib import Path

from django.conf import settings
from django.core.files import File


def copy_static_image_to_media(static_relative_path: str, media_subdir: str) -> str | None:
    """
    Copy a file from static/ into MEDIA_ROOT/seeded/<media_subdir>/.

    Returns the relative media path (for ImageField.name) or None if missing.
    """
    source = settings.BASE_DIR / "static" / static_relative_path
    if not source.is_file():
        return None

    destination_dir = settings.MEDIA_ROOT / "seeded" / media_subdir
    destination_dir.mkdir(parents=True, exist_ok=True)
    destination = destination_dir / source.name

    if not destination.exists():
        shutil.copy2(source, destination)

    return f"seeded/{media_subdir}/{source.name}"


def assign_image_if_empty(image_field, static_relative_path: str, media_subdir: str) -> bool:
    """Assign a copied static image to an ImageField when it is currently empty."""
    if image_field:
        return False

    media_relative_path = copy_static_image_to_media(static_relative_path, media_subdir)
    if media_relative_path is None:
        return False

    absolute_path = settings.MEDIA_ROOT / media_relative_path
    with absolute_path.open("rb") as image_file:
        image_field.save(absolute_path.name, File(image_file), save=False)
    return True
