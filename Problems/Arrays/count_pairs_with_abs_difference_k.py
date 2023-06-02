class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        """
        Given a list of integers 'nums' and an integer 'k', this function calculates the number of pairs (i, j) where i and j are distinct indices in nums and nums[i] - nums[j] == k.

        :param nums: A list of integers.
        :type nums: List[int]
        :param k: An integer value.
        :type k: int
        :return: An integer value representing the count of pairs (i, j) where i and j are distinct indices in nums and nums[i] - nums[j] == k.
        :rtype: int
        """
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        c=0
        for i in nums:
            b=(i-k)
            if b in d:
                c+=d[b]
        return c
                