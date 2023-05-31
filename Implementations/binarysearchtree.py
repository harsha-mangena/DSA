class Node:
    def __init__(self, data):
        """
        Initializes a new instance of the class with the specified data.

        Args:
            data: The data to be stored in the node.

        Returns:
            None.
        """
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        """
        Initializes an instance of the class with a None value assigned to the 'root' instance variable.

        Args:
            None

        Returns:
            None
        """
        self.root = None

    def insert(self, data):
        """
        Inserts a new node with the given data into the binary tree.

        :param data: The data to be inserted into the binary tree.
        :type data: Any
        :return: None
        """
        if self.root is None:
            self.root = Node(data)
        else:
            stack = [self.root]
            while stack:
                node = stack.pop()
                if node.left is None:
                    node.left = Node(data)
                    break
                elif node.right is None:
                    node.right = Node(data)
                    break
                else:
                    stack.append(node.left)
                    stack.append(node.right)

    def search(self, data):
        """
        Given a data value, this function searches for a matching node in the binary tree starting from the root.
        :param data: The data value to search for
        :return: True if the matching node is found, False otherwise
        """
        if self.root is None:
            return False
        stack = [self.root]
        while stack:
            node = stack.pop()
            if node.data == data:
                return True
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)
        return False

    def delete(self, data):
        """
        Deletes a node with the given data from the binary search tree.

        :param data: the data of the node to delete
        :type data: any
        :return: True if the node was found and deleted, False otherwise
        :rtype: bool
        """
        if self.root is None:
            return False
        if self.root.data == data:
            if self.root.left is None:
                self.root = self.root.right
            elif self.root.right is None:
                self.root = self.root.left
            else:
                stack = [self.root.right]
                while stack[-1].left:
                    stack.append(stack[-1].left)
                stack[-1].left = self.root.left
                self.root = self.root.right
            return True
        stack = [self.root]
        while stack:
            node = stack.pop()
            if node.left and node.left.data == data:
                if node.left.left is None:
                    node.left = node.left.right
                elif node.left.right is None:
                    node.left = node.left.left
                else:
                    temp = node.left.right
                    node.left = node.left.left
                    stack.append(temp)
                return True
            elif node.right and node.right.data == data:
                if node.right.left is None:
                    node.right = node.right.right
                elif node.right.right is None:
                    node.right = node.right.left
                else:
                    temp = node.right.right
                    node.right = node.right.left
                    stack.append(temp)
                return True
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)
        return False

    def inorder(self):
        """
        Traverses the binary search tree in-order and prints the data of each node visited.
        
        Parameters:
        None
        
        Returns:
        None
        """
        if self.root is None:
            return
        stack = []
        node = self.root
        while True:
            if node is not None:
                stack.append(node)
                node = node.left
            elif stack:
                node = stack.pop()
                print(node.data, end=' ')
                node = node.right
            else:
                break
        print()

    def preorder(self):
        """
        Performs a preorder traversal of the binary tree starting from the root node.
        Does not take any parameters.
        Does not return any value. Prints the preorder traversal of the binary tree.
        """
        if self.root is None:
            return
        stack = [self.root]
        while stack:
            node = stack.pop()
            print(node.data, end=' ')
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        print()

    def postorder(self):
        """
        Traverses the binary tree in postorder (left-right-root) and prints the data of each node.
        
        Returns:
        None
        
        Parameters:
        self: The binary tree object.
        """
        if self.root is None:
            return
        stack1 = [self.root]
        stack2 = []
        while stack1:
            node = stack1.pop()
            stack2.append(node)
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
        while stack2:
            node = stack2.pop()
            print(node.data, end=' ')
        print()

