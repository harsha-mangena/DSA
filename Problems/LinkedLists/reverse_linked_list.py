class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverses a linked list in place.

        Args:
            head (Optional[ListNode]): A reference to the head of the linked list.

        Returns:
            Optional[ListNode]: A reference to the head of the reversed linked list.
        """
        #Edge case
        if head is None or head.next is None: return head

        previous = next_pointer = None

        while head:
            next_pointer = head.next
            head.next = previous
            previous = head
            head = next_pointer
        
        return previous