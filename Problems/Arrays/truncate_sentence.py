class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        """
        Given a string 's' and an integer 'k', the function truncates the string 
        's' to 'k' words and returns the truncated string. 

        :param s: A string to be truncated.
        :type s: str
        :param k: An integer representing the number of words to be kept in the 
            truncated string.
        :type k: int

        :return: A string containing the first 'k' words of the original string.
        :rtype: str
        """
        s = s.split(' ')
        return ' '.join(s[:k])