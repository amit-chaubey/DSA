class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)
    
    def dequeue(self):
        if self.is_empty():
            return "Stack Underflow"
        return self.queue.pop(0)
    
    def is_empty(self):
        return self.size()==0
    
    def peek(self):
        if self.is_empty():
            return "Stack Underflow"
        return self.queue[0]
    
    def size(self):
        return len(self.queue)
    
    def display(self):
        return self.queue
    
if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(11)        
    queue.enqueue(22)
    queue.enqueue(33)
    queue.enqueue(44)
    print(queue.display())
    print(queue.dequeue())
    print(queue.display())
    print(queue.peek())
    print(queue.size())
    print(queue.is_empty())
        

    