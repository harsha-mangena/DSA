class Solution:
    def _naive(self, head: Optional[ListNode]) -> bool:
        """
        Checks if there is a cycle in a linked list using a naive approach. 

        :param head: A reference to the head of the linked list.
        :type head: Optional[ListNode]
        :return: True if there is a cycle in the linked list, False otherwise.
        :rtype: bool
        """
        next_store = {}
        
        while head:
            if head.next in next_store:
                return True
            next_store[head.next] = 1
            head = head.next
        
        return False
    
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Determines whether a given linked list has a cycle or not.

        Args:
            head (Optional[ListNode]): The head node of the linked list.

        Returns:
            bool: True if the linked list has a cycle, False otherwise.
        """
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                return True
        
        return False
    
    