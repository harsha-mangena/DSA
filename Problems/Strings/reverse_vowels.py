class Solution:
    def reverseVowels(self, s):
        """
        Reverses the positions of the vowels in a given string.
        
        :param s: a string to be processed.
        :type s: str
        :return: a string with the vowels reversed.
        :rtype: str
        """
        vowel = 'AEIOUaeiou'
        s = list(s)
        i,j = 0, len(s)-1
        while i<j:
            while s[i] not in vowel and i<j:
                i = i + 1
            while s[j] not in vowel and i<j:
                j = j - 1
            s[i], s[j] = s[j], s[i]
            i, j = i + 1, j - 1
        return ''.join(s)