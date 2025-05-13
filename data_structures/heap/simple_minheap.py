class MinHeap:
    def __init__(self):
        self.heap_list = []  # List to store heap elements
    
    def get_parent_index(self, child_index):
        return (child_index - 1) // 2
    
    def get_left_child_index(self, parent_index):
        return 2 * parent_index + 1
    
    def get_right_child_index(self, parent_index):
        return 2 * parent_index + 2
    
    def has_parent(self, child_index):
        return self.get_parent_index(child_index) >= 0
    
    def has_left_child(self, parent_index):
        return self.get_left_child_index(parent_index) < len(self.heap_list)
    
    def has_right_child(self, parent_index):
        return self.get_right_child_index(parent_index) < len(self.heap_list)
    
    def get_parent_value(self, child_index):
        return self.heap_list[self.get_parent_index(child_index)]
    
    def get_left_child_value(self, parent_index):
        return self.heap_list[self.get_left_child_index(parent_index)]
    
    def get_right_child_value(self, parent_index):
        return self.heap_list[self.get_right_child_index(parent_index)]
    
    def swap(self, index1, index2):
        self.heap_list[index1], self.heap_list[index2] = self.heap_list[index2], self.heap_list[index1]
    
    def add(self, value):
        self.heap_list.append(value)
        self._bubble_up(len(self.heap_list) - 1)
    
    def _bubble_up(self, child_index):
        while self.has_parent(child_index) and self.heap_list[child_index] < self.get_parent_value(child_index):
            parent_index = self.get_parent_index(child_index)
            self.swap(child_index, parent_index)
            child_index = parent_index
    
    def remove_min(self):
        if len(self.heap_list) == 0:
            return None
        
        if len(self.heap_list) == 1:
            return self.heap_list.pop()
        
        min_value = self.heap_list[0]
        self.heap_list[0] = self.heap_list.pop()
        self._bubble_down(0)
        
        return min_value
    
    def _bubble_down(self, parent_index):
        while self.has_left_child(parent_index):
            smaller_child_index = self.get_left_child_index(parent_index)
            
            if self.has_right_child(parent_index) and self.get_right_child_value(parent_index) < self.get_left_child_value(parent_index):
                smaller_child_index = self.get_right_child_index(parent_index)
            
            if self.heap_list[parent_index] < self.heap_list[smaller_child_index]:
                break
            else:
                self.swap(parent_index, smaller_child_index)
            
            parent_index = smaller_child_index
    
    def peek(self):
        return self.heap_list[0] if self.heap_list else None
    
    def size(self):
        return len(self.heap_list)
    
    def is_empty(self):
        return len(self.heap_list) == 0
    
    def print_heap(self):
        print("Heap:", self.heap_list)

# Test the heap
if __name__ == "__main__":
    # Create a new heap
    heap = MinHeap()
    
    # Add some numbers
    print("Adding numbers: 5, 3, 7, 1, 9")
    heap.add(5)
    heap.add(3)
    heap.add(7)
    heap.add(1)
    heap.add(9)
    
    print("\nInitial heap:")
    heap.print_heap()
    
    print("\nRemoving minimum values one by one:")
    while not heap.is_empty():
        min_value = heap.remove_min()
        print(f"Removed: {min_value}")
        heap.print_heap()
