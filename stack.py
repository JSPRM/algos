class Node():
    def __init__(self, value, next=None):
        self.value =  value
        self.next = next

class Stack():
    def __init__(self):
        self.head = Node()
        self.size = 0
        
    def append(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1
        
    def pop(self):
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value