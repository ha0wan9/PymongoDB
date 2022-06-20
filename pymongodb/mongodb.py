from pymongodb.config import mongodb_settings
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure


class MongoDB:

    def __init__(self, database_name: str = None, collection_name: str = None):
        # Establishing connection
        try:
            uri = mongodb_settings.uri
            self.client = MongoClient(uri)
            print("[MongoDB]: MongoDB cluster is reachable")
            print(self.client)
        except ConnectionFailure as e:
            print("[MongoDB]: Could not connect to MongoDB")
            print(e)
        self.dblist = self.client.list_database_names()
        self.database = None
        self.collist = None
        self.collection = None
        self.primary_key = None

        self.set_database(database_name)
        self.set_collection(collection_name)

    def set_database(self, name: str):
        if name not in self.dblist and not None:
            self.database = self.client[name]
            print(f'[MongoDB]: Database {name} created.')
        else:
            self.database = self.client[name]
            print(f'[MongoDB]: Database {name} exists.')

    def set_collection(self, name: str):
        if self.database is not None:
            self.collist = self.database.list_collection_names()
            if name not in self.collist:
                self.collection = self.database[name]
                print(f'[MongoDB]: Collection {name} created in {self.database}.')
            else:
                self.collection = self.database[name]
                print(f'[MongoDB]: Collection {name} exists.')
        else:
            print(f'[MongoDB]: No database selected, please set a database.')

    def set_primary_key(self, key_name: str):
        self.primary_key = key_name

    def query(self, key_name, key_value: str, unique: bool = False):
        '''

        Args:
            key_name: key name to query
            key_value: key value to query
            unique: query only

        Returns:
            if unique: a dictionary of query result
            not unique: an iterable which contains all found documents

        '''
        if unique:
            return self.collection.find_one({key_name: key_value})
        return self.collection.find({key_name: key_value})

    def primary_query(self, key_value, unique: bool = False):
        return self.query(self.primary_key, key_value, unique=unique)

    def list_all(self):
        return self.collection.find({})

    def insert(self, data: [dict, list]):
        if type(data) is dict:
            res = self.collection.insert_one(data)
            print(f'[MongoDB]: Document inserted with id {res.inserted_id}.')
        elif type(data) is list:
            res = self.collection.insert_many(data)
            print(f'[MongoDB]: {len(data)} documents inserted with ids {res.inserted_id}.')

    def update(self, query: dict, new_value: dict, batch: bool = False):
        new_value = {"$set": new_value}
        if not batch:
            self.collection.update_one(query, new_value)
            print(f'[MongoDB]: Document updated successfully.')
        else:
            res = self.collection.update_many(query, new_value)
            print(f'[MongoDB]: {res.modified_count} documents updated successfully.')

    def delete(self, query: dict, batch: bool = False):
        if not batch:
            self.collection.delete_one(query)
            print(f'[MongoDB]: Document deleted successfully.')
        else:
            res = self.collection.delete_many(query)
            print(f'[MongoDB]: {res.deleted_count} documents deleted successfully.')


if __name__ == "__main__":
    tray_table = MongoDB(database_name='AI_Backend', collection_name='TrayTable')
    # element = {"name": "John", "address": "Highway 37"}
    # tray_table.insert(element)
    data = tray_table.query('name', 'John', True)
    print(data)
    # new_value = {"address": "18 rue des Roseaux"}
    #$ tray_table.update(data, new_value)
    data['name'] = 'Mary'
    data['address'] = '8, Avenue des Champs Elysee'
    tray_table.insert(data)




