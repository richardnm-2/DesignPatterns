from abc import ABC, abstractmethod
import random


class IUIFactory(ABC):
    """
    UI factory INTERFACE
    """
    def order_widgets(self, *args, **kwargs):
        button = self.create_button(*args, **kwargs)
        alert = self.create_alert(*args, **kwargs)
        return button, alert

    @abstractmethod
    def create_button(*args, **kwargs):
        pass

    @abstractmethod
    def create_alert(*args, **kwargs):
        pass


class IUIWidget(ABC):
    """
    UI widget INTERFACE
    """
    @abstractmethod
    def print_os():
        pass

class WindowsFactory(IUIFactory):
    """
    Concrete UI factory, creating windows widgets
    """
    def create_button(self, *args, **kwargs):
        print(kwargs['teste'])
        a, *b, c = args[0]
        d = b
        buttons = []
        widget_classess = IUIWidget.__subclasses__()
        for widget_class in widget_classess:
            if widget_class.os == 'Windows' and widget_class.type == 'button':
                buttons.append(widget_class)
        random_index = random.randint(0, len(buttons) - 1)
        button = buttons[random_index]()
        return button

    def create_alert(self, *args, **kwargs):
        alerts = []
        widget_classess = IUIWidget.__subclasses__()
        for widget_class in widget_classess:
            if widget_class.os == 'Windows' and widget_class.type == 'alert':
                alerts.append(widget_class)
        random_index = random.randint(0, len(alerts) - 1)
        alert = alerts[random_index]()
        return alert


class LinuxFactory(IUIFactory):
    """
    Concrete UI factory, creating linux widgets
    """
    def create_button(self, *args, **kwargs):
        buttons = []
        widget_classess = IUIWidget.__subclasses__()
        for widget_class in widget_classess:
            if widget_class.os == 'Linux' and widget_class.type == 'button':
                buttons.append(widget_class)
        random_index = random.randint(0, len(buttons) - 1)
        button = buttons[random_index]()
        return button

    def create_alert(self, *args, **kwargs):
        alerts = []
        widget_classess = IUIWidget.__subclasses__()
        for widget_class in widget_classess:
            if widget_class.os == 'Linux' and widget_class.type == 'alert':
                alerts.append(widget_class)
        random_index = random.randint(0, len(alerts) - 1)
        alert = alerts[random_index]()
        return alert



class WindowsButton1(IUIWidget):
    """
    Concrete UI widget, os Windows
    """
    os = 'Windows'
    type = 'button'

    def print_os(self):
        print(self.os)

class WindowsButton2(IUIWidget):
    """
    Concrete UI widget, os Windows
    """
    os = 'Windows'
    type = 'button'

    def print_os(self):
        print(self.os)

class WindowsAlert1(IUIWidget):
    """
    Concrete UI widget, os Windows
    """
    os = 'Windows'
    type = 'alert'

    def print_os(self):
        print(self.os)

class WindowsAlert2(IUIWidget):
    """
    Concrete UI widget, os Windows
    """
    os = 'Windows'
    type = 'alert'

    def print_os(self):
        print(self.os)


class LinuxButton1(IUIWidget):
    """
    Concrete UI widget, os Linux
    """
    os = 'Linux'
    type = 'button'

    def print_os(self):
        print(self.os)

class LinuxButton2(IUIWidget):
    """
    Concrete UI widget, os Linux
    """
    os = 'Linux'
    type = 'button'

    def print_os(self):
        print(self.os)

class LinuxAlert1(IUIWidget):
    """
    Concrete UI widget, os Linux
    """
    os = 'Linux'
    type = 'alert'

    def print_os(self):
        print(self.os)

class LinuxAlert2(IUIWidget):
    """
    Concrete UI widget, os Linux
    """
    os = 'Linux'
    type = 'alert'

    def print_os(self):
        print(self.os)




def main():
    windows_factory = WindowsFactory()
    linux_factory = LinuxFactory()

    w_button, w_alert = windows_factory.order_widgets([1, 2, 3, 4, 5], teste='Teste')
    l_button, l_alert = linux_factory.order_widgets()

    print()

main()