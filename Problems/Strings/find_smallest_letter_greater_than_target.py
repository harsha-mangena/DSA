class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        """
        Given a list of lowercase sorted letters and a target letter, returns the smallest letter in the list that is larger than the target letter. If the target letter is greater than or equal to the last letter in the list, it returns the first letter in the list. 
        
        :param letters: A list of lowercase sorted letters. 
        :type letters: list[str]
        :param target: The target letter.
        :type target: str
        :return: The smallest letter in the list that is larger than the target letter or the first letter in the list if the target letter is greater than or equal to the last letter in the list.
        :rtype: str
        """
        for char in letters:
            if char > target:
                return char
        return letters[0]