class PymongoDBError(Exception):
    pass


class TypeValidationError(PymongoDBError):
    pass


class KeyNotFoundError(PymongoDBError):
    pass

class KeyNotDefinedError(PymongoDBError):
    pass

class DataNotFoundError(PymongoDBError):
    pass