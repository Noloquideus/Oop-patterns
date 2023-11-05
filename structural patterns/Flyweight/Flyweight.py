class Flyweight:
    def __init__(self, shared_state):
        self.shared_state = shared_state

    def operation(self, unique_state):
        pass

class ConcreteFlyweight(Flyweight):
    def operation(self, unique_state):
        print(f"Выполняется операция с общим состоянием '{self.shared_state}' и уникальным состоянием '{unique_state}'")

class FlyweightFactory:
    def __init__(self):
        self.flyweights = {}

    def get_flyweight(self, shared_state):
        if shared_state not in self.flyweights:
            self.flyweights[shared_state] = ConcreteFlyweight(shared_state)
        return self.flyweights[shared_state]

# Пример использования
factory = FlyweightFactory()

flyweight1 = factory.get_flyweight("Общее состояние")
flyweight1.operation("Уникальное состояние 1")

flyweight2 = factory.get_flyweight("Общее состояние")
flyweight2.operation("Уникальное состояние 2")
