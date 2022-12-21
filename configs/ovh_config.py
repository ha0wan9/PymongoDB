from ..pymongodb import MongoDBSettings
from typing import Dict
from define import get_mongo_uri

__all__ = ['OVHConfig']


class OVHConfig(MongoDBSettings):

    URI: str = get_mongo_uri(mongo_cloud='OVH')
    DB: str = "admin"
    COL: Dict[str, Dict[str, str]] = {
        'aliment': {'name': 'aliment', 'primary key': 'aliment_id'},
        'aliment_cat': {'name': 'aliment_cat', 'primary key': 'aliment_cat_id'},
        'sample': {'name': 'sample', 'primary key': 'sample_id'},
        'tray': {'name': 'tray', 'primary key': 'image_ref'},
        'TrayNonOrga': {'name': 'TrayNonOrga', 'primary key': 'id'},
        'test': {'name': 'test', 'primary key': 'id'},
    }
