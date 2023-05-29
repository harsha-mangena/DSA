class Node:
    def __init__(self, data) -> None:
        """
        Initializes a new instance of the LinkedListNode class with the specified value.

        :param data: The value to assign to the new node.
        :type data: any
        :return: None
        """
        self.data = data
        self.next = None
        self.prev = None
        
class DoublyLinkedList:
    def __init__(self) -> None:
        """
        Initializes a new instance of the class with a null head.

        :param None:
        :type None:
        :return: None
        :rtype: None
        """
        self.head = None
        self.tail = None
        
    def insert_at_beginning(self, data) -> None:
        """
        Inserts the given data at the beginning of the linked list.
        
        :param data: The data to be inserted.
        :type data: Any
        
        :return: None
        :rtype: None
        """
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
    def insert(self, data) -> None:
        """
        Inserts the given data into the linked list.

        Args:
            data: The data to be inserted.

        Returns:
            None.
        """
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
    
    def delete_at_beginning(self):
        """
        Deletes the first node of the linked list.
        Does not take any parameters.
        Does not return anything.
        """
        if self.is_empty():
            return "Error: List is empty"
        
        elif self.head == self.tail:
            self.head = None
            self.tail = None
            
        else:
            self.head = self.head.next
            self.head.prev = None

    def delete_at_end(self):
        """
        Deletes the node at the end of the doubly linked list and updates the tail pointer. 
        
        :return: "Error: List is empty" if the list is empty, else None.
        """
        if self.is_empty():
            return "Error: List is empty"
        
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    def delete_node(self, node):
        """
        Deletes a given node from a doubly linked list.

        :param node: The node to be deleted.
        :type node:
        """
        if self.is_empty():
            return "Error: List is empty"
        elif node == self.head:
            self.delete_at_beginning()
        elif node == self.tail:
            self.delete_at_end()
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

    
    def is_empty(self) -> bool:
        return self.head == None 
    
    def clear(self) -> None:
        """
        Clears the linked list by setting the head node to None.

        :return: None
        """
        self.head = None
        self.tail = None
        
    def get_to_list(self) -> list:
        """
        Returns a list of items. Takes no parameters.

        :return: A list of items.
        :rtype: list
        """
        nodes = list()
        
        if self.head is None:
            return nodes 
        
        current_node = self.head
        
        while current_node is not None:
            nodes.append(current_node.data)
            current_node = current_node.next
        
        return nodes
    
    
        