from pydantic import BaseModel
from ovh_api.mongodb import MongoDB


class Model(MongoDB):
    class Data(BaseModel):
        pass
    pass


class Aliment(Model):

    def __init__(self):
        super(Aliment, self).__init__(database_name='admin', collection_name='aliment')
        self.primary_key = 'id'
        self.data = self.Data()

if __name__ == '__main__':
    aliment = Aliment()
    print(aliment.data.dict())







