class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Returns the middle node of a linked list.
        :param head: The head node of the linked list.
        :type head: Optional[ListNode]
        :return: The middle node of the linked list.
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head

        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        return slow