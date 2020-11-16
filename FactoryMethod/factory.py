from abc import ABC, abstractmethod
import random


def animals_counter(animals_list):
    animal_types = {}
    for animal in animals_list:
        animal_type_name = animal.__class__.__name__
        if not animal_type_name in animal_types.keys():
            animal_types[animal_type_name] = 1
        else:
            animal_types[animal_type_name] += 1
    return animal_types


class IAnimalFactory(ABC):
    """
    Animal factory INTERFACE
    """
    def order_animal(self, animals_list):
        animal = self.create_animal(animals_list)
        # animals_list.append(animal)
        if animals_list:
            print(self.__class__.__name__)
            print(animals_counter(animals_list))
            animal.make_noise()
        return animal
    @abstractmethod
    def create_animal(animals_list):
        pass


class IAnimal(ABC):
    """
    Animal INTERFACE
    """
    @abstractmethod
    def make_noise():
        pass

class BalancedFactory(IAnimalFactory):
    """
    Concrete animal factory, creating balanced animals
    """
    def create_animal(self, animals_list):
        animal_types = animals_counter(animals_list)
        animal_classes = IAnimal.__subclasses__()
        animal_classes_dict = {}

        for animal in animal_classes:
            animal_classes_dict[animal.__name__] = animal

        animals_count = list(animal_types.values())

        if animals_count:
            max_count = animals_count.index(max(animals_count))
            max_indices = [i for i, x in enumerate(animals_count) if x == animals_count[max_count]]

            if len(max_indices) != len(animal_classes_dict):
                for max_index in max_indices:
                    key = list(animal_types.keys())[max_index]
                    del animal_classes_dict[key]

        random_index = random.randint(0, len(animal_classes_dict) - 1)
        animal = list(animal_classes_dict.values())[random_index]()
        return animal


class RandomFactory(IAnimalFactory):
    """
    Concrete animal factory, creating balanced animals
    """
    def create_animal(self, _):
        animal_classes = IAnimal.__subclasses__()
        random_index = random.randint(0, len(animal_classes) - 1)
        animal = animal_classes[random_index]()
        return animal



class Dog(IAnimal):
    """
    Concrete dog
    """
    @staticmethod
    def make_noise():
        print('Wooof Wooof')


class Cat(IAnimal):
    """
    Concrete cat
    """
    @staticmethod
    def make_noise():
        print('Miau Miau')


class Duck(IAnimal):
    """
    Concrete duck
    """
    @staticmethod
    def make_noise():
        print('Quack Quack')


# class Crocodile(IAnimal):
#     """
#     Concrete duck
#     """
#     @staticmethod
#     def make_noise(self):
#         print('Nhoc Nhoc')


def main():
    balanced_animals_list = []
    balanced_factory = BalancedFactory()
    random_animals_list = []
    random_factory = RandomFactory()

    start = 0
    for i in range(1, 2000):
        animal = balanced_factory.order_animal(balanced_animals_list)
        balanced_animals_list.append(animal)

        animal = random_factory.order_animal(random_animals_list)
        random_animals_list.append(animal)
        print()


        # if i % len(IAnimal.__subclasses__()) == 0:
        #     print(balanced_animals_list[start:i])
        #     start = i

    # print(animals_list)
    print()
    print('Balanced Factory')
    print(animals_counter(balanced_animals_list))
    print()
    print('Random Factory')
    print(animals_counter(random_animals_list))

main()