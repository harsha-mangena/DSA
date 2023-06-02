class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        """
        Determines if the number of occurrences of each element in the input list is unique.

        :param arr: A list of integers.
        :type arr: list[int]
        :return: True if the number of occurrences of each element is unique, False otherwise.
        :rtype: bool
        """
        num_store = {}
        for i in arr:
            try:
                if num_store[i]:
                    num_store[i] += 1
            except:
                num_store[i] = 1
        
        return len(num_store.values()) == len(set(num_store.values()))