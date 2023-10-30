class Adaptee:
    def specific_request(self):
        return "Specific request"

# Адаптер
class Adapter:
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def request(self):
        return f"Adapter: Translated {self.adaptee.specific_request()}"

adaptee = Adaptee()
adapter = Adapter(adaptee)

result = adapter.request()
print(result)
