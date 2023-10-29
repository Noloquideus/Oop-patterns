class AbstractFactory:
    def create_product_a(self):
        pass

    def create_product_b(self):
        pass


class ConcreteFactory1(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA1()

    def create_product_b(self):
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA2()

    def create_product_b(self):
        return ConcreteProductB2()


class AbstractProductA:
    def operation_a(self):
        pass


class ConcreteProductA1(AbstractProductA):
    def operation_a(self):
        return "ConcreteProductA1 operation"


class ConcreteProductA2(AbstractProductA):
    def operation_a(self):
        return "ConcreteProductA2 operation"


class AbstractProductB:
    def operation_b(self):
        pass


class ConcreteProductB1(AbstractProductB):
    def operation_b(self):
        return "ConcreteProductB1 operation"


class ConcreteProductB2(AbstractProductB):
    def operation_b(self):
        return "ConcreteProductB2 operation"
