class Solution:
    def balancedStringSplit(self, s: str) -> int:
        """
        Computes the maximum number of balanced strings that can be formed from the given string s.
        
        :param s: A string of length n (1 ≤ n ≤ 10^4) containing only 'L' and 'R' characters.
        :return: An integer denoting the maximum number of balanced strings that can be formed.
        """
        stack, result = [], 0
                        
        for char in s:            
            if stack == []:
                stack.append(char)
                result += 1
            elif char == stack[-1]:
                stack.append(char)
            else:
                stack.pop()
                
        return result