class Stack:
    def __init__(self):
        """
        Initializes a new instance of the class with an empty stack, a maximum size of 10,
        and a length of -1.

        Parameters:
            self: the object instance.

        Returns:
            None
        """
        self.stack = []
        self.MAX_SIZE = 10
        self.length = -1
        self.initialize_stack()
        
    def push(self, value) -> None:
        """
        Pushes a new value to the top of the stack.
        
        :param value: The value to be pushed onto the stack.
        :type value: Any
        
        :return: None
        """
        if self.length == self.MAX_SIZE-1:
            return "Error: Stack Overflow"
        
        self.length += 1
        self.stack[self.length] = value
           
    
    def pop(self) -> None:
        """
        Removes and returns the top element from the stack.
        
        :param None
        :return None
        
        If the stack is empty, it returns an error message "Error: Stack Underflow".
        """
        if self.length == -1:
            return "Error: Stack Underflow"

        self.stack[self.length] = -1
        self.length -= 1
    
    def peek(self) -> int:
        """
        Returns the top element of the stack without removing it. 

        :param self: The instance of the stack class.

        :return: Returns the top element of the stack. If the stack is empty, it returns -1.
        :rtype: int or str
        """
        return self.stack[self.length] if self.length >= 0 else -1

    
    def is_empty(self) -> bool:
        return self.length == -1
    
    def clear(self) -> None:
        """
        Clears the stack by resetting the stack and stack length to their initial values. 
        This function takes no parameters and returns nothing.
        """
        self.stack = []
        self.length = -1
        self.initialize_stack()
        
    def initialize_stack(self) -> None:
        """
        Initializes the stack by appending -1 to the stack list for the range of self.MAX_SIZE.

        :param self: The instance of the class.
        :return: None
        """
        for i in range(self.MAX_SIZE):
            self.stack.append(-10**9)
    