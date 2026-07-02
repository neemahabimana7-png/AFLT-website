# Image Filename Mapping (Phase 2)

Original files in `images/` are unchanged. Copies below live in `static/images/` with normalized names for Django `{% static %}` usage.

| Original path | Django static path |
|---------------|-------------------|
| `images/Afrilott.png` | `static/images/afrilott.png` |
| `images/AFLT 1.jpg.jpeg` | `static/images/aflt-1.jpg` |
| `images/AFLT 2.jpg.jpeg` | `static/images/aflt-2.jpg` |
| `images/AFLT 3.png` | `static/images/aflt-3.png` |
| `images/Airplane.jpg` | `static/images/airplane.jpg` |
| `images/Boat.jpg` | `static/images/boat.jpg` |
| `images/laptop.jpg` | `static/images/laptop.jpg` |
| `images/truck.jpg` | `static/images/truck.jpg` |

## Usage in Phase 4 templates

```django
{% load static %}
<img src="{% static 'images/afrilott.png' %}" alt="Afrilott">
```

## External images

Remote URLs (Wix, Pexels, Unsplash, etc.) remain in HTML until a later localization phase.
