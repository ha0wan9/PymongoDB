from pydantic import BaseModel
from ovh_api.mongodb import MongoDB


class Model(MongoDB, BaseModel):
    pass



class Aliment(MongoDB, BaseModel):

    def __init__(self):
        BaseModel.__init__()
        MongoDB.__init__(self, database_name='admin', collection_name='aliment')
        self.primary_key = 'id'

if __name__ == '__main__':
    aliment = Model()
    aliment.__mro__()
