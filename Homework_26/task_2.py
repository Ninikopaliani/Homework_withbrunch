class Queue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return len(self.elements) == 0

    def insert(self, new_element):
        self.elements.append(new_element)

    def pop(self):
        if self.is_empty():
            raise ValueError("Stack is empty")

        return self.elements.pop(0)


q = Queue()
q.insert(1)
q.insert(2)
q.insert(3)
print(q.elements)

print(q.pop())
print("left in stack ", q.elements)