import heapq

class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        nums=list(set(nums))
        """
        Given a list of integers, returns the third distinct largest integer in O(nlogn) time complexity.

        Args:
            nums (list[int]): A list of integers.

        Returns:
            int: The third distinct largest integer if it exists, otherwise the maximum integer in the list.

        Example:
            >>> thirdMax([3,2,1])
            1

        Note:
            The input list may contain duplicates, and the algorithm should treat them as a single value.
        """
        if len(nums)<3:
            return max(nums)
        n=[-i for i in nums]
        heapq.heapify(n)
        for i in range(3):
            poping=heapq.heappop(n)
            if i==2:
                return -(poping)
            

           