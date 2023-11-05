from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def operation(self):
        pass


class ConcreteProductA(Product):
    def operation(self):
        return "ConcreteProductA operation"


class ConcreteProductB(Product):
    def operation(self):
        return "ConcreteProductB operation"


class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self):
        product = self.factory_method()
        result = f"Creator: {product.operation()}"
        return result


class ConcreteCreatorA(Creator):
    def factory_method(self):
        return ConcreteProductA()


class ConcreteCreatorB(Creator):
    def factory_method(self):
        return ConcreteProductB()


# Usage example
creator_a = ConcreteCreatorA()
product_a = creator_a.some_operation()
print(product_a)


creator_b = ConcreteCreatorB()
product_b = creator_b.some_operation()
print(product_b)
