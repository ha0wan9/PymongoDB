# MongoClient('mongodb://username:password@hostnameOrReplicaset/?tls=True') replica by your own Service URI
from pydantic import BaseSettings
from typing import Dict

__all__ = 'mongodb_settings'


class MongoDBSettings(BaseSettings):

      uri: str = "mongodb://haoran:r2SRX3l8KQap7TzJPx6s" \
                  "@node1-581706eeb81da997.database.cloud.ovh.net/" \
                  "admin?replicaSet=replicaset&tls=true"
      db: str = "admin"
      col: Dict[str, str] = {
            'aliment': 'aliment',
            'sample': 'sample',
            'tray': 'tray',
            'test': 'test'
      }

      class Config(BaseSettings.Config):
            env_prefix = 'MONGO_'


mongodb_settings = MongoDBSettings()
