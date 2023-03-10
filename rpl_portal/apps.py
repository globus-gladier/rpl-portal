import os
from django.apps import AppConfig

from rpl_portal import fields

APP_DIR = os.path.join(os.path.dirname(__file__))


class RPLIndexConfig(AppConfig):
    name = "rpl_portal"


SEARCH_INDEXES = {
    "rpl": {
        "uuid": "aefcecc6-e554-4f8c-a25b-147f23091944",
        "name": "RPL Index",
        "group": "f08083f3-db94-11ec-9616-51db4d10f5bd",
        "collection": "bb8d048a-2cad-4029-a9c7-671ec5d1f84d",
        "base_templates": "globus-portal-framework/v2/",
        "template_override_dir": "rpl",
        "tabbed_project": False,
        "access": "private",
        "description": ("RPL portal"),
        "fields": [
            ("title", fields.title),
            "dc",
            "files",
            ("final_plates",fields.final_plates),
            ("all_files",fields.all_files),
            ("result", fields.results)
        ],
        "facets": [
            {
                "name": "Creator",
                "field_name": "dc.creators.creatorName",
            },
            {
                "name": "Dates",
                "field_name": "dc.dates.date",
                "type": "date_histogram",
                "date_interval": "day",
            },
            
        ],
        "facet_modifiers": [],
        "default_filters": [
            {
                "type": "match_all",
                "field_name": "project_metadata.project-slug",
                "values": ['reports'],
            }
        ]
        
    }
}
