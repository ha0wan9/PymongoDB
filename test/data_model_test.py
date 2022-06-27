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


def test1():
    test = Test()
    test1 = {'_id': 3, 'a': 'A', 'b': 1}
    test1 = test.to_model(test1)
    test.save(test1)

    print(test.list_all_elements())

def test2():
    test = Test()
    test.delete(test.list_all_elements())

