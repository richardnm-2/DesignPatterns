from abc import ABC, abstractmethod
import random


class NoCommand:
    """
    Concrete command, implementing ICommand
    """
    def execute(self):
        pass

    def unexecute(self):
        pass

class OnOffInvoker:
    """
    Comand invoker (remote control). Concrete class, that could be underneath a Parent Class
    """
    on = None
    off = None
    up = None
    down = None
    error_func = None
    undo_command = [NoCommand()]

    def __init__(self, on, off, up, down, error_func):
        self.on = on
        self.off = off
        self.up = up
        self.down = down
        self.error_func = error_func

    def click_on(self):
        self.on.execute()
        self.undo_command.append(self.on)

    def click_off(self):
        self.off.execute()
        self.undo_command.append(self.on)

    def click_up(self):
        self.up.execute()
        self.undo_command.append(self.on)

    def click_down(self):
        self.down.execute()
        self.undo_command.append(self.on)

    def click_error(self):
        self.error_func.execute()

    def click_undo(self):
        self.undo_command.unexecute()

class ColorInvoker:
    """
    Comand invoker (remote control). Concrete class, that could be underneath a Parent Class
    """
    change = None
    undo_command = [NoCommand()]
    def __init__(self, change):
        self.change = change

    def click_change(self):
        self.change.execute()
        self.undo_command.append(self.click_change)

    def click_unchange(self):
        self.change.unexecute()


class ICommand(ABC):
    """
    Command INTERFACE
    """
    @abstractmethod
    def execute():
        pass

    @abstractmethod
    def unexecute():
        pass

class LightOnCommand:
    """
    Concrete command, implementing ICommand
    """
    light = None

    def __init__(self, light):
        assert isinstance(light, OnOffLight)
        self.light = light

    def execute(self):
        self.light.on()

    def unexecute(self):
        self.light.off()

class LightOffCommand:
    """
    Concrete command, implementing ICommand
    """
    light = None

    def __init__(self, light):
        assert isinstance(light, OnOffLight)
        self.light = light

    def execute(self):
        self.light.off()

    def unexecute(self):
        self.light.on()

class LightUpCommand:
    """
    Concrete command, implementing ICommand
    """
    light = None

    def __init__(self, light):
        assert isinstance(light, OnOffLight)
        self.light = light

    def execute(self):
        self.light.up()

    def unexecute(self):
        self.light.down()

class LightDownCommand:
    """
    Concrete command, implementing ICommand
    """
    light = None

    def __init__(self, light):
        assert isinstance(light, OnOffLight)
        self.light = light

    def execute(self):
        self.light.down()

    def unexecute(self):
        self.light.up()

class LightErrorCommand:
    """
    Concrete command, implementing ICommand. Criando essa classe "depois", extendendo a funcionalidade, porém com um erro (downn e upp não existem em OnOffLight)
    """
    light = None

    def __init__(self, light):
        assert isinstance(light, OnOffLight)
        self.light = light

    def execute(self):
        self.light.downn()

    def unexecute(self):
        self.light.upp()

class LightColorChangeCommand:
    """
    Concrete command, implementing ICommand
    """
    light = None

    def __init__(self, light):
        assert isinstance(light, LightColor)
        self.light = light

    def execute(self):
        self.light.change_color()

    def unexecute(self):
        self.light.unchange_color()

class OnOffLight:
    def on(self):
        print('light on!!!')

    def off(self):
        print('light off....')

    def up(self):
        print('light up!')

    def down(self):
        print('light down.')

class LightColor:
    colors = ['red', 'green', 'blue', 'pink', 'black', 'gray', 'yellow', 'magenta']
    color_idx = None
    prev_color_idx = [None]
    def change_color(self):
        _, self.color_idx = self.color_randomizer()
        color = self.colors[self.color_idx]
        print(f'{color.upper()} light')

    def unchange_color(self):
        prev_color = self.colors[self.prev_color_idx.pop()]
        print(f'{prev_color.upper()} light')

    def color_randomizer(self):
        idx = random.randint(0, len(self.colors) - 1)
        self.prev_color_idx.append(self.color_idx)
        return self.colors[idx], idx

light = OnOffLight()
invoker = OnOffInvoker(LightOnCommand(light),
                  LightOffCommand(light),
                  LightUpCommand(light),
                  LightDownCommand(light),
                  LightErrorCommand(light)
                  )
# invoker.click_on()
# invoker.click_undo()
# invoker.click_on()
# invoker.click_off()
# invoker.click_down()

color_invoker = ColorInvoker(LightColorChangeCommand(LightColor()))
color_invoker.click_change()
color_invoker.click_change()
color_invoker.click_change()
color_invoker.click_change()
print('Undoing...')
color_invoker.click_unchange()
color_invoker.click_unchange()