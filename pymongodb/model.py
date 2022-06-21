from typing import Type, TypeVar, Generic
from pydantic import BaseModel
from .mongodb import MongoDB


__all__ = "ColModel"

_M = TypeVar('_M', bound=BaseModel)
_OutputM = TypeVar('_OutputM', bound=BaseModel)

class AbstractCol(MongoDB, Generic[_M]):

    class Meta:
        database_name: str
        collection_name: str

    def __init__(self):
        super().__init__(database_name=self.Meta.database_name,
                         collection_name=self.Meta.collection_name)
        self.__document_class = self.__orig_bases__[0].__args__[0]


    def __validate(self):
        if not issubclass(self.__document_class, BaseModel):
            raise Exception('[MongoDB]: Document class should inherit BaseModel')
        if 'id' not in self.__document_class.__fields__:
            raise Exception('[MongoDB]: Document class should have id field')

    @staticmethod
    def to_dict(model: _M) -> dict:
        result = model.dict()
        result.pop('id')
        if model.id:
            result['_id'] = model.id
        return result

    def to_model_custom(self, output_type: Type[_OutputM], data: dict) -> _OutputM:
        data_copy = data.copy()
        if '_id' in data_copy:
            data_copy['id'] = data_copy.pop('_id')
        return output_type.parse_obj(data_copy)

    def to_model(self, data: dict) -> _M:
        return self.to_model_custom(self.__document_class, data)

    def save(self, model: _M):
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





























