class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        """
        Reverses the letters in a given string, while keeping the non-letter characters in place. 
        :param s: A string to reverse the letters of.
        :type s: str
        :return: The string s with its letters reversed and all other characters in their original place.
        :rtype: str
        """
        s = list(s.strip())
        i,j = 0, len(s)-1

        while i<j:
            if not s[i].isalpha():
                i+=1
                continue
            if not s[j].isalpha():
                j-=1
                continue
            s[i], s[j] = s[j],s[i]

            i+=1
            j-=1

        return ''.join(s)