class Component:
    def operation(self):
        pass

class ConcreteComponent(Component):
    def operation(self):
        print("Выполняется базовая операция")

class Decorator(Component):
    def __init__(self, component):
        self.component = component

    def operation(self):
        self.component.operation()

class ConcreteDecoratorA(Decorator):
    def operation(self):
        super().operation()
        print("Выполняется дополнительная операция A")

class ConcreteDecoratorB(Decorator):
    def operation(self):
        super().operation()
        print("Выполняется дополнительная операция B")

# Пример использования
component = ConcreteComponent()
decoratorA = ConcreteDecoratorA(component)
decoratorB = ConcreteDecoratorB(decoratorA)

decoratorB.operation()
