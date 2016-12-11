

class ClassmethodProperty(property):
    """Realization merge two descriptors: @classmethod and @property (getter)

    A base taken from http://stackoverflow.com/questions/128573/using-property-on-classmethods
    """

    def __get__(self, obj, objtype):
        return self.fget.__get__(None, objtype)()
