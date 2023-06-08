class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        """
        Calculates the decimal value of a binary number represented by a linked list.

        :param head: The head of the linked list representing the binary number.
        :type head: ListNode
        :return: The decimal value of the binary number.
        :rtype: int
        """
        number = head.val
        while head.next:
            number = number*2 + head.next.val
            head = head.next 
        
        return number