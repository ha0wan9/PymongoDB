from ..pymongodb import DefaultCol, mongodb_settings
from pydantic import BaseModel

__all__ = ["aliment_cat_table"]


class AlimentCatModel(BaseModel):

    aliment_cat_id: int
    aliment_cat_name: str
    cat_eMin: float
    cat_eMoy: float
    cat_volumic_mass: float


class AlimentCatCol(DefaultCol[AlimentCatModel]):

    class Meta:
        database_name = mongodb_settings.db
        collection_name = mongodb_settings.col['aliment_cat']['name']
        primary_key = mongodb_settings.col['aliment_cat']['primary key']


aliment_cat_table = AlimentCatCol()
