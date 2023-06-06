class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        """
        Builds an array based on the given list of integers.

        :param nums: A list of integers used to build the array.
        :type nums: list[int]
        :return: A list of integers that represents the built array.
        :rtype: list[int]
        """
        output = [-1]*len(nums)
        for i in range(len(nums)):
            output[i] = nums[nums[i]]
        return output
        
        