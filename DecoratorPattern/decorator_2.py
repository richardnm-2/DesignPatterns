from abc import ABC, abstractmethod

"""
Padrão ideal para quando cada implementação concreta do decorador possui uma FORMA DIFERENTE de cálculo/retorno.
Nesse caso, a única coisa que varia de um decorador para outro são atributos, o que seria melhor e mais fácil a implementação da simples adição dos custos de cada objeto, colocando-os numa lista, à medida que o pedido entra.

https://www.youtube.com/watch?v=GCraGHx6gso&list=PLrhzvIcii6GNjpARdnO4ueTUAVR9eMBpc&index=3
"""


class Beverage(ABC):
    """
    Abstract Beverage
    """
    @abstractmethod
    def get_description():
        pass

    @abstractmethod
    def get_cost():
        pass


class AddonDecorator(Beverage):
    """
    Abstract flavor addon
    """

    @abstractmethod
    def get_description():
        pass

    @abstractmethod
    def get_cost():
        pass


class Decaf(Beverage):
    """
    Concrete beverage
    """

    description = 'Decaf coffee'
    cost = 2

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost


class Expresso(Beverage):
    """
    Concrete beverage
    """

    description = 'Expresso coffee'
    cost = 1

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost


class DecoratorBase(AddonDecorator):
    """
    Addon decorator base, implementing common functions and atrributes to the concrete addons
    """

    beverage = None

    def __init__(self, beverage=None):
        self.beverage = beverage

    def __call__(self, bevarage):
        self.beverage = bevarage
        return self

    def get_description(self):
        return self.description + self.beverage.description

    def get_cost(self):
        cost = self.cost + self.beverage.get_cost()
        return cost


class CaramelDecorator(DecoratorBase):
    """
    Concrete addon
    """
    description = 'Caramel addon'
    cost = 2


class SoyDecorator(DecoratorBase):
    """
    Concrete addon
    """
    description = 'Soy addon'
    cost = 1


def main():
    """
    Só um teste, usando __call__ para poder criar instâncias "vazias" dos decoradores, apesar de não fazer sentido eles existirem por si só.
    """
    expresso = Expresso()
    caramel = CaramelDecorator()

    beverage = caramel(expresso)
    # caramel = CaramelDecorator()
    beverage = caramel(beverage)
    beverage_cost = beverage.get_cost()
    print('Beverage cost: $' + str(beverage_cost) )

    beverage = CaramelDecorator(expresso)
    beverage = CaramelDecorator(beverage)
    # beverage = SoyDecorator(beverage)
    # beverage = SoyDecorator(beverage)
    # beverage = CaramelDecorator(beverage)
    beverage_cost = beverage.get_cost()

    print()
    print('Beverage cost: $' + str(beverage_cost) )

main()