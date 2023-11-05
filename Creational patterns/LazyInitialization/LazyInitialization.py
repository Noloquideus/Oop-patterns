def _initialize_expensive_data():
    return "Expensive data"


class LazyInitialization:
    def __init__(self):
        self._expensive_data = None

    @property
    def expensive_data(self):
        if self._expensive_data is None:
            self._expensive_data = _initialize_expensive_data()
        return self._expensive_data

# Usage example
lazy_obj = LazyInitialization()

print(lazy_obj.expensive_data)  # "Expensive data"

print(lazy_obj.expensive_data)  # "Expensive data"
