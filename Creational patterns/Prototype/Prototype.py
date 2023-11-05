import copy


class Prototype:
    def clone(self):
        return copy.deepcopy(self)


class ConcretePrototype(Prototype):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return f"Data: {self.data}"


# Пример использования
prototype = ConcretePrototype("Initial data")
clone = prototype.clone()
print(prototype)  # "Data: Initial data"
print(clone)  # "Data: Initial data"

clone.data = "Modified data"
print(prototype)  # "Data: Initial data"
print(clone)  # "Data: Modified data"
