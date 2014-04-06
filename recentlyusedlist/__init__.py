class RecentlyUsedList():
    def __init__(self):
        self._values = []

    def __len__(self):
        return len(self._values)

    def add(self, value):
        if value and value not in self._values:
            self._values.append(value)
