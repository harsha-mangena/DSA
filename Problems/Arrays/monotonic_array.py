class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        """
        Determines if the given list of integers is monotonic, i.e. either entirely non-increasing or non-decreasing.
        
        :param nums: A list of integers to be checked.
        :type nums: list[int]
        
        :return: A boolean value indicating whether the given list is monotonic or not.
        :rtype: bool
        """
        #Base Condition
        if not len(nums):
            return 0

        incre = decre = True
        for i in range(1, len(nums)):
            if nums[i-1]>nums[i]:
                incre = False
            elif nums[i-1]<nums[i]:
                decre = False
        return incre or decre