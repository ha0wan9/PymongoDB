from ..config import *
from ..mongodb import MongoDB


class Aliment(MongoDB):

    def __init__(self):
        super().__init__(database_name=MAIN_DATABASE,
                         collection_name="aliment")


if __name__ == '__main__':
    aliment_table = Aliment().list_all()
