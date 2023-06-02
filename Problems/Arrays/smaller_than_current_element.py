class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        """
        Returns a list of integers containing, for each element in the input list, the number of elements in the list that are smaller than it.
        
        :param nums: A list of integers.
        :type nums: list[int]
        :return: A list of integers containing the number of elements in the input list that are smaller than each element.
        :rtype: list[int]
        """
        temp = sorted(nums)
        
        result = [temp.index(i) for i in nums]

        return result