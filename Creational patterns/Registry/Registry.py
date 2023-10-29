class Registry:
    def __init__(self):
        self._registry = {}

    def register(self, key, value):
        self._registry[key] = value

    def unregister(self, key):
        del self._registry[key]

    def get(self, key):
        return self._registry.get(key, None)

    def get_all(self):
        return self._registry

# Пример использования реестра
# Создаем экземпляр реестра
registry = Registry()

# Регистрируем объекты в реестре
registry.register('key1', 'value1')
registry.register('key2', 'value2')
registry.register('key3', 'value3')

# Получаем объекты из реестра по ключу
value1 = registry.get('key1')
value2 = registry.get('key2')
value3 = registry.get('key3')

# Получаем все объекты из реестра
all_values = registry.get_all()

# Выводим результаты
print(value1)  # Выведет: value1
print(value2)  # Выведет: value2
print(value3)  # Выведет: value3
print(all_values)  # Выведет: {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}