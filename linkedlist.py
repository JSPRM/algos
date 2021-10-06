class node():
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
        
class linked_list():
    def __init__(self):
        self.head = node()
    
    def append(self, data) -> None:
        nuevo_node = node(data)
        current = self.head
        while (current.next != None):
            current = current.next
        current.next = nuevo_node
    
    def size(self) -> int:
        current = self.head
        size = 0
        while (current.next != None):
            current = current.next
            size+=1
        return size
    
    def print(self) -> None:
        r = []
        current = self.head
        while (current.next != None):
            current = current.next
            r.append(current.data)
        print(r)
        
if __name__ == "__main__":
    jijo = linked_list()
    jijo.append(3)
    jijo.append("Hola")
    
    print(jijo.size())
    jijo.print()
    
        