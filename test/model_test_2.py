from ovh_api.PymongoDB.pymongodb import DefaultCol, mongodb_settings
from pydantic import BaseModel

class TestModel(BaseModel):
    id: int
    value: str

class TestCol(DefaultCol[TestModel]):

    class Meta:
        database_name = mongodb_settings.db
        collection_name = mongodb_settings.col['test']['name']
        primary_key = mongodb_settings.col['test']['primary key']

def test1():
    test = TestCol()
    print(test.list_all_elements())

    data = TestModel()
    data.id = 1
    data.value = 'x'

    #data = test.get(1)
    #data.value = 's'
    test.save(data)
    #test.delete(data)
    print(test.list_all_elements())

