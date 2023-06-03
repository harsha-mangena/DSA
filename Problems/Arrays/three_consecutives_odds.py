class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        """
        Determines whether there are three consecutive odd integers in the given list.
        
        :param arr: A list of integers to search for three consecutive odd integers.
        :type arr: list[int]
        :return: A boolean indicating whether there are three consecutive odd integers in the given list.
        :rtype: bool
        """
        stack = []
        for i in arr:
            if len(stack) == 3:
                return True
            elif stack is None or i%2!=0:
                stack.append(i)
            else:
                stack = []
        
        return len(stack) == 3