class HashTable:
    def __init__(self, size=10):
        """
        Initializes a new instance of the class with the given size.

        :param size: An integer representing the size of the table to be initialized.
        :type size: int

        :return: None
        :rtype: None
        """
        self.size = size
        self.table = [[] for i in range(size)]

    def hash_function(self, key):
        """
        Returns the hash value of the key by taking the length of the key and performing the modulus operation 
        with the size of the hash table. 

        Parameters:
        key (any): The key to be hashed.

        Returns:
        int: The hash value of the key.
        """
        return len(key) % self.size

    def insert(self, key, value):
        """
        Inserts a key-value pair into the hash table. The function uses the hash function 
        to determine the index of the key in the table. If the index is empty, the key-value 
        pair is added to the table. Otherwise, the function handles the collision by chaining 
        the new key-value pair to the existing pairs at the index.
        
        :param key: The key to be inserted.
        :type key: Any hashable type.
        :param value: The value to be inserted.
        :type value: Any type.
        :return: None.
        """
        index = self.hash_function(key)

        if self.table[index] is None:
            self.table[index] = [key, value]
        else:
            # Handle collision (chaining)
            self.table[index].append((key, value))

    def search(self, key):
        """
        Searches for a key in the hash table and returns its value if found, otherwise returns None.
        
        :param key: The key to be searched in the hash table.
        :type key: Any hashable type.
        
        :return: The value associated with the key in the hash table, if found. Otherwise, returns None.
        :rtype: Any type or None.
        """
        index = self.hash_function(key)

        if self.table[index] is None:
            return None
        elif self.table[index][0] == key:
            return self.table[index][1]
        else:
            # Handle collision (chaining)
            for pair in self.table[index]:
                if pair[0] == key:
                    return pair[1]

        return None  # Key not found


# Example usage:
hash_table = HashTable()

hash_table.insert("apple", 5)
hash_table.insert("banana", 10)
hash_table.insert("cherry", 15)

print(hash_table.search("banana"))  # Output: 10
print(hash_table.search("grape"))   # Output: None
