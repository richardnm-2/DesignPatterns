

class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instance = {}

    def __new__(class_, *args, **kwargs):
        class_._instance = object.__new__(class_, *args, **kwargs)
        return class_


    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

# class Singleton(metaclass=SingletonMeta):

class BaseClass:
    """
    docstring
    """
    base_test = 'base_test'


class Singleton:
    """
    Singleton class
    """
    foo = 'foo'

    def __new__(cls, *args, **kwargs):
        """
        Dessa forma, nenhuma instância é criada, apenas repassada a classe para a variável
        """
        # cls._instance = object.__new__(cls, *args, **kwargs)
        return cls

    def __init__(self):
        self = object
        return self

class SubSingleton(BaseClass):
    sub_test = 'sub_test'

    def __init__(self):
        pass

singleton = Singleton()
singleton2 = Singleton()
singleton.foo = 'bar'
singleton.bar = 'baz'
print(singleton is singleton2)
print(singleton2.foo)

sub_singleton = SubSingleton()
sub_singleton2 = SubSingleton()
sub_singleton.sub_test = 0
print(sub_singleton2.sub_test)
