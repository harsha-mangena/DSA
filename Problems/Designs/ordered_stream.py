class OrderedStream:

    def __init__(self, n: int):
        self.data = [None]*n
        self.ptr = 0 

    def insert(self, id: int, value: str) -> list[str]:
        """
        Inserts a value into the self.data list at the given id - 1 index. 
        If the id - 1 index is greater than the current pointer, an empty list is returned. 
        The function then iterates through the self.data list until a None value is found or 
        the end of the list is reached. The function returns a slice of the self.data list 
        from the id index to the index of the first None value found. 

        :param id: The index where the value should be inserted.
        :type id: int
        :param value: The value to be inserted.
        :type value: str
        :return: A slice of the self.data list from the id index to the index of the first None value found.
        :rtype: list[str]
        """
        id -= 1 
        self.data[id] = value 
        if id > self.ptr: return [] 
        
        while self.ptr < len(self.data) and self.data[self.ptr]: self.ptr += 1 
        return self.data[id:self.ptr]