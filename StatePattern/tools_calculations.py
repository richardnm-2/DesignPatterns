from abc import ABC, abstractmethod


class CalculationTool(ABC):
    @abstractmethod
    def calculate():
        pass


class VibrationCalculation(CalculationTool):
    def calculate(self):
        print('Vibration data parser')


class RelubricationIntervalCalculation(CalculationTool):
    def calculate(self):
        print('Relubrication interval calculation')


class TraceWidthCalculation(CalculationTool):
    def calculate(self):
        print('Trace width calculation')


class Calculation():
    current_calculation = None

    def calculate(self):
        self.current_tool.calculate()


    def get_current_tool(self):
        return self.current_tool

    def set_current_tool(self, tool):
        self.current_tool = tool


def main(calculation_tool_name):
    calculation_tool = globals()[calculation_tool_name]()
    calculation = Calculation()
    calculation.set_current_tool(calculation_tool)
    calculation.calculate()

main('TraceWidthCalculation')