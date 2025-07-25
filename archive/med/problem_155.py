class MinStack:
    def __init__(self):
        self.data = []

    def push(self, val: int) -> None:
        self.data.insert(0, val) 

    def pop(self) -> None:
        self.data.pop(0)

    def top(self) -> int:
        return self.data[0]

    def getMin(self) -> int:
        return min(self.data)
