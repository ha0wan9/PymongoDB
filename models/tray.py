from ..pymongodb import DefaultCol, mongodb_settings, AbstractModel
from typing import Union, Optional
from datetime import date

__all__ = ["tray_table"]


class TrayModel(AbstractModel):

    image_ref: str
    created_at: Union[date, str]
    mask_ref: Optional[str]
    pfm_ref: Optional[str]
    restaurant_name: str
    status: str


class TrayCol(DefaultCol[TrayModel]):

    class Meta:
        database_name = mongodb_settings.db
        collection_name = mongodb_settings.col['tray']['name']
        primary_key = mongodb_settings.col['tray']['primary key']


tray_table = TrayCol(TrayModel)
