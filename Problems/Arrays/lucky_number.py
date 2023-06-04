class Solution:
    def findLucky(self, arr: list[int]) -> int:
        """
        Finds the largest integer in the given list that occurs the same number of times as its value.
        
        Parameters:
        arr (list[int]): A list of integers to search for a lucky integer.
        
        Returns:
        int: The largest lucky integer found in the input list. Returns -1 if no lucky integer is found.
        """
        d = {}
        for i in arr:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        
        output = -1
        for k,v in d.items():
            if k == v:
                output = max(output, k)
        return output