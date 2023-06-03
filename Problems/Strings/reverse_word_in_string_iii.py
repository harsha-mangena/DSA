class Solution:
    def reverseWords(self, s: str) -> str:
        """
        Reverses each word in a given string and returns the modified string.

        :param s: A string consisting of words separated by spaces.
        :type s: str
        :return: The modified string with each word reversed.
        :rtype: str
        """
        s =list(s.split(" "))
        output = ""
        for word in s:
            output += word[::-1]
            output += " "
        return output.rstrip(" ")
        
        