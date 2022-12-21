from ovh_api.PymongoDB.pymongodb import DefaultCol, AbstractModel
from ovh_api.PymongoDB.configs import AWSConfig, OVHConfig
from typing import Optional
from datetime import datetime

__all__ = ["sample_table_aws", "sample_table_ovh"]


class SampleModel(AbstractModel):

    sample_id: str = 'sample_id'.upper()
    aliment_id: int = 0
    created_at: datetime = datetime(1970, 1, 1, 0, 0, 0)
    from_isahit: Optional[bool]
    from_supervisely: Optional[bool]
    image_ref: str = 'image_ref'.upper()
    mask_ref: Optional[str]
    observed_thick: Optional[float]
    restaurant_name: str = 'restaurant_name'.upper()
    surface: Optional[float]
    volume: Optional[float]
    volume_moy: Optional[float]


class SampleColAWS(DefaultCol[SampleModel]):

    class Meta:
        mongodb_settings = AWSConfig()
        identifier = mongodb_settings.URI
        database_name = mongodb_settings.DB
        collection_name = mongodb_settings.COL['sample']['name']
        primary_key = mongodb_settings.COL['sample']['primary key']


class SampleColOVH(DefaultCol[SampleModel]):

    class Meta:
        mongodb_settings = OVHConfig()
        identifier = mongodb_settings.URI
        database_name = mongodb_settings.DB
        collection_name = mongodb_settings.COL['sample']['name']
        primary_key = mongodb_settings.COL['sample']['primary key']


sample_table_aws = SampleColAWS(SampleModel)
sample_table_ovh = SampleColOVH(SampleModel)