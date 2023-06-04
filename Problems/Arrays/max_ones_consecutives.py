class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        """
        Given a list of integers nums, returns the maximum number of consecutive 1's in the list.
        :param nums: A list of integers.
        :type nums: list[int]
        :return: The maximum number of consecutive 1's in the list.
        :rtype: int
        """
        max_ones = -10**9
        count = 0 
        for i in nums:
            if i==1:
                count += 1
            else:
                count = 0
            max_ones = max(max_ones, count)
        return max_ones