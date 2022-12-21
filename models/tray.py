from ovh_api.PymongoDB.pymongodb import DefaultCol, AbstractModel
from ovh_api.PymongoDB.configs import AWSConfig, OVHConfig
from typing import Union, Optional
from datetime import datetime

__all__ = ["tray_table_aws", "tray_table_ovh"]


class TrayModel(AbstractModel):

    image_ref: str = 'image_ref'.upper()
    created_at: Union[datetime, str] = datetime(1970, 1, 1, 0, 0, 0)
    mask_ref: Optional[str] = 'mask_ref'.upper()
    pfm_ref: Optional[str] = 'pfm_ref'.upper()
    restaurant_name: Optional[str] = 'restaurant_name'.upper()
    status: Optional[str] = 'status'.upper()


class TrayColAWS(DefaultCol[TrayModel]):

    class Meta:
        mongodb_settings = AWSConfig()
        identifier = mongodb_settings.URI
        database_name = mongodb_settings.DB
        collection_name = mongodb_settings.COL['tray']['name']
        primary_key = mongodb_settings.COL['tray']['primary key']


class TrayColOVH(DefaultCol[TrayModel]):

    class Meta:
        mongodb_settings = OVHConfig()
        identifier = mongodb_settings.URI
        database_name = mongodb_settings.DB
        collection_name = mongodb_settings.COL['tray']['name']
        primary_key = mongodb_settings.COL['tray']['primary key']


tray_table_aws = TrayColAWS(TrayModel)
tray_table_ovh = TrayColOVH(TrayModel)