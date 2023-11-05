import threading


class ObjectPool:
    
    def __init__(self, object_factory, max_size):
        self._object_factory = object_factory
        self._max_size = max_size
        self._lock = threading.Lock()
        self._pool = []

    def acquire(self):
        with self._lock:
            if len(self._pool) > 0:
                return self._pool.pop()
            else:
                return self._object_factory()

    def release(self, obj):
        with self._lock:
            if len(self._pool) < self._max_size:
                self._pool.append(obj)
