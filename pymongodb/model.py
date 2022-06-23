from .mongodb import MongoDB
from .config import mongodb_settings
from typing import Type, TypeVar, Generic
from pydantic import BaseModel


_T = TypeVar('_T', bound=BaseModel)
_OT = TypeVar('_OT', bound=BaseModel)


class AbstractCol(MongoDB, Generic[_T]):

    class Meta:
        database_name: str
        collection_name: str

    def __init__(self):
        super().__init__(database_name=self.Meta.database_name,
                         collection_name=self.Meta.collection_name)
        self.__document_class = self.__orig_bases__[0].__args__[0]
        self.__validate()

    def __validate(self):
        assert issubclass(self.__document_class, BaseModel), '[MongoDB]: Document class should inherit BaseModel'
        assert 'id' in self.__document_class.__fields__, '[MongoDB]: Document class should have id field, which is your primary key.'

    def list_classes(self):
        return list(self.__document_class.__fields__)

    def doc(self):
        return self.__document_class

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

        result = self.insert(document)
        model.id = result.inserted_id
        return result





























