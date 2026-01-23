from collections import deque
class Queue():
    E = deque()
    D = deque()
    def enqueue(self, x):
        self.E.append(x)
    def dequeue(self):
        if self.D:
            self.D.pop()
        else:
            while self.E:
                x = self.E.pop()
                if self.E:
                    self.D.append(x)

q = Queue()
q.enqueue(3)
q.enqueue(5)
q.enqueue(7)
q.dequeue()
q.enqueue(10)
q.enqueue(12)
q.print_contents()

        

    