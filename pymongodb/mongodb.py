"""
A MongoDB interface for manipulating document data objects.
"""
import typing

from typing import List, overload, Any, Generic, TypeVar
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from pydantic import BaseSettings
from .errors import PymongoDBError, TypeValidationError
from .utils import check_type


class MongoDB:

    def __init__(self, database_name: str = None, collection_name: str = None,
                 identifier: str = None):
        # Establishing connection
        try:
            self.client = MongoClient(identifier)
            print("[MongoDB]: MongoDB cluster is reachable")
            print(self.client)
        except ConnectionFailure as e:
            print("[MongoDB]: Could not connect to MongoDB")
            print(e)
        self.dblist = self.client.list_database_names()
        self.database = None
        self.collist = None
        self.collection = None

        self.set_database(database_name)
        self.set_collection(collection_name)

    def set_database(self, name: str):
        if name not in self.dblist and not None:
            self.database = self.client[name]
            print(f'[MongoDB]: Database {name} created.')
        else:
            self.database = self.client[name]
            # print(f'[MongoDB]: Database {name} exists.')

    def set_collection(self, name: str):
        if self.database is not None:
            self.collist = self.database.list_collection_names()
            if name not in self.collist:
                self.collection = self.database[name]
                print(f'[MongoDB]: Collection {name} created in {self.database.name}.')
            else:
                self.collection = self.database[name]
                # print(f'[MongoDB]: Collection {name} exists.')
        else:
            print(f'[MongoDB]: No database selected, please set a database.')

    def create_index(self, keys: str, **kwargs) -> str:
        '''

        Args:
            keys: Union[str, Sequence[Tuple[str, Union[int, str, Mapping[str, Any]]]]]
                - single key in str or list of keys with [(key, direction(ASCENDING,
                  DESCENDING, GEO2D, GEOSPHERE, HASHED, TEXT))]
            **kwargs:
                - unique: bool = False, set key(s) as primary key or not.

        Returns:

        '''
        return self.collection.create_index(keys, **kwargs)

    def query(self, key_name: Any, query_value: str, one: bool = False, **kwargs):
        '''

        Args:
            key_name: key name to query
            key_value: key value to query
            one: query only

        Returns:
            if unique: a dictionary of query result
            not unique: an iterable which contains all found documents

        '''
        if one:
            return self.collection.find_one({key_name: query_value}, **kwargs)
        return self.collection.find({key_name: query_value}, **kwargs)

    def primary_query(self, key_value, one: bool = False):
        return self.query('_id', key_value, one=one)

    def list_all_elements(self):
        return list(self.collection.find({}))

    @overload
    def insert(self, data: List[dict], *args, **kwargs):
        ...

    @overload
    def insert(self, data: dict, *args, **kwargs):
        ...

    def insert(self, data: [dict, List[dict]], *args, **kwargs):
        if isinstance(data, dict):
            res = self.collection.insert_one(data, *args, **kwargs)
            print(f'[MongoDB]: Document inserted with id {res.inserted_id}.')
            return res
        elif isinstance(data, list):
            res = self.collection.insert_many(data, *args, **kwargs)
            print(f'[MongoDB]: {len(data)} documents inserted with ids {res.inserted_id}.')
            return res
        raise TypeValidationError(f'[MongoDB]: {type(data)} is not allowed.')

    def update(self, query: dict, new_value: dict, with_regex: bool = False, **kwargs):
        new_value = {"$set": new_value}
        if not with_regex:
            self.collection.update_one(query, new_value, **kwargs)
        else:
            res = self.collection.update_many(query, new_value, **kwargs)
            print(f'[MongoDB]: {res.modified_count} documents updated successfully.')

    @overload
    def delete(self, query: List[dict], with_regex: bool = False):
        ...

    @overload
    def delete(self, query: dict, with_regex: bool = False):
        ...

    def delete(self, query: [dict, List[dict]], with_regex: bool = False):
        if check_type(query, 'List[dict]'):
            if len(query) == 0:
                print(f"[MongoDB]: The query list is empty, nothing to delete.")
                return
            for q in query:
                self.delete(q, with_regex=with_regex)
            return
        elif isinstance(query, list) and len(query) == 0:
            print(f"[MongoDB]: The query list is empty, nothing to delete.")
            return
        elif isinstance(query, dict):
            if not with_regex:
                res = self.collection.delete_one(query)
                print(f"[MongoDB]: Document {query.keys()[0]} deleted successfully.")
            else:
                res = self.collection.delete_many(query)
                print(f'[MongoDB]: {res.deleted_count} documents deleted successfully.')
            return
        raise TypeValidationError(f'[MongoDB]: {type(query)} is not allowed.')
