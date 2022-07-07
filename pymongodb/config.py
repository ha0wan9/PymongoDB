# MongoClient('mongodb://username:password@hostnameOrReplicaset/?tls=True') replica by your own Service URI
from pydantic import BaseSettings
from typing import Dict

__all__ = 'mongodb_settings'


class MongoDBSettings(BaseSettings):

      uri: str
      db: str = "admin"
      col: Dict[str, Dict[str, str]] = {
            'aliment': {'name': 'aliment', 'primary key': 'aliment_id'},
            'aliment_cat': {'name': 'aliment_cat', 'primary key': 'aliment_cat_id'},
            'sample': {'name': 'sample', 'primary key': 'sample_id'},
            'tray': {'name': 'tray', 'primary key': 'image_ref'},
            'test': {'name': 'test', 'primary key': 'id'},
      }

      class Config(BaseSettings.Config):
            env_prefix = 'MONGO_'


mongodb_settings = MongoDBSettings()
