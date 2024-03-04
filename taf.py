class MyEmptyStackException(Exception):
    pass

class MyOutOfSizeException(Exception):
    pass

class MyStack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.stack = []
    
    def add_to_stack(self, item):
        if len(self.stack) >= self.max_size:
            raise MyOutOfSizeException("La pile est pleine")
        self.stack.append(item)
    
    def pop_from_stack(self):
        if len(self.stack) == 0:
            raise MyEmptyStackException("La pile est vide")
        return self.stack.pop()
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def is_full(self):
        return len(self.stack) >= self.max_size

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
