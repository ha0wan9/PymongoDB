from ..pymongodb import DefaultCol, mongodb_settings, AbstractModel

__all__ = ["aliment_cat_table"]


class AlimentCatModel(AbstractModel):

    aliment_cat_id: int # primary_key
    aliment_cat_name: str = 'aliment_cat_name'.upper()
    cat_eMin: float = 0.0
    cat_eMoy: float = 0.0
    cat_volumic_mass: float = 0.0



class AlimentCatCol(DefaultCol[AlimentCatModel]):

    class Meta:
        database_name = mongodb_settings.db
        collection_name = mongodb_settings.col['aliment_cat']['name']
        primary_key = mongodb_settings.col['aliment_cat']['primary key']

    def create(self, key_value: int):
        return AlimentCatModel.__setattr__(self.Meta.primary_key, key_value)


aliment_cat_table = AlimentCatCol(AlimentCatModel)
