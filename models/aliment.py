from ovh_api.PymongoDB.pymongodb import DefaultCol, AbstractModel
from ovh_api.PymongoDB.configs import AWSConfig, OVHConfig

__all__ = ["aliment_table_aws", "aliment_table_ovh"]


class AlimentModel(AbstractModel):

    aliment_id: int = 0
    aliment_cat_id: int = 0
    aliment_cat_name: str = 'aliment_cat_name'.upper()
    aliment_name: str = 'aliment_name'.upper()
    cat_eMin: float = 0.0
    cat_eMoy: float = 0.0
    cat_volumic_mass: float = 0.0
    eMin: int = 0
    eMoy: int = 0
    volumic_mass: float = 0.0


class AlimentColAWS(DefaultCol[AlimentModel]):

    class Meta:
        mongodb_settings = AWSConfig()
        identifier = mongodb_settings.URI
        database_name = mongodb_settings.DB
        collection_name = mongodb_settings.COL['aliment']['name']
        primary_key = mongodb_settings.COL['aliment']['primary key']


class AlimentColOVH(DefaultCol[AlimentModel]):

    class Meta:
        mongodb_settings = OVHConfig()
        identifier = mongodb_settings.URI
        database_name = mongodb_settings.DB
        collection_name = mongodb_settings.COL['aliment']['name']
        primary_key = mongodb_settings.COL['aliment']['primary key']



aliment_table_aws = AlimentColAWS(AlimentModel)
aliment_table_ovh = AlimentColOVH(AlimentModel)
