from pydantic import BaseModel
from ovh_api.PymongoDB.pymongodb import AbstractCol
from ovh_api.PymongoDB.pymongodb import mongodb_settings


class TestModel(BaseModel):
    id: int
    a: str
    b: int


class Test(AbstractCol[TestModel]):

    class Meta:
        database_name = mongodb_settings.db
        collection_name = mongodb_settings.col['test']


test = Test()

