from abc import ABC, abstractmethod
# https://stackoverflow.com/questions/54020772/get-the-type-of-the-super-class-in-python-3 ANSWER 2
import inspect

class Computer:
    pass

class UIControl(ABC):
    def __init__(self):
        """
        Enables UIControl
        """
        print(type(self).__name__)

    def __eq__(self, other):
        if isinstance(other, __class__):
            return NotImplemented
        return True

    def equal(self, other):
        if isinstance(other, __class__):
            print(True)
            return
        print(False)


    @abstractmethod
    def draw(self):
        """
        docstring
        """
        raise NotImplementedError

class TextBox(UIControl):
    def draw(self):
        print('Draw textbox')

    def mytree(self):
        print(inspect.getclasstree([self.__class__]))


class CheckBox(UIControl):
    def draw(self):
        print('Draw checkbox')


class AudioFile():
    def __init__(self, filename):
        if not filename.endswith(self.ext):
            raise Exception('Invalid format')
        self.filename = filename


class MP3File(AudioFile):
    ext = 'mp3'

    def play(self):
        print(f'playing {self.filename} as mp3')