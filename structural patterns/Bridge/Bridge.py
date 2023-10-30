# Абстракция
class Abstraction:
    def __init__(self, implementation):
        self.implementation = implementation

    def operation(self):
        return self.implementation.operation_implementation()

# Реализация
class Implementation:
    def operation_implementation(self):
        pass


class ConcreteImplementation1(Implementation):
    def operation_implementation(self):
        return "ConcreteImplementation1: Operation implementation"

class ConcreteImplementation2(Implementation):
    def operation_implementation(self):
        return "ConcreteImplementation2: Operation implementation"

implementation1 = ConcreteImplementation1()
implementation2 = ConcreteImplementation2()
abstraction1 = Abstraction(implementation1)
abstraction2 = Abstraction(implementation2)

result1 = abstraction1.operation()
result2 = abstraction2.operation()

print(result1)
print(result2)
