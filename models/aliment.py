from ..pymongodb import DefaultCol, mongodb_settings, AbstractModel
from pydantic import BaseModel

__all__ = ["aliment_table"]


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



class AlimentCol(DefaultCol[AlimentModel]):

    class Meta:
        database_name = mongodb_settings.db
        collection_name = mongodb_settings.col['aliment']['name']
        primary_key = mongodb_settings.col['aliment']['primary key']


aliment_table = AlimentCol(AlimentModel)
