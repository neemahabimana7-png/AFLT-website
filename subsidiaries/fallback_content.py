"""Fallback subsidiary content when database records are missing."""

FALLBACK_SUBSIDIARY_DETAILS = {
    "transtrade-africa": {
        "name": "TransTrade Africa",
        "summary": (
            "Cross-border commodity flow, warehousing, and freight coordination "
            "for growth markets."
        ),
        "description": (
            "TransTrade Africa supports cross-border commodity flow, warehousing, "
            "and freight coordination for growth markets across the region. The "
            "company works as part of the AFRILOTT ecosystem to connect suppliers, "
            "storage, and distribution channels for reliable trade outcomes."
        ),
        "website_url": "https://transtradeafrica.rw/",
        "is_external": True,
    },
    "grittech-resources": {
        "name": "Grittech Resources Ltd",
        "summary": (
            "Industrial tools, technical solutions, and project support tailored "
            "for enterprise operations."
        ),
        "description": (
            "Grittech Resources Ltd provides industrial tools, technical solutions, "
            "and project support tailored for enterprise operations. The subsidiary "
            "helps clients source, deploy, and maintain equipment and technical "
            "resources needed for demanding industrial environments."
        ),
        "website_url": "https://grittechresources.com/",
        "is_external": True,
    },
}

FALLBACK_SUBSIDIARY_SLUGS = frozenset(FALLBACK_SUBSIDIARY_DETAILS.keys()) | frozenset(
    {"afrilott-overseas"}
)
