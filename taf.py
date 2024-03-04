class MyEmptyStackException(Exception):
    pass

class MyOutOfSizeException(Exception):
    pass

class MyStack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.stack = [None] * max_size
        self.top_index = -1
    
    def add_to_stack(self, item):
        if self.is_full():
            raise MyOutOfSizeException("La pile est pleine")
        self.top_index += 1
        self.stack[self.top_index] = item
    
    def pop_from_stack(self):
        if self.is_empty():
            raise MyEmptyStackException("La pile est vide")
        item = self.stack[self.top_index]
        self.stack[self.top_index] = None
        self.top_index -= 1
        return item
    
    def is_empty(self):
        return self.top_index == -1
    
    def is_full(self):
        return self.top_index == self.max_size - 1

if __name__ == '__main__':
    myStack = MyStack(3)
    myStack.add_to_stack('hello')
    myStack.add_to_stack('world')
    print(myStack.is_full())  # False
    myStack.add_to_stack('!')
    print(myStack.is_full())  # True
    try:
        myStack.add_to_stack('extra')  # MyOutOfSizeException
    except MyOutOfSizeException as e:
        print(e)
    print(myStack.pop_from_stack())  # !
    print(myStack.is_empty())  # False
    print(myStack.pop_from_stack())  # world
    print(myStack.is_empty())  # False
    print(myStack.pop_from_stack())  # hello
    print(myStack.is_empty())  # True
    try:
        print(myStack.pop_from_stack())  # MyEmptyStackException
    except MyEmptyStackException as e:
        print(e)
