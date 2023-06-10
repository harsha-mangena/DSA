class Solution:
    def mergeTwoLists(self, 
                      list1: Optional[ListNode], 
                      list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merge two sorted linked lists into a single sorted linked list and return it. 

        :param list1: Optional[ListNode], the head of the first linked list.
        :param list2: Optional[ListNode], the head of the second linked list.
        :return: Optional[ListNode], the head of the merged linked list.

        The function takes in two linked lists, both of which are sorted in non-descending order. 
        The function iterates through both lists and compares the values of the nodes at each 
        iteration. The smaller node is added to the output list and the iterator for that list is 
        incremented. This continues until all nodes of at least one list have been added to the 
        output list. The function then returns the head of the output list.
        """
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        root = dummy = ListNode(0)
        while list1 and list2:
            if list1.val < list2.val:
                dummy.next = list1
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next
            dummy = dummy.next
        dummy.next = list1 or list2
        return root.next