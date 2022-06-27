from ovh_api.PymongoDB.pymongodb.utils import *

def test_check_type():
    int_ = 1
    str_ = 'a'
    list_str_ = ['a']
    list_int_ = [1]
    tuple_int_ = (1,)

    assert check_type(int_, 'int')
    assert not check_type(str_, 'int')
    assert check_type(list_int_, 'List[int]')
    assert not check_type(list_str_, 'List[int]')
    assert check_type(list_int_, 'List[Any]')
    assert check_type(tuple_int_, 'Tuple[int]')

