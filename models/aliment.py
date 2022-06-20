from pymongodb.model import ColModel
from pymongodb.config import mongodb_settings
from pydantic import BaseModel


class Aliment(ColModel):

    class Data(BaseModel):
        id: int
        aliment_cat_id: int
        aliment_cat_name: str
        aliment_name: str
        cat_eMin: float
        cat_eMoy: float
        cat_volumic_mass: float
        eMin: int
        eMoy: int
        volumic_mass: float


    def __init__(self):
        super(Aliment, self).__init__(database_name= mongodb_settings.db,
                                      collection_name=mongodb_settings.col['aliment'],
                                      data_model=)
        self.primary_key = 'id'


if __name__ == '__main__':
    aliment_table = Aliment().data()
