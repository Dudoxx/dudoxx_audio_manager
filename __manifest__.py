{
    "name": "Dudoxx Audio Manager",
    "version": "1.0.0",
    "author": "Walid Boudabbous",
    "website": "https://www.dudoxx.com",
    "category": "Tools",
    "summary": "Module for managing audio recordings and their transcriptions.",
    "description": "This module provides a comprehensive solution for managing a vast collection of vocal recordings, including transcriptions, translations, and updates.",
    "depends": ["base", "web"],
    "data": [
        "security/ir.model.access.csv",
        "views/dudoxx_audio_manager_views.xml",
        "data/data.xml"
    ],
    "assets": {
        "web.assets_backend": [
           
            "/dudoxx_audio_manager/static/src/js/audio_player_widget.js",
            "/dudoxx_audio_manager/static/src/xml/audio_player_widget_template.xml",
            "/dudoxx_audio_manager/static/src/css/dudoxx_audio_manager.css",
            "/dudoxx_audio_manager/static/src/css/audio_player_widget.css",
        ]
    },
    "installable": True,
    "application": True,
    "license": "LGPL-3"
}
