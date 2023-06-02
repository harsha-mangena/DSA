class Solution:
    def arraySign(self, nums: list[int]) -> int:
        """
        Returns the sign of the product of all the non-zero elements of the input list 'nums'. 
        The function takes a list of integers as input and returns an integer as output. If 
        the product is negative, returns -1, if positive, returns 1, and if zero, returns 0.
        
        :param nums: A list of integers.
        :type nums: List[int]
        :return: An integer representing the sign of the product of all non-zero elements of nums.
        :rtype: int
        """
        neg_count = 0
        for i in nums:
            if i == 0:
                return 0
            elif i < 0:
                neg_count += 1
        
        return 1 if (neg_count%2 == 0 or neg_count == 0) else -1 