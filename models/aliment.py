from ..pymongodb import DefaultCol, mongodb_settings
from pydantic import BaseModel

__all__ = ["aliment_table"]


class AlimentModel(BaseModel):

    aliment_id: int
    aliment_cat_id: int
    aliment_cat_name: str
    aliment_name: str
    cat_eMin: float
    cat_eMoy: float
    cat_volumic_mass: float
    eMin: int
    eMoy: int
    volumic_mass: float


class AlimentCol(DefaultCol[AlimentModel]):

    class Meta:
        database_name = mongodb_settings.db
        collection_name = mongodb_settings.col['aliment']['name']
        primary_key = mongodb_settings.col['aliment']['primary key']


aliment_table = AlimentCol()
