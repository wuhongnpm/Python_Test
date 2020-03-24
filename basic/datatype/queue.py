class Queue():
    def __init__(self, size):
        self.queue132 = []
        self.front = -1
        self.rear = -1
        self.size = size

    def isfull(self):
        return self.rear - self.front + 1 == self.size

    def isempty(self):
        return self.front == self.rear

    # 入队列
    def enqueue(self, x):
        if self.isfull():
            raise Exception("queue is full")
        else:
            self.queue132.append(x)
            self.rear = self.rear + 1

    # 出队列
    def dequeue(self):
        if self.isempty():
            raise Exception("queue is empty")
        else:
            self.queue132.pop(0)
            self.front = self.front + 1

    def show_queue(self):
        print(self.queue132)

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

    q = Queue(7)
    q.show_queue()
    for i in range(6):
        q.enqueue(i)
    q.show_queue()
    for i in range(3):
        q.dequeue()
    q.show_queue()
