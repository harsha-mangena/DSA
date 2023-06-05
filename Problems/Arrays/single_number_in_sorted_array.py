class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        """
        Finds and returns the single non-duplicate integer in a list of integers.

        Args:
            nums (list[int]): The list of integers to search.

        Returns:
            int: The single non-duplicate integer in the list.
        """
        left, right = 0, len(nums)-1
        while left < right:
            mid = int((left + right)/2)
            if (mid % 2 == 1 and nums[mid - 1] == nums[mid]) or (mid%2 == 0 and nums[mid] == nums[mid + 1]):
                left = mid + 1
            else:
                right = mid
        return nums[left]