"""
Link: https://leetcode.com/problems/running-sum-of-1d-array/
"""
class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        """
        Calculates the running sum of a given list of integers.

        :param nums: A list of integers.
        :type nums: list[int]
        :return: A new list of integers with the running sum.
        :rtype: list[int]
        """
        if nums is None or len(nums) == 1:
            return nums
        
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        
        return nums