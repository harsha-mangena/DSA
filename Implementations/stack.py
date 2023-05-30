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
        self.MAX_SIZE = 10
        self.length = -1
        self.stack = [None] * self.MAX_SIZE
        
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

        self.stack[self.length] = None
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
    
    def is_full(self) -> bool:
        return self.length == self.MAX_SIZE-1
    
    def clear(self) -> None:
        """
        Clears the stack by resetting the stack and stack length to their initial values. 
        This function takes no parameters and returns nothing.
        """
        self.stack = [None] * self.MAX_SIZE
        self.length = 0
        
    