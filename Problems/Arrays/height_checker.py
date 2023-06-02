class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        """
        Given a list of integers `heights`, the function `heightChecker` 
        returns the number of indices `i` for which heights[i] != sortedHeights[i], 
        where sortedHeights is the sorted version of the input list.
        
        :param heights: A list of integers representing the heights of students.
        :type heights: list[int]
        :return: The number of students not standing in the correct positions.
        :rtype: int
        """
        count = 0
        for x,y in zip(heights, sorted(heights)):
            if x != y:
                count += 1
        return count
        