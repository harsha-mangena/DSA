class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        """
        Check if a given sentence is a pangram.
        
        :param sentence: A string representing the sentence to be checked.
        :type sentence: str
        
        :return: True if sentence is a pangram, False otherwise.
        :rtype: bool
        """
        arr = [0 for i in range(26)]
        for i in sentence:
            index = ord(i)-97
            arr[index] += 1
        
        for i in arr:
            if i==0:
                return False
        return True