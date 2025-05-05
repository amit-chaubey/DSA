class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def insert_at_position(self,data,position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for i in range(position-1):
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def print_ll(self):
        current = self.head
        while current:
            print(current.data,end="->")
            current = current.next
        print("None")

    def delete_at_position(self,position):
        if position == 0:
            self.head = self.head.next
        else:
            current = self.head
            for i in range(position-1):
                current = current.next
            current.next = current.next.next

    
if __name__=="__main__":
    ll = SingleLinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.delete_at_position(2)
    ll.insert_at_position(4,2)

    print(ll.head.data)

   
    ll.print_ll()
