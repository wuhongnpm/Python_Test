class Stack():
    def __init__(self, size):
        self.stack131 = []
        self.top = -1
        self.size = size

    def isfull(self):
        return self.top + 1 == self.size

    def isempty(self):
        return self.top == '-1'

    # 入栈前先检查栈是否已满
    def push_stack(self, x):
        if self.isfull():
            raise Exception("statck is full")
        else:
            self.stack131.append(x)
            self.top = self.top + 1

    # 出栈之前检查栈是否为空
    def pop_statck(self):
        if self.isempty():
            raise Exception("stack is empty")
        else:
            self.top = self.top - 1
            self.stack131.pop()

    def show_stack(self):
        print(self.stack131)


if __name__ == "__main__":
    s = Stack(10)
    s.show_stack()
    for i in range(6):
        s.push_stack(i)
    s.show_stack()
    for i in range(3):
        s.pop_statck()
    s.show_stack()
    print("stack FILO is end.......")
