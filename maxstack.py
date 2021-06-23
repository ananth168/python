class MaxStack:
    def __init__(self) :
        self.stack = []
        self.max = []

    def push(self, x):
        self.stack.append(x)

        if self.max:
            if x >= self.max[-1]:
                self.max.append(x)
        else:
            self.max.append(x)

    def pop(self):
        if self.stack[-1] == self.max[-1]:
            self.max.pop()
        self.stack.pop()

    def top(self):
        return self.stack[-1]
    
    def getMax(self):
        return self.max[-1]


object = MaxStack()
object.push(2)
object.push(6)
object.push(4)
object.pop()
object.push(5)
print(object.stack)

top_ele = object.top()
print("top element is : ", top_ele)

max_ele = object.getMax()
print("maximum element is : ", max_ele)

