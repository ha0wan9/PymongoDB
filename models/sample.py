from ..pymongodb import DefaultCol, mongodb_settings, AbstractModel
from typing import Optional
from pydantic import BaseModel

__all__ = ["sample_table"]


class SampleModel(AbstractModel):

    sample_id: str
    aliment_id: int
    from_isahit: Optional[bool]
    from_supervisely: Optional[bool]
    image_ref: str
    mask_ref: Optional[str]
    observed_thick: Optional[float]
    restaurant_name: str
    surface: Optional[float]
    volume: Optional[float]


class SampleCol(DefaultCol[SampleModel]):

    class Meta:
        database_name = mongodb_settings.db
        collection_name = mongodb_settings.col['sample']['name']
        primary_key = mongodb_settings.col['sample']['primary key']


sample_table = SampleCol(SampleModel)
