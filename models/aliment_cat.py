from ovh_api.PymongoDB.pymongodb import DefaultCol, AbstractModel
from ovh_api.PymongoDB.configs import AWSConfig, OVHConfig

__all__ = ["aliment_cat_table_aws", "aliment_cat_table_ovh"]


class AlimentCatModel(AbstractModel):

    aliment_cat_id: int = 0
    aliment_cat_name: str = 'aliment_cat_name'.upper()
    cat_eMin: float = 0.0
    cat_eMoy: float = 0.0
    cat_volumic_mass: float = 0.0


class AlimentCatColAWS(DefaultCol[AlimentCatModel]):

    class Meta:
        mongodb_settings = AWSConfig()
        identifier = mongodb_settings.URI
        database_name = mongodb_settings.DB
        collection_name = mongodb_settings.COL['aliment_cat']['name']
        primary_key = mongodb_settings.COL['aliment_cat']['primary key']


class AlimentCatColOVH(DefaultCol[AlimentCatModel]):

    class Meta:
        mongodb_settings = OVHConfig()
        identifier = mongodb_settings.URI
        database_name = mongodb_settings.DB
        collection_name = mongodb_settings.COL['aliment_cat']['name']
        primary_key = mongodb_settings.COL['aliment_cat']['primary key']

aliment_cat_table_aws = AlimentCatColAWS(AlimentCatModel)
aliment_cat_table_ovh = AlimentCatColOVH(AlimentCatModel)