class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        """
        Returns a list of indices of the target integer in the input list after sorting it.

        :param nums: A list of integers to be sorted and searched.
        :type nums: list[int]
        :param target: An integer to be searched in the input list.
        :type target: int
        :return: A list of integers representing the indices of the target in the input list.
        :rtype: list[int]
        """
        nums.sort()
        output = []
        for i in range(len(nums)):
            if nums[i] == target:
                output.append(i)
        return output
        