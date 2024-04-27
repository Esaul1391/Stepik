class Atomic:
    def __init__(self, data, deep=False):
        self.data = data
        self.snapshot = None
        self.deep = deep

    def __enter__(self):
        self.snapshot = self.deepcopy(self.data) if self.deep else self.data
        return self.data

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            if isinstance(exc_val, IndexError):
                return True  # Exit early if IndexError occurs
            if self.deep:
                self.data.clear()
                self.data.extend(self.snapshot)
            else:
                self.data[:] = self.snapshot

    def deepcopy(self, obj):
        if isinstance(obj, list):
            return [self.deepcopy(item) for item in obj]
        elif isinstance(obj, dict):
            return {key: self.deepcopy(value) for key, value in obj.items()}
        elif isinstance(obj, set):
            return {self.deepcopy(item) for item in obj}
        else:
            return obj