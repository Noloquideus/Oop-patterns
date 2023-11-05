class Car:
    def __init__(self, model, color, engine_power):
        self.model = model
        self.color = color
        self.engine_power = engine_power


class CarBuilder:
    def __init__(self):
        self.model = None
        self.color = None
        self.engine_power = None

    def set_model(self, model):
        self.model = model
        return self

    def set_color(self, color):
        self.color = color
        return self

    def set_engine_power(self, engine_power):
        self.engine_power = engine_power
        return self

    def build(self):
        return Car(self.model, self.color, self.engine_power)


# Using
car_builder = CarBuilder()
car_builder.set_model("Sedan").set_color("Red").set_engine_power(200)
car = car_builder.build()
