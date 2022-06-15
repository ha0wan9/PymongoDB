from pydantic import BaseModel
from ovh_api.mongodb.models.config import *
from ..mongodb import MongoDB

model = {
    'aliment_id': int,
}


class Aliment(MongoDB):

    def __init__(self):
        super().__init__(database_name=MAIN_DATABASE,
                         collection_name="aliment")
        self.model = model

    def get_model(self):
        return self.model



if __name__ == '__main__':
    aliment_table = Aliment().list_all()
