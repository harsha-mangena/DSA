class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        Given a ransom note string and a magazine string, this function determines if the ransom note can be constructed
        from the magazine. The function returns a boolean indicating whether or not it is possible to construct the 
        ransom note using the characters in the magazine. The function takes two parameters: 
        ransomNote (str): a string representing the ransom note to be constructed
        magazine (str): a string representing the magazine from which the ransom note can be constructed

        Returns:
        bool: True if the ransom note can be constructed from the magazine, False otherwise.
        """
        store = {}

        for i in magazine:
            if i in store:
                store[i] += 1
            else:
                store[i] = 1
        
        for i in ransomNote:
            if i in store:
                store[i] -= 1
                if store[i] < 0:
                    return False
            else:
                return False
        
        return True