class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        """
        Determines whether the given list of integers has any duplicates.

        :param nums: A list of integers to check for duplicates.
        :type nums: list[int]
        :return: True if the list contains any duplicates, False otherwise.
        :rtype: bool
        """
        duplicates = set()
        for i in nums:
            if i in duplicates:
                return True
            duplicates.add(i)
        return False