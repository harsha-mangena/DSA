class Solution:
    def maxPower(self, s: str) -> int:
        """
        Finds the length of the longest consecutive substring of a given string that 
        contains only one character.
        
        Args:
            s (str): The input string.
            
        Returns:
            int: The length of the longest consecutive substring of a given string that 
            contains only one character.
        """
        prev_char = s[0]
        current_max = max_count = 1

        for i in s[1:]:
            if i==prev_char:
                current_max += 1
                max_count = max(max_count, current_max)

            elif prev_char != i:
                prev_char = i
                current_max = 1
        
        return max_count