from ..pymongodb import DefaultCol, mongodb_settings
from pydantic import BaseModel

__all__ = ["sample_table"]


class SampleModel(BaseModel):

    sample_id: str
    aliment_id: int
    from_isahit: bool
    from_supervisely: bool
    image_ref: str
    mask_ref: str
    observed_thick: float
    restaurant_name: str
    surface: float
    volume: float


class SampleCol(DefaultCol[SampleModel]):

    class Meta:
        database_name = mongodb_settings.db
        collection_name = mongodb_settings.col['sample']['name']
        primary_key = mongodb_settings.col['sample']['primary key']


sample_table = SampleCol()
