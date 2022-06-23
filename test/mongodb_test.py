import pytest
from ovh_api.PymongoDB.pymongodb import MongoDB, mongodb_settings

#@pytest.mark.skip
def test_connection():

    test_col = MongoDB(database_name=mongodb_settings.db,
                      collection_name=mongodb_settings.col['test'])

    test_col.delete(test_col.list_all_elements())
    print(test_col.list_all_elements())

