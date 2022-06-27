from .mongodb import MongoDB
from .config import mongodb_settings
from .errors import *
from .utils import check_type
from typing import List, Type, TypeVar, Generic, overload
from pydantic import BaseModel


_T = TypeVar('_T', bound=BaseModel)
_OT = TypeVar('_OT', bound=BaseModel)

class AbstractCol(MongoDB, Generic[_T]):

    class Meta:
        database_name: str
        collection_name: str
        primary_key: str

    def __init__(self):
        super().__init__(database_name=self.Meta.database_name,
                         collection_name=self.Meta.collection_name)
        self.__document_class = self.__orig_bases__[0].__args__[0]
        self.primary_key = None
        self.__validate()

    def __validate(self):
        assert issubclass(self.__document_class, BaseModel), '[MongoDB]: Document class should inherit BaseModel'
        try:
            if self.Meta.primary_key not in self.__document_class.__fields__:
                raise KeyNotFoundError(f'[MongoDB]: Primary key {self.Meta.primary_key} not found in collection.')
            self.primary_key = self.Meta.primary_key
        except NameError:
            raise KeyNotDefinedError(f'[MongoDB]: Primary key not defined in class Meta.')
            # if 'id' not in self.__document_class.__fields__:
            #     raise KeyNotFoundError('[MongoDB]: Document class without primary key should have id field.')
            # self.primary_key = 'id'

    def list_classes(self):
        return list(self.__document_class.__fields__)

    def doc(self):
        return self.__document_class


class DefaultCol(AbstractCol[_T]):

    class Meta:
        database_name: str
        collection_name: str
        primary_key: str

    def __init__(self):
        super().__init__()
        self.__document_class = self.__orig_bases__[0].__args__[0]
        self.create_index(self.primary_key, unique=True)

    # Built in test collection
    @classmethod
    def test_col(cls) -> _OT:
        cls.Meta.database_name = mongodb_settings.db
        cls.Meta.collection_name = mongodb_settings.col['test']['name']
        cls.Meta.primary_key = mongodb_settings.col['test']['primary key']

        class TestModel(BaseModel):
            id: int
            value: str

        return cls[TestModel]

    @staticmethod
    def to_model_custom(output_type: Type[_OT], data: dict) -> _OT:
        if '_id' in data.keys():
            data.pop('_id')
        return output_type.parse_obj(data)

    def to_model(self, data: [dict, List[dict]]) -> _T:
        if check_type(data, 'List_dict'):
            return [self.to_model(data_point) for data_point in data]
        return self.to_model_custom(self.__document_class, data)

    def get(self, key_value, key: str = None, one: bool = False):
        if not key:
            key = self.primary_key
            result = self.query(key, key_value, one=True)
        else:
            result = self.query(key, key_value, one=one)
        if not result:
            raise DataNotFoundError(f'[MongoDB] Data with {key} = {key_value} doesnt exist.')
        if isinstance(result, dict):
            return self.to_model(result)
        return [self.to_model(res) for res in result]

    def save(self, model: _T):
        # Convert input data to document
        document = dict(model)
        if '_id' in document.keys():
            document.pop('_id')
        result = self.update({self.primary_key: document[self.primary_key]},
                             document, upsert=True)
        return result

    def delete(self, query: _T, with_regex: bool = False):
        return super().delete(dict(query), with_regex=with_regex)




class DefaultIdCol(AbstractCol[_T]):

    class Meta:
        database_name: str
        collection_name: str
        primary_key: str

    def __init__(self):
        super().__init__()

    # Built in test collection
    @classmethod
    def test_col(cls) -> _OT:
        cls.Meta.database_name = mongodb_settings.db
        cls.Meta.collection_name = mongodb_settings.col['test']

        class TestModel(BaseModel):
            id: int
            value: str

        return cls[TestModel]

    @staticmethod
    def to_dict(model: _T) -> dict:
        result = model.dict()
        result.pop('id')
        if model.id:
            result['_id'] = model.id
        return result

    @staticmethod
    def to_model_custom(output_type: Type[_OT], data: dict) -> _OT:
        data_copy = data.copy()
        if '_id' in data_copy:
            data_copy['id'] = data_copy.pop('_id')
        return output_type.parse_obj(data_copy)

    def to_model(self, data: dict) -> _T:
        return self.to_model_custom(self.__document_class, data)

    def save(self, model: _T):
        # Convert input data to document
        document = self.to_dict(model)

        # if model id exists, update the data point
        if model.id:
            mongo_id = document.pop('_id')
            self.update({'_id': mongo_id}, document)
            return

        # result = self.insert(document)
        # model.id = result.inserted_id
        # return result
        raise KeyNotFoundError(f'[MongoDB]: field id of {_T.__name__} not found')





























