class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Deletes all duplicates from a given linked list.
        
        :param head: A pointer to the head of the linked list.
        :type head: Optional[ListNode]
        
        :return: A pointer to the head of the linked list with all duplicates removed.
        :rtype: Optional[ListNode]
        """
        if head is None:
            return head

        current = head 
        while current.next:
            if current.val == current.next.val:
                current.next = current.next.next 
            else:
                current = current.next 
        
        return head