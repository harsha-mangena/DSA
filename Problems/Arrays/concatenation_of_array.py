"""
Link: https://leetcode.com/problems/concatenation-of-array
"""
class Solution:
    
    def naive(self, nums: list[int]) -> list[int]:
        n =  len(nums)
        for i in range(n):
            nums.append(nums[(i+n)%n])
        return nums
    def getConcatenation(self, nums: list[int]) -> list[int]:
        """
        Returns a list containing the concatenation of the input list with itself.
        
        :param nums: A list of integers.
        :type nums: list[int]
        
        :return: A list of integers representing the concatenation of the input list with itself.
        :rtype: list[int]
        """
        nums += nums
        return nums
        