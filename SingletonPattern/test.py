class BaseClass:
    """
    docstring
    """
    base_test = 'base_test'

class Singleton(object):
    _instance = None
    _instance2 = None
    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
        class_._instance2 = object.__new__(class_, *args, **kwargs)
        return class_._instance

class MyClass(BaseClass, Singleton):
    test = 'test'


singleton = MyClass()
singleton2 = MyClass()
singleton.test = 0
print(singleton2.test)