

class ClassmethodProperty(property):
    """Realization merge two descriptors: @classmethod and @property (getter)

    A base taken from http://stackoverflow.com/questions/128573/using-property-on-classmethods
    """

    def __get__(self, obj, objtype):
        return self.fget.__get__(None, objtype)()


class staticmethod_(object):
    """Pure the Python implementation of decorator staticmethod."""

    def __init__(self, method):
        self.method = method

    def __get__(self, obj, objtype=None):
        return self.method


class classmethod_(object):
    """Pure the Python implementation of decorator classmethod."""

    def __init__(self, method):
        self.method = method

    def __get__(self, obj, objtype=None):

        objtype = type(obj) if objtype is None else objtype

        return lambda *args, **kwargs: self.method(objtype, *args, **kwargs)


class staticclassmethod(object):

    def __init__(self, method):
        self.method = method

    def __get__(self, obj, objtype=None):

        objtype = type(obj) if objtype is None else objtype

        def method(*args, **kwargs):
            return self.method(*args, **kwargs)

        return method


class classproperty(object):

    def __init__(self, method):
        self.method = method

    def __get__(self, obj, objtype=None):
        objtype = type(obj) if objtype is None else objtype
        return self.method(objtype)
