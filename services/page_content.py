"""Hardcoded service page content migrated from static HTML sources."""

VALID_CATEGORY_SLUGS = frozenset(
    {
        'digital-solutions',
        'general-trading-logistics',
        'procurement-supply-chain',
    }
)

VALID_SERVICE_SLUGS = {
    'digital-solutions': frozenset(
        {
            'ai-data-science',
            'cctv-surveillance',
            'hardware-devices',
            'it-consulting-managed-services',
            'networking-infrastructure',
            'software-solutions',
        }
    ),
    'general-trading-logistics': frozenset(
        {
            'agricultural-commodities',
            'air-freight',
            'customs-clearance',
            'inland-transportation',
            'ocean-freight',
            'petroleum-logistics',
            'warehousing-distribution',
        }
    ),
    'procurement-supply-chain': frozenset(
        {
            'furniture-appliances',
            'industrial-equipment-supplies',
            'laboratory-medical-equipment',
            'specialized-equipment',
            'strategic-sourcing-procurement',
            'woodworking-equipment-tools',
        }
    ),
}

CATEGORY_PAGES = {
    'digital-solutions': {
        "hero_title": 'Digital Solutions',
        "page_title": 'Digital Solutions',
        "cards": [
            {
                "title": 'IT Infrastructure Solutions',
                "text": 'End-to-end IT infrastructure setup, server installation and data center solutions.',
                "service_slug": 'it-consulting-managed-services',
                "aos_delay": 40,
                "icon_svg": '<rect x="2" y="3" width="20" height="14" rx="1" fill="none" stroke="currentColor" stroke-width="1.8"></rect> <path d="M7 21h10M12 17v4" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"></path> <path d="M6 8h12M6 11h8" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"></path>',
            },
            {
                "title": 'Network Solutions',
                "text": 'Reliable networking solutions including structured cabling, switches and routers.',
                "service_slug": 'networking-infrastructure',
                "aos_delay": 100,
                "icon_svg": '<circle cx="12" cy="12" r="4" fill="none" stroke="currentColor" stroke-width="1.8"></circle> <path d="M12 2v3M12 19v3M2 12h3M19 12h3" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"></path> <path d="M5.6 5.6l2.1 2.1M16.3 16.3l2.1 2.1M5.6 18.4l2.1-2.1M16.3 7.7l2.1-2.1" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"></path>',
            },
            {
                "title": 'CCTV & Surveillance Systems',
                "text": 'Advanced surveillance systems for real-time monitoring and enhanced security.',
                "service_slug": 'cctv-surveillance',
                "aos_delay": 160,
                "icon_svg": '<circle cx="12" cy="10" r="4" fill="none" stroke="currentColor" stroke-width="1.8"></circle> <path d="M5 20a7 7 0 0 1 14 0" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"></path> <path d="M18 5l2-2M6 5L4 3" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"></path>',
            },
            {
                "title": 'Hardware Supply',
                "text": 'Supply of computers, laptops, printers, servers and other IT hardware.',
                "service_slug": 'hardware-devices',
                "aos_delay": 220,
                "icon_svg": '<rect x="3" y="5" width="14" height="10" rx="1" fill="none" stroke="currentColor" stroke-width="1.8"></rect> <path d="M17 9h2l2 3v2h-4" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"></path> <circle cx="7" cy="17" r="1.4" fill="currentColor"></circle> <circle cx="18" cy="17" r="1.4" fill="currentColor"></circle>',
            },
            {
                "title": 'Software Solutions',
                "text": 'Business software, licenses and tools to improve productivity.',
                "service_slug": 'software-solutions',
                "aos_delay": 280,
                "icon_svg": '<rect x="3" y="3" width="18" height="18" rx="2" fill="none" stroke="currentColor" stroke-width="1.8"></rect> <path d="M8 10l2 2-2 2M12 14h4" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"></path>',
            },
            {
                "title": 'AI & Data Science',
                "text": 'Data-driven insights and AI solutions to help your business grow.',
                "service_slug": 'ai-data-science',
                "aos_delay": 340,
                "icon_svg": '<path d="M12 3C8 7 5 10 5 13a7 7 0 0 0 14 0c0-3-3-6-7-10z" fill="none" stroke="currentColor" stroke-width="1.8"></path> <path d="M9 15c0-1.7 1.3-3 3-3s3 1.3 3 3" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"></path>',
            },
        ],
    },
    'general-trading-logistics': {
        "hero_title": 'General Trading & Logistics',
        "page_title": 'General Trading & Logistics',
        "cards": [
            {
                "title": 'Oil & Petroleum Products Supply',
                "text": 'Reliable supply of premium petroleum products for wholesale and retail markets.',
                "service_slug": 'petroleum-logistics',
                "aos_delay": 340,
                "icon_svg": '<path d="M12 3c3.6 4.1 5.5 7.1 5.5 9.5A5.5 5.5 0 1 1 6.5 12.5C6.5 10.1 8.4 7.1 12 3z" fill="none" stroke="currentColor" stroke-width="1.8"></path>',
            },
            {
                "title": 'Ocean Freight Services',
                "text": 'Efficient and secure sea freight solutions connecting global markets.',
                "service_slug": 'ocean-freight',
                "aos_delay": 40,
                "icon_svg": '<path d="M2.5 17.5h19M4 17.5V9h16v8.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"></path> <path d="M8 9V6h8v3" fill="none" stroke="currentColor" stroke-width="1.8"></path> <circle cx="8" cy="18" r="1.3" fill="currentColor"></circle> <circle cx="16" cy="18" r="1.3" fill="currentColor"></circle>',
            },
            {
                "title": 'Agricultural Commodities',
                "text": 'Reliable sourcing and distribution of high-quality agricultural commodities for local and international markets.',
                "service_slug": 'agricultural-commodities',
                "aos_delay": 420,
                "icon_svg": '<path d="M12 3v18M7 8c1.4-1.2 2.8-1.8 5-2m5 2c-1.4-1.2-2.8-1.8-5-2M7 16c1.2-1 2.5-1.6 5-1.8m5 1.8c-1.2-1-2.5-1.6-5-1.8" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"></path>',
            },
            {
                "title": 'Air Freight Services',
                "text": 'Fast and reliable air cargo solutions for time-sensitive shipments.',
                "service_slug": 'air-freight',
                "aos_delay": 100,
                "icon_svg": '<path d="M3 13l7-2 3-4 2 1-1 3 4 2 3-1v2l-3 1-4-1-2 3-2-1 1-3-6-1z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"></path>',
            },
            {
                "title": 'Inland Transportation',
                "text": 'Safe and timely road transportation across regions.',
                "service_slug": 'inland-transportation',
                "aos_delay": 160,
                "icon_svg": '<path d="M3 16h13V9H3v7z" fill="none" stroke="currentColor" stroke-width="1.8"></path> <path d="M16 12h3l2 2v2h-5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"></path> <circle cx="7" cy="17" r="1.4" fill="currentColor"></circle> <circle cx="18" cy="17" r="1.4" fill="currentColor"></circle>',
            },
            {
                "title": 'Customs Clearance',
                "text": 'Hassle-free customs documentation and clearance services.',
                "service_slug": 'customs-clearance',
                "aos_delay": 220,
                "icon_svg": '<path d="M7 4h10v16H7z" fill="none" stroke="currentColor" stroke-width="1.8"></path> <path d="M9.5 9.5h5M9.5 13h5M9.5 16.5h3" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"></path> <path d="M10 2h4v3h-4z" fill="none" stroke="currentColor" stroke-width="1.8"></path>',
            },
            {
                "title": 'Warehousing Solutions',
                "text": 'Secure and well-managed warehousing for short and long-term storage.',
                "service_slug": 'warehousing-distribution',
                "aos_delay": 280,
                "icon_svg": '<path d="M4 10l8-6 8 6v10H4z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"></path> <path d="M9 20v-5h6v5" fill="none" stroke="currentColor" stroke-width="1.8"></path>',
            },
        ],
    },
    'procurement-supply-chain': {
        "hero_title": 'Procurement & Supply Chain Management',
        "page_title": 'Services',
        "cards": [
            {
                "title": 'Woodworking Machinery',
                "text": 'Supplying durable woodworking machinery and workshop tools for industrial and commercial production.',
                "service_slug": 'woodworking-equipment-tools',
                "aos_delay": 380,
                "icon_svg": '<path d="M4 18h7l-2.5-2.5L16 8l2.5 2.5L21 8l-5-5-2.5 2.5L16 8 8.5 15.5 6 13z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"></path>',
            },
            {
                "title": 'Strategic Procurement',
                "text": 'We source quality products from trusted global and local suppliers, ensuring value and reliability.',
                "service_slug": 'strategic-sourcing-procurement',
                "aos_delay": 40,
                "icon_svg": '<path d="M6 5h12v14H6z" fill="none" stroke="currentColor" stroke-width="1.8"></path> <path d="M9 3h6v4H9z" fill="none" stroke="currentColor" stroke-width="1.8"></path> <path d="M9 12h6M9 16h4" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"></path>',
            },
            {
                "title": 'Industrial Equipment Supply',
                "text": 'Supplying reliable industrial machinery and equipment for diverse sectors.',
                "service_slug": 'industrial-equipment-supplies',
                "aos_delay": 100,
                "icon_svg": '<path d="M12 3l8 4.5v9L12 21l-8-4.5v-9z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"></path> <path d="M12 3v9m0 0l8-4.5m-8 4.5L4 7.5" fill="none" stroke="currentColor" stroke-width="1.8"></path>',
            },
            {
                "title": 'Laboratory Equipment & Consumables',
                "text": 'Providing advanced laboratory instruments and consumables for accurate results.',
                "service_slug": 'laboratory-medical-equipment',
                "aos_delay": 160,
                "icon_svg": '<path d="M9 3h6l1 4H8l1-4z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"></path> <path d="M10 7v4l-4 7h12l-4-7V7" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"></path>',
            },
            {
                "title": 'Furniture & Appliances Supply',
                "text": 'Supplying office, home and institutional furniture and appliances for every need.',
                "service_slug": 'furniture-appliances',
                "aos_delay": 220,
                "icon_svg": '<path d="M4 8h16v8H4z" fill="none" stroke="currentColor" stroke-width="1.8"></path> <path d="M8 8V6h8v2m-9 8h2m8 0h2" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"></path>',
            },
            {
                "title": 'Specialized Equipment & Tools',
                "text": 'Supplying precision tools and specialized equipment for industrial applications.',
                "service_slug": 'specialized-equipment',
                "aos_delay": 280,
                "icon_svg": '<path d="M6 6l12 12M18 6L6 18" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"></path> <circle cx="8" cy="8" r="2" fill="none" stroke="currentColor" stroke-width="1.8"></circle> <circle cx="16" cy="16" r="2" fill="none" stroke="currentColor" stroke-width="1.8"></circle>',
            },
        ],
    },
}

SERVICE_DETAILS = {
    ('digital-solutions', 'ai-data-science'): {
        "title": 'AI & Data Science',
        "page_title": 'AI & Data Science - AFRILOTT',
        "paragraphs": [
            'AFRILOTT empowers organizations through AI and data science solutions that turn information into insights, automation, and smarter decision-making.',
            'We help clients leverage predictive analytics, intelligent automation, and data-driven strategies to improve efficiency, identify opportunities, and stay competitive.',
            'Our AI and data science services are designed to deliver practical value across operations, planning, reporting, and customer experience.',
        ],
        "stats": [
            {
                "value": '80+',
                "label": 'Data Projects',
            },
            {
                "value": '40%',
                "label": 'Faster Decisions',
            },
            {
                "value": '24/7',
                "label": 'Analytics Support',
            },
        ],
        "main_image": {
            "src": 'https://images.unsplash.com/photo-1677442136019-21780ecad995?auto=format&fit=crop&w=1200&q=80',
            "alt": 'AI and Data Science',
        },
        "small_image": {
            "src": 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=1200&q=80',
            "alt": 'Data Analysis',
        },
    },
    ('digital-solutions', 'cctv-surveillance'): {
        "title": 'CCTV & Surveillance Systems',
        "page_title": 'CCTV & Surveillance Systems - AFRILOTT',
        "paragraphs": [
            'AFRILOTT delivers advanced CCTV and surveillance systems designed to strengthen security, improve visibility, and support safer operations across homes, offices, and commercial properties.',
            'Our solutions include high-definition cameras, remote monitoring, intelligent recording, and scalable system design to meet the needs of both small and large sites.',
            'We combine dependable technology with professional installation to ensure effective protection and peace of mind for our clients.',
        ],
        "stats": [
            {
                "value": '100+',
                "label": 'Security Installations',
            },
            {
                "value": '24/7',
                "label": 'Remote Monitoring',
            },
            {
                "value": '99%',
                "label": 'System Uptime',
            },
        ],
        "main_image": {
            "src": 'https://images.unsplash.com/photo-1581578731548-c64695cc6952?auto=format&fit=crop&w=1200&q=80',
            "alt": 'CCTV Systems',
        },
        "small_image": {
            "src": 'https://images.unsplash.com/photo-1552664730-d307ca884978?auto=format&fit=crop&w=1200&q=80',
            "alt": 'Surveillance Installation',
        },
    },
    ('digital-solutions', 'hardware-devices'): {
        "title": 'Hardware Systems',
        "page_title": 'Hardware Systems - AFRILOTT',
        "paragraphs": [
            'AFRILOTT offers dependable hardware systems that support efficient computing, secure operations, and long-term business performance through quality devices and infrastructure.',
            'We supply and install servers, workstations, networking devices, peripherals, and other essential hardware tailored to business requirements and future scalability.',
            'Our approach ensures clients receive reliable equipment, professional setup, and ongoing support that keeps technology performing at its best.',
        ],
        "stats": [
            {
                "value": '500+',
                "label": 'Hardware Units',
            },
            {
                "value": '100%',
                "label": 'Certified Equipment',
            },
            {
                "value": '24/7',
                "label": 'Maintenance Support',
            },
        ],
        "main_image": {
            "src": 'https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&w=1200&q=80',
            "alt": 'Hardware Systems',
        },
        "small_image": {
            "src": 'https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=1200&q=80',
            "alt": 'IT Hardware Setup',
        },
    },
    ('digital-solutions', 'it-consulting-managed-services'): {
        "title": 'IT Solutions',
        "page_title": 'IT Solutions - AFRILOTT',
        "paragraphs": [
            'AFRILOTT is a leading provider of comprehensive IT solutions for businesses of all sizes. With a team of highly skilled professionals & a commitment to delivering excellence, we specialize in supplying top-quality computer hardware and software, installation and maintenance of IT infrastructure, security and surveillance solutions such as CCTV camera systems and Drone technology.',
            'Our goal is to help businesses enhance their productivity, efficiency, and security through reliable and cost-effective IT solutions.',
            "We collaborate with leading hardware manufacturers to deliver customized solutions that align with our clients' specific requirements.",
        ],
        "stats": [
            {
                "value": '500+',
                "label": 'Clients Served',
            },
            {
                "value": '1000+',
                "label": 'IT Projects',
            },
            {
                "value": '24/7',
                "label": 'Technical Support',
            },
        ],
        "main_image": {
            "src": 'https://plus.unsplash.com/premium_photo-1714618849685-89cad85746b1?q=80&w=1288&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
            "alt": 'IT Solutions and technology',
        },
        "small_image": {
            "src": 'https://images.unsplash.com/photo-1517694712202-14dd9538aa97?auto=format&fit=crop&w=1200&q=80',
            "alt": 'Computer hardware and equipment',
        },
    },
    ('digital-solutions', 'networking-infrastructure'): {
        "title": 'Network Solutions',
        "page_title": 'Network Solutions - AFRILOTT',
        "paragraphs": [
            'AFRILOTT delivers reliable network solutions that keep businesses connected, secure, and ready for growth through robust infrastructure and intelligent design.',
            'From structured cabling and wireless connectivity to secure data exchange, our networking services are tailored to support communication, collaboration, and operational efficiency.',
            'We help organizations build future-ready networks that are scalable, resilient, and aligned with their day-to-day business requirements.',
        ],
        "stats": [
            {
                "value": '250+',
                "label": 'Connected Sites',
            },
            {
                "value": '99.9%',
                "label": 'Network Uptime',
            },
            {
                "value": '24/7',
                "label": 'Support',
            },
        ],
        "main_image": {
            "src": 'https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=1200&q=80',
            "alt": 'Network Solutions',
        },
        "small_image": {
            "src": 'https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&w=1200&q=80',
            "alt": 'Networking Infrastructure',
        },
    },
    ('digital-solutions', 'software-solutions'): {
        "title": 'Software Solutions',
        "page_title": 'Software Solutions - AFRILOTT',
        "paragraphs": [
            'AFRILOTT provides customized software solutions that help businesses streamline operations, improve productivity, and make smarter decisions through technology.',
            'From business applications and automation tools to integration and support services, our software offerings are built to improve efficiency and simplify daily workflows.',
            'We work closely with clients to create practical digital tools that are intuitive, reliable, and aligned with organizational goals.',
        ],
        "stats": [
            {
                "value": '150+',
                "label": 'Software Deployments',
            },
            {
                "value": '95%',
                "label": 'Client Satisfaction',
            },
            {
                "value": '24/7',
                "label": 'Technical Support',
            },
        ],
        "main_image": {
            "src": 'https://images.unsplash.com/photo-1516321497487-e288fb19713f?auto=format&fit=crop&w=1200&q=80',
            "alt": 'Software Solutions',
        },
        "small_image": {
            "src": 'https://images.unsplash.com/photo-1555099962-4199c345e5dd?auto=format&fit=crop&w=1200&q=80',
            "alt": 'Software Development',
        },
    },
    ('general-trading-logistics', 'agricultural-commodities'): {
        "title": 'Agricultural Commodities',
        "page_title": 'Petroleum Logistics - AFRILOTT',
        "paragraphs": [
            'AFRILOTT supports the trade and movement of agricultural commodities with reliable sourcing, efficient logistics, and strong market access across regional and international channels.',
            'We connect producers, suppliers, and buyers through structured trade solutions that cover quality assurance, timely delivery, and end-to-end coordination from origin to destination.',
            'Our expertise in agricultural commodities enables clients to benefit from dependable supply chains, competitive pricing, and seamless handling of bulk and value-added products.',
        ],
        "stats": [
            {
                "value": '30+',
                "label": 'Commodity Partnerships',
            },
            {
                "value": '24/7',
                "label": 'Supply Coordination',
            },
            {
                "value": '100%',
                "label": 'Quality Focus',
            },
        ],
        "main_image": {
            "src": 'https://media.istockphoto.com/id/990083620/fr/photo/chariots-de-manutention-des-sacs-de-sucre-pour-le-rembourrage-dans-le-r%C3%A9cipient-pour.jpg?b=1&s=612x612&w=0&k=20&c=D3GN1206xyeCyDrt_nyaI-0Hsmo_zc8A9GFm0K7ssyg=',
            "alt": 'Agricultural Commodities',
        },
        "small_image": {
            "src": 'https://images.pexels.com/photos/7420980/pexels-photo-7420980.jpeg',
            "alt": 'Agricultural Trade Team',
        },
    },
    ('general-trading-logistics', 'air-freight'): {
        "title": 'Air Freight Services',
        "page_title": 'Air Freight Services - AFRILOTT',
        "paragraphs": [
            'AFRILOTT delivers fast and dependable air freight services for urgent shipments that require speed, precision, and secure handling.',
            'Our air cargo solutions support time-sensitive deliveries, high-value goods, and critical supply chain needs with coordinated airport handling and tracking support.',
            'From door-to-door movement to priority bookings, we help clients stay agile while maintaining reliability and visibility throughout transit.',
        ],
        "stats": [
            {
                "value": '50+',
                "label": 'Air Routes',
            },
            {
                "value": '24/7',
                "label": 'Priority Support',
            },
            {
                "value": '99%',
                "label": 'Service Reliability',
            },
        ],
        "main_image": {
            "src": 'https://media.istockphoto.com/id/1431570827/photo/cargo-plane-flying-above-stack-of-containers-at-container-port.jpg?s=2048x2048&w=is&k=20&c=zvtgXudO83_-s4n1vKyYVuLmle__HnfiQj-ZnXvrkOw=',
            "alt": 'Air Freight Services',
        },
        "small_image": {
            "src": 'https://images.pexels.com/photos/9749472/pexels-photo-9749472.jpeg',
            "alt": 'Air Cargo Operations',
        },
    },
    ('general-trading-logistics', 'customs-clearance'): {
        "title": 'Customs Clearance',
        "page_title": 'Customs Clearance - AFRILOTT',
        "paragraphs": [
            'AFRILOTT offers efficient customs clearance services that help clients navigate import and export procedures with confidence and compliance.',
            'Our team manages documentation, regulatory requirements, and processing coordination to reduce delays and keep shipments moving smoothly through border checkpoints.',
            'With deep knowledge of trade regulations and a strong partner network, we ensure that every clearance process is handled accurately and professionally.',
        ],
        "stats": [
            {
                "value": '100+',
                "label": 'Clearances Monthly',
            },
            {
                "value": '98%',
                "label": 'Compliance Rate',
            },
            {
                "value": '24/7',
                "label": 'Support',
            },
        ],
        "main_image": {
            "src": 'images/aflt-2.jpg',
            "alt": 'Customs Clearance',
        },
        "small_image": {
            "src": 'images/aflt-3.png',
            "alt": 'Customs Support Team',
        },
    },
    ('general-trading-logistics', 'inland-transportation'): {
        "title": 'Inland Transportation',
        "page_title": 'Inland Transportation - AFRILOTT',
        "paragraphs": [
            'AFRILOTT provides reliable inland transportation services that connect major trade points with efficient road freight solutions across the region.',
            'From scheduled deliveries to urgent shipments, our transport network supports timely movement of goods with strong route planning and responsive dispatch operations.',
            'We help clients reduce transit risks and improve delivery performance through dependable vehicles, experienced drivers, and coordinated logistics support.',
        ],
        "stats": [
            {
                "value": '200+',
                "label": 'Transport Routes',
            },
            {
                "value": '24/7',
                "label": 'Dispatch Support',
            },
            {
                "value": '95%',
                "label": 'On-Time Delivery',
            },
        ],
        "main_image": {
            "src": 'images/aflt-2.jpg',
            "alt": 'Inland Transportation',
        },
        "small_image": {
            "src": 'images/aflt-1.jpg',
            "alt": 'Transport Operations',
        },
    },
    ('general-trading-logistics', 'ocean-freight'): {
        "title": 'Ocean Freight Services',
        "page_title": 'Petroleum Logistics - AFRILOTT',
        "paragraphs": [
            'AFRILOTT delivers dependable ocean freight solutions for businesses moving cargo across international trade routes with efficiency, safety, and transparency.',
            'From full container loads to consolidated shipments, we coordinate port handling, customs support, and end-to-end logistics to keep goods moving smoothly from origin to destination.',
            'Our trusted network of shipping partners and experienced logistics professionals helps clients reduce transit risks, optimize costs, and maintain reliable delivery schedules.',
        ],
        "stats": [
            {
                "value": '100+',
                "label": 'Trade Lanes',
            },
            {
                "value": '24/7',
                "label": 'Shipment Tracking',
            },
            {
                "value": '98%',
                "label": 'On-Time Delivery',
            },
        ],
        "main_image": {
            "src": 'https://images.pexels.com/photos/20712621/pexels-photo-20712621.jpeg',
            "alt": 'Ocean Freight Operations',
        },
        "small_image": {
            "src": 'https://images.pexels.com/photos/38095258/pexels-photo-38095258.jpeg',
            "alt": 'Ocean Freight Team',
        },
    },
    ('general-trading-logistics', 'petroleum-logistics'): {
        "title": 'Petroleum Logistics',
        "page_title": 'Petroleum Logistics - AFRILOTT',
        "paragraphs": [
            'AFRILOTT is a trusted petroleum logistics provider, delivering safe, reliable, and efficient transportation of fuel and petroleum products across the region.',
            'Through a modern fleet of specialized fuel tankers and experienced personnel, we ensure secure handling and timely delivery while maintaining the highest standards of safety and compliance.',
            'Our advanced fleet management systems and dedicated customer-focused approach enable us to provide seamless, professional, and cost-effective petroleum transport services.',
        ],
        "stats": [
            {
                "value": '50+',
                "label": 'Fleet Units',
            },
            {
                "value": '24/7',
                "label": 'Operations',
            },
            {
                "value": '100%',
                "label": 'Safety Focused',
            },
        ],
        "main_image": {
            "src": 'images/aflt-2.jpg',
            "alt": 'Petroleum Logistics',
        },
        "small_image": {
            "src": 'images/aflt-3.png',
            "alt": 'Petroleum Team',
        },
    },
    ('general-trading-logistics', 'warehousing-distribution'): {
        "title": 'Warehousing Solutions',
        "page_title": 'Warehousing Solutions - AFRILOTT',
        "paragraphs": [
            'AFRILOTT provides secure and flexible warehousing solutions designed to support efficient storage, inventory control, and seamless distribution for businesses of all sizes.',
            'Our facilities are equipped to handle a diverse range of cargo, offering organized storage, real-time tracking, and dependable handling for goods at every stage of the supply chain.',
            'Whether for short-term transit storage or long-term inventory management, our warehousing services help clients optimize operations while maintaining safety and accessibility.',
        ],
        "stats": [
            {
                "value": '20+',
                "label": 'Storage Facilities',
            },
            {
                "value": '24/7',
                "label": 'Site Monitoring',
            },
            {
                "value": '99%',
                "label": 'Inventory Accuracy',
            },
        ],
        "main_image": {
            "src": 'https://images.pexels.com/photos/34718922/pexels-photo-34718922.jpeg',
            "alt": 'Warehousing Solutions',
        },
        "small_image": {
            "src": 'https://images.pexels.com/photos/12069525/pexels-photo-12069525.jpeg',
            "alt": 'Warehouse Operations',
        },
    },
    ('procurement-supply-chain', 'furniture-appliances'): {
        "title": 'Supply and Installation of Furniture & Appliances',
        "page_title": 'Supply & Installation of Furniture & Appliances - AFRILOTT',
        "paragraphs": [
            'Afrilott Holding Ltd provides end-to-end solutions for the supply and professional installation of high-quality furniture and appliances for residential, commercial, and institutional projects.',
            'Our services cover procurement, logistics, delivery, assembly, and installation, ensuring durability, functionality, and aesthetic alignment with client requirements.',
            'We partner with reputable manufacturers and brands to guarantee quality, while our experienced technical teams ensure timely execution and compliance with project specifications and safety standards.',
        ],
        "stats": [
            {
                "value": '120+',
                "label": 'Projects Delivered',
            },
            {
                "value": '24/7',
                "label": 'Client Support',
            },
            {
                "value": '100%',
                "label": 'Installation Quality Focus',
            },
        ],
        "main_image": {
            "src": 'https://images.unsplash.com/photo-1497366811353-6870744d04b2?auto=format&fit=crop&w=1200&q=80',
            "alt": 'Modern office furniture installation',
        },
        "small_image": {
            "src": 'https://images.unsplash.com/photo-1618221195710-dd6b41faaea6?auto=format&fit=crop&w=1200&q=80',
            "alt": 'Interior furniture and appliance setup',
        },
    },
    ('procurement-supply-chain', 'industrial-equipment-supplies'): {
        "title": 'Industrial Equipment Supply',
        "page_title": 'Industrial Equipment Supply - AFRILOTT',
        "paragraphs": [
            'AFRILOTT is a leading supplier of industrial equipment, providing businesses across Africa with high-quality machinery, tools, and technical solutions sourced from trusted manufacturers worldwide. We cater to sectors including construction, manufacturing, mining, and energy.',
            'Our team of procurement experts manages the entire supply process — from identifying the right equipment specifications to handling importation, customs clearance, and on-site delivery. We ensure every unit meets industry standards and client requirements before it reaches your facility.',
            'With strong relationships with global manufacturers and distributors, AFRILOTT guarantees competitive pricing, reliable lead times, and after-sales technical support — empowering your operations with the equipment they need to perform at peak efficiency.',
        ],
        "stats": [
            {
                "value": '500+',
                "label": 'Equipment Units',
            },
            {
                "value": '30+',
                "label": 'Industry Sectors',
            },
            {
                "value": '100%',
                "label": 'Quality Assured',
            },
        ],
        "main_image": {
            "src": 'images/aflt-2.jpg',
            "alt": 'Industrial Equipment Supply',
        },
        "small_image": {
            "src": 'images/aflt-3.png',
            "alt": 'Industrial Equipment Team',
        },
    },
    ('procurement-supply-chain', 'laboratory-medical-equipment'): {
        "title": 'Laboratory Equipment & Consumables',
        "page_title": 'Laboratory Equipment & Consumables - AFRILOTT',
        "paragraphs": [
            'AFRILOTT is a trusted supplier of laboratory equipment and consumables, serving research institutions, hospitals, universities, and industrial laboratories across Africa. We source precision instruments, analytical tools, and scientific supplies from internationally certified manufacturers.',
            'Our product range covers diagnostic equipment, glassware, reagents, safety consumables, microscopes, centrifuges, and specialised testing instruments. We manage procurement, quality verification, importation, and delivery — ensuring every item arrives in perfect condition and fully compliant with relevant standards.',
            'With an extensive network of global suppliers and a dedicated in-house procurement team, AFRILOTT delivers competitive pricing, reliable timelines, and responsive after-sales support — keeping your laboratory operations running without interruption.',
        ],
        "stats": [
            {
                "value": '1,000+',
                "label": 'Products Supplied',
            },
            {
                "value": '50+',
                "label": 'Lab Partners',
            },
            {
                "value": '100%',
                "label": 'Certified Quality',
            },
        ],
        "main_image": {
            "src": 'https://images.unsplash.com/photo-1657778751969-1ed46209bb67?q=80&w=1074&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
            "alt": 'Laboratory Equipment',
        },
        "small_image": {
            "src": 'https://images.unsplash.com/photo-1738778151587-032287ae9f90?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
            "alt": 'Laboratory Consumables',
        },
    },
    ('procurement-supply-chain', 'specialized-equipment'): {
        "title": 'Specialized Equipment & Tools',
        "page_title": 'Specialized Equipment & Tools - AFRILOTT',
        "paragraphs": [
            'AFRILOTT is a leading provider of specialized equipment and tools procurement solutions. With our expertise and industry knowledge, we are dedicated to meeting the unique needs of businesses and organizations requiring top-quality equipment for various applications.',
            'Our extensive network of trusted suppliers and manufacturers enables us to source and deliver cutting-edge tools tailored to your specific requirements.',
            'From advanced machinery to specialized instruments, we offer a comprehensive range of products designed to enhance productivity and efficiency across industries.',
        ],
        "stats": [
            {
                "value": '300+',
                "label": 'Equipment Types',
            },
            {
                "value": '50+',
                "label": 'Trusted Suppliers',
            },
            {
                "value": '100%',
                "label": 'Quality Oriented',
            },
        ],
        "main_image": {
            "src": 'https://images.unsplash.com/photo-1657778751969-1ed46209bb67?q=80&w=1074&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
            "alt": 'Specialized equipment',
        },
        "small_image": {
            "src": 'https://images.unsplash.com/photo-1511379938547-c1f69419868d?auto=format&fit=crop&w=1200&q=80',
            "alt": 'Precision tools and instruments',
        },
    },
    ('procurement-supply-chain', 'strategic-sourcing-procurement'): {
        "title": 'Strategic Procurement',
        "page_title": 'Strategic Procurement - AFRILOTT',
        "paragraphs": [
            'AFRILOTT delivers end-to-end strategic procurement solutions designed to optimise sourcing, reduce costs, and strengthen supply chains across industries. We connect businesses with reliable suppliers and negotiate the best possible terms on their behalf.',
            'Our procurement specialists leverage deep market knowledge and a wide network of vetted vendors to ensure timely delivery of goods and services. From tender management to contract negotiations, we handle every stage of the procurement cycle with precision and transparency.',
            "With a focus on value creation and risk mitigation, AFRILOTT's strategic procurement services empower organisations to achieve operational excellence, maintain compliance, and build resilient supply partnerships that drive long-term growth.",
        ],
        "stats": [
            {
                "value": '200+',
                "label": 'Vetted Suppliers',
            },
            {
                "value": '15+',
                "label": 'Years Experience',
            },
            {
                "value": '100%',
                "label": 'Client Satisfaction',
            },
        ],
        "main_image": {
            "src": 'images/aflt-2.jpg',
            "alt": 'Strategic Procurement',
        },
        "small_image": {
            "src": 'images/laptop.jpg',
            "alt": 'Procurement Planning',
        },
    },
    ('procurement-supply-chain', 'woodworking-equipment-tools'): {
        "title": 'Woodworking Equipment & Tools',
        "page_title": 'Woodworking Equipment & Tools - AFRILOTT',
        "paragraphs": [
            'We offer wide range of Professional & Semi-Professional high-quality Woodworking Machinery, Industrial Equipment, and tools to meet the diverse needs of the woodworking industry.',
            'With years of experience and a commitment to excellence, we have established ourselves as a trusted provider of reliable and efficient machinery.',
            'AFRILOTT has been serving solid wood, MDF, chipboard, plastic, composites, light alloys, and non-ferrous metals manufacturers across the African Continent.',
        ],
        "stats": [
            {
                "value": '15+',
                "label": 'Years Experience',
            },
            {
                "value": '250+',
                "label": 'Machinery Supplied',
            },
            {
                "value": '100%',
                "label": 'Expert Support',
            },
        ],
        "main_image": {
            "src": 'https://images.unsplash.com/photo-1530124566582-a618bc2615dc?auto=format&fit=crop&w=1200&q=80',
            "alt": 'Woodworking machinery',
        },
        "small_image": {
            "src": 'https://media.istockphoto.com/id/1286896059/photo/electric-planer-and-electric-sheet-finishing-sander-on-old-rusty-metal-sheet-on-background.jpg?s=2048x2048&w=is&k=20&c=fyKsIWMUN-X6IW6ip-7T4m7lvoTaRpE9IBaceyjV3Yc=',
            "alt": 'Professional woodworking tools',
        },
    },
}


def get_category_page(category_slug: str) -> dict | None:
    """Return category page content dict or None if slug is unknown."""
    return CATEGORY_PAGES.get(category_slug)


def get_service_detail(category_slug: str, service_slug: str) -> dict | None:
    """Return service detail content dict or None if slug pair is unknown."""
    return SERVICE_DETAILS.get((category_slug, service_slug))


def is_valid_category(category_slug: str) -> bool:
    """Return True if category_slug is a known service category."""
    return category_slug in VALID_CATEGORY_SLUGS


def is_valid_service(category_slug: str, service_slug: str) -> bool:
    """Return True if the category/service slug pair is known."""
    return (
        category_slug in VALID_SERVICE_SLUGS
        and service_slug in VALID_SERVICE_SLUGS[category_slug]
    )
