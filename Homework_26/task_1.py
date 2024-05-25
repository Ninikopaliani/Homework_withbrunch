class Inset:
    def __init__(self):
        self.list_elements = []

    def insert(self, element):
        return self.list_elements.append(element)

    def member(self, element):
        if element in self.list_elements:
            return True
        return False

    def remove(self, element):
        if element in self.list_elements:
            self.list_elements.pop(element)
        raise ValueError("could not find element in this list")

    def __str__(self):
        sorted(self.list_elements)
        for i in range(len(self.list_elements)):
            return f"{self.list_elements[i]}"


def main():
    l1 = Inset()
    l1.insert(3)
    print(l1.list_elements)



