class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], 
                            l2: Optional[ListNode]) -> Optional[ListNode]:
        
        """
        Adds two linked lists, l1 and l2, and returns a new linked list that represents their sum.
        :param l1: The head of the first linked list.
        :type l1: Optional[ListNode]
        :param l2: The head of the second linked list.
        :type l2: Optional[ListNode]
        :return: The head of the new linked list representing the sum of l1 and l2.
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(-1)
        curnode = dummy
        #carry to take on next
        carry = 0
        while l1 or l2:
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0
            
            sum = val1+val2+carry
            newNode = ListNode(sum%10)
            curnode.next = newNode
            curnode = newNode
            carry = sum//10
            
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        if carry:
            newNode = ListNode(carry)
            curnode.next = newNode
        return dummy.next