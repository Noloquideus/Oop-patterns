class Multiton:
    __instances = {}

    @staticmethod
    def get_instance(key):
        if key not in Multiton.__instances:
            Multiton.__instances[key] = Multiton()
        return Multiton.__instances[key]

    def __init__(self):
        pass


# Usage example
multiton_instance1 = Multiton.get_instance("Instance 1")
multiton_instance2 = Multiton.get_instance("Instance 2")
print(multiton_instance1 is multiton_instance2)  # False

multiton_instance3 = Multiton.get_instance("Instance 1")
print(multiton_instance1 is multiton_instance3)  # True
