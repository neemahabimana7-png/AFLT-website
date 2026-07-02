# External Vendor Assets (CDN)

Phase 2 keeps CDN usage unchanged. Documented for Django `base.html` references.

## CSS

| Library | URL | Used on |
|---------|-----|---------|
| Bootstrap 5.3.8 | `https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css` | All pages |
| AOS 2.3.1 | `https://unpkg.com/aos@2.3.1/dist/aos.css` | Most pages except `afos.html`, `subsidia.html` |
| Font Awesome 6.5.1 | `https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css` | `subsidiaries-section/afos.html` |
| Google Fonts (Manrope, Sora) | `https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Sora:wght@500;600;700;800&display=swap` | Service detail pages |

## JavaScript

| Library | URL | Used on |
|---------|-----|---------|
| Bootstrap bundle 5.3.8 | `https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js` | All pages |
| AOS 2.3.1 | `https://unpkg.com/aos@2.3.1/dist/aos.js` | Pages with AOS animations |

## External images (not copied in Phase 2)

Remote images remain on Wix, Pexels, Unsplash, epcafrica.com, etc.
Localize critical assets in a later phase if needed.

## Local vendor folder

`static/vendor/` is reserved for optional future self-hosted copies.
No vendor files are downloaded in Phase 2.
