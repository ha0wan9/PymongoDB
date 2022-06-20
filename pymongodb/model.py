from pydantic import BaseModel
from pymongodb.mongodb import MongoDB


class ColModel(MongoDB):

    def __init__(self, database_name: str, collection_name: str, data_model: BaseModel):
        super(ColModel, self).__init__(database_name=database_name, collection_name=collection_name)
        self._data_model = data_model

    @property
    def data(self) -> BaseModel:
        return self._data_model











