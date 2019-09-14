from node import Node
class LinkedList:
    def __init__(self):
        self.head = None
    def is_empty(self):
        return self.head == None
    def add(self, valor):
            node = Node(valor)
            node.setProximo(self.head)
            self.head = node
    def size(self):
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.getProximo()
        return count
    def search(self, valor):
        busca = False
        current = self.head
        while current != None:
            if current.getDado() == valor:
                busca = True
                break
            else: 
                current = current.getProximo()
        return busca
    def delete(self, valor):
        current = self.head
        previous = None
        found = False

        while not found:
            if current.getDado() == valor:
                found = True
            else:
                previous = current
                current = current.getProximo()
        if previous == None:
            self.head = current.getProximo()
        else:
            previous.setProximo(current.getProximo())




linked_list = LinkedList()
linked_list.add(77)
linked_list.add(17)
linked_list.add(93)
linked_list.add(26)
linked_list.add(54)
print(linked_list.size())
print(linked_list.search(93))
linked_list.delete(93)
print(linked_list.search(93))

