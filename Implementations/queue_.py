class Queue:
    def __init__(self, size=10) -> None:
        """
        Initialize a new queue with a given size.
        
        Args:
            size (int): The size of the queue. Defaults to 10.
        Returns:
            None
        """
        self.size = size
        self.queue = [-1] * self.size
        self.front = 0
        self.rear = 0
        self.count = 0
        
    def is_empty(self) -> bool:
        """
        Return a boolean indicating whether the object is empty or not
        """
        return self.count == 0
    
    def is_full(self) -> bool:
        """
        Determines if the data structure is full.

        :return: A boolean indicating if the data structure is full.
        """
        return self.count == self.size
    
    def enqueue(self, item):
        """
        Enqueues an item at the end of the queue.

        :param item: An object to be added to the queue.
        :type item: any

        :return: None
        """
        if self.is_full():
            return "Queue is full. Unable to enqueue item."

        self.queue[self.rear] = item
        self.rear = (self.rear + 1) % self.size
        self.count += 1
        
    def dequeue(self):
        """
        Removes and returns an item from the front of the queue. If the queue is empty, a message is printed and
        None is returned. 

        Returns:
            item (Any): The item dequeued from the front of the queue. If the queue is empty, None is returned.
        """
        if self.is_empty():
            return "Queue is empty. Unable to dequeue item."

        item = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return item
    
    def peek(self):
        """
        Returns the first element in the queue without removing it. If the queue is empty, 
        it prints an error message and returns None.

        :return: The first element in the queue.
        """
        if self.is_empty():
            return "Queue is empty. No item to peek."
        return self.queue[self.front]
    
    def clear(self):
        """
        Clears the queue.
        """
        self.front = 0
        self.rear = 0
        self.queue = [None] * self.size
        self.count = 0
    
    
    