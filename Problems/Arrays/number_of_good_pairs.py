"""
Link: https://leetcode.com/problems/number-of-good-pairs/
"""
class Solution:
    def _naive(self, nums: list[int]) -> int:
        count = 0
        n = len(nums)
        if nums is None or len(nums) == 1:
            return count

        for i in range(n):
            for j in range(i+1, n):
                if nums[i] == nums[j]:
                    count += 1
        return count
    
    def numIdenticalPairs(self, nums: list[int]) -> int:
        """
        Given a list of integers nums, this function returns the count of all the 
        pairs (i, j) such that i < j and nums[i] == nums[j]. 
        
        Args:
        - nums: a list of integers
        
        Returns:
        - An integer representing the count of all the pairs
        
        Example:
        numIdenticalPairs([1,2,3,1,1,3])
        Output: 4
        """
        d = {}
        count = 0
        for i in range(len(nums)):
            if nums[i] in d:
                if d[nums[i]][-1] < i:
                    count += len(d[nums[i]])
                d[nums[i]].append(i)
            
            else:
                d[nums[i]] = [i]
        return count