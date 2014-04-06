class RecentlyUsedList():
    def __init__(self, values=[]):
        self._values = values

    def __len__(self):
        return len(self._values)

    def __getitem__(self, key):
        return self._values[key]

    def __iter__(self):
        return iter(self._values)

    def add(self, value):
        if value and value not in self._values:
            self._values.insert(0, value)

    def last(self):
        return self._values[-1]

    def first(self):
        return self._values[0]
