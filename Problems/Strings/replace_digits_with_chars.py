class Solution:
    def replaceDigits(self, s: str) -> str:
        """
        Replaces every digit in a string s with a character whose ASCII value is the sum of the digit and the ASCII value of the character just before it. Returns the resulting string.

        :param s: A string containing the characters to be replaced
        :type s: str
        :return: The resulting string with replaced digits
        :rtype: str
        """
        ans = ''
        for i in range(len(s)):
            if(i & 1):
                asci = ord(s[i - 1]) + int(s[i])
                ans += chr(asci) 
            else:
                ans += s[i]
        return ans