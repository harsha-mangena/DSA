class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        """
        Finds the first palindrome string in a list of words.
        
        Args:
            words (list[str]): A list of strings to search for a palindrome.
        
        Returns:
            str: The first palindrome string found in the list, or an empty string if none is found.
        """
        for word in words:
            if word==word[::-1]:
                return word
        return ""