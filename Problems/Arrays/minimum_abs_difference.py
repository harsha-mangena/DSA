class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        """
        Given an array of integers 'arr', returns a list of pairs with minimum absolute difference
        between them. Each pair is sorted in non-descending order. 
        
        Args:
        - arr: A list of integers
        
        Returns:
        - output: A list of lists of integers, representing the pairs with minimum absolute difference
        """
        arr.sort()
        minimum = 10**9
        output = list()
        for i in range(1, len(arr)):
            current_minimum = abs(arr[i]-arr[i-1])
            if current_minimum == minimum:
                output.append([arr[i-1], arr[i]])
            elif current_minimum < minimum:
                minimum = current_minimum
                output.clear()
                output.append([arr[i-1], arr[i]])
        return output
