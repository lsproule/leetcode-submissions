class MinStack:

    def __init__(self):
       self.arr = [] 
       self.min_index = []

    def push(self, val: int) -> None:
        self.arr.append(val)

        if self.min_index == []: 
            self.min_index.append(0)
        elif self.arr[self.min_index[-1]] > val:
            self.min_index.append(len(self.arr) - 1)
        

    def pop(self) -> None:
        if self.min_index[-1] == len(self.arr) -1: 
            self.min_index.pop()
        return self.arr.pop()
        

    def top(self) -> int:
        return self.arr[len(self.arr)-1]

    def getMin(self) -> int:
        return self.arr[self.min_index[-1]]
        
