class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        Deletes all duplicates from the given linked list and returns the modified linked list.

        :param head: The head node of the linked list.
        :type head: ListNode
        :return: The head node of the modified linked list.
        :rtype: ListNode
        """
        sentinel = ListNode(0, head)

        pred = sentinel
        
        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next

                pred.next = head.next 

            else:
                pred = pred.next 

            head = head.next
            
        return sentinel.next