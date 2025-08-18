class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class SinglyLinkedList:
    def __init__(self, start=None, tail= None):
        self.start = start
        self.tail = tail

    def is_empty(self):
        return self.start is None
    
    def insert_at_start(self, data):
        new_node = Node(data, self.start)
        self.start = new_node
        if self.tail is None:
            self.tail = new_node

    def insert_at_last(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.start = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None
    
    def insert_after(self,temp, data):
        if self.is_empty():
            return ValueError("List is empty")
        new_node = Node(data, temp.next)
        temp.next = new_node
        if temp == self.tail:
            self.tail = new_node
        
        return new_node
    
    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end= '->')
            temp = temp.next
        print()  # for a new line after printing the list

    def delete_first(self):
        if self.is_empty():
            return ValueError("List is empty")
        removed_item = self.start
        self.start = self.start.next
        if self.start is None:
            self.tail = None
        return removed_item.item
    
    def delete_last(self):
        if self.is_empty():
            raise ValueError("List is empty")

        # Single-node list
        if self.start.next is None:
            item = self.start.item
            self.start = self.tail = None
            return item

        # Find penultimate node
        temp = self.start
        while temp.next.next is not None:  # stop at node before last
            temp = temp.next

        item = temp.next.item              # last node’s data
        temp.next = None                   # drop the last node
        self.tail = temp                  
        return item

    
    def delete_item(self, data):
        """Delete the first node whose item == data. Returns the deleted item."""
        if self.is_empty():
            raise ValueError("List is empty")

        # Case 1: head matches
        if self.start.item == data:
            deleted = self.start
            self.start = self.start.next
            if self.start is None:        
                self.tail = None
            return deleted.item

        # Case 2: find the node BEFORE the one to delete
        prev = self.start
        curr = self.start.next
        while curr is not None and curr.item != data:
            prev, curr = curr, curr.next

        if curr is None:
            raise ValueError("Item not found in the list")

        # curr is the node to delete
        prev.next = curr.next
        if prev.next is None:             
            self.tail = prev
        return curr.item



mylist = SinglyLinkedList()
mylist.insert_at_start(10)
mylist.insert_at_start(20)
mylist.insert_at_last(30)
mylist.insert_at_last(40)
mylist.insert_after(mylist.search(20), 25)
mylist.delete_last()
mylist.delete_item(25)

print("List after inserting elements:")
mylist.print_list()

