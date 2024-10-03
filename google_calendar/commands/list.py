class List():
    def __init__(self, type: str):
        self._type = type

    def run(self):
        print("{self._type = }")