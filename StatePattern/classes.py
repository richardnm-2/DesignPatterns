from enum import Enum, auto
from abc import ABC, abstractmethod


class Tooltype(Enum):
    SELECTION = auto()
    BRUSH = auto()
    ERASER = auto()

def get_gurrent_tool():
    pass


class Tool(ABC):
    @abstractmethod
    def mouse_down():
        pass

    @abstractmethod
    def mouse_up():
        pass


class SelectionTool(Tool):
    def mouse_down(self):
        print('Selection icon')

    def mouse_up(self):
        print('Draw dashed rectangle')


class BrushTool(Tool):
    def mouse_down(self):
        print('Brush icon')

    def mouse_up(self):
        print('Draw a line')


class Canvas():
    current_tool = None

    def mouse_down(self):
        self.current_tool.mouse_down()

    def mouse_up(self):
        self.current_tool.mouse_up()

    def get_current_tool(self):
        return self.current_tool

    def set_current_tool(self, tool):
        self.current_tool = tool


def main():
    canvas = Canvas()
    canvas.set_current_tool(SelectionTool())
    canvas.mouse_down()
    canvas.mouse_up()

main()
