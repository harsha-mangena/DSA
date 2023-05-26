class Node:
    def __init__(self, data) -> None:
        """
        Initializes a new instance of the class with the given data.

        :param data: The data to be stored in the node.
        :type data: Any
        :return: None
        """
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None 
        
    def insert(self, data) -> None:
        """
        Inserts a new node at the end of the linked list.
        check 1: If the head is None
        check 2: If the head is not None
        """
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        
        last_node.next = new_node
    
    def insert_at_beginning(self, data) -> None:
        """
        Inserts a new node at the beginning of the linked list.
        """
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        new_node.next = self.head
        self.head = new_node
        
    def is_empty(self) -> bool:
        return self.head is None
    
    def delete(self, value) -> None:
        """
        Deletes the node with the given value from the linked list. 
        
        :param value: The value of the node to be deleted.
        :type value: any
        
        :return: None
        
        1) If the linked list is empty, return an error message.
        2) If the node to be deleted is at the head, reassign head.
        3) Iterate through the list, and find the node to be deleted.
        """
        if self.is_empty():
            return "Error: Linked List is empty"
        
        if self.head.data == value:
            self.head = self.head.next
            return
        
        current_node = self.head
        while current_node.next:
            if current_node.next.value == value:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next
        
    def display(self) -> None:
        """
        Displays the data of all nodes in the linked list in the format "data1->data2->...->dataN->NULL".
        Does not return anything.
        """
        if self.is_empty():
            return "Error: Linked List is empty"
        
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end="->")
            current_node = current_node.next
        print("NULL")
        
    def clear(self) -> None:
        """
        Clears the linked list by setting the head to None.

        :param None
        :return None
        """
        self.head = None
        
    def get_to_list(self) -> None:
        """
        Returns a list of all the elements in the LinkedList.
        Does not modify the LinkedList.

        :return: A list of all the elements in the LinkedList.
        :rtype: list
        """
        if self.is_empty():
            return []
        
        nodes = list()
        current_node = self.head
        while current_node:
            nodes.append(current_node.data)
            current_node = current_node.next 
        
        return nodes        