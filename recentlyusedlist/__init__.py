class RecentlyUsedList():
    def __init__(self):
        self._values = []

    def __len__(self):
        return len(self._values)

    def add(self, value):
        self._values.append(value)
