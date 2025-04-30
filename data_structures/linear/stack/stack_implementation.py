class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)

    def is_empty(self):
        return len(self.stack) == 0 
    

    def pop(self):
        if self.is_empty():
            return "Stack Underflow"
        return self.stack.pop()
    
    def peek(self):
        if self.is_empty():
            return "Stack Underflow"
        return self.stack[-1]
    
    def size(self):
        return len(self.stack)
    
    def print_stack(self):
        print("Stack (top to bottom): ", self.stack[::-1])


if __name__ =="__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.print_stack()
    print(stack.pop())
    print(stack.peek())
    print(stack.size())
    stack.print_stack()