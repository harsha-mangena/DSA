class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Check if two strings are anagrams of each other.

        Args:
            s (str): The first string to be compared.
            t (str): The second string to be compared.

        Returns:
            bool: True if the strings are anagrams, False otherwise.
        """
        #Base Condition
        if len(s) != len(t):
            return False
        #return sorted(s) == sorted(t)
        d={}
        for i in s:
            try:
                if d[i]:
                    d[i]+=1
            except:
                d[i]=1
        for i in t:
            try:
                if d[i]:
                    d[i]-=1
            except:
                return False
        for k,v in d.items():
            if v!=0:
                return False
        return True
            
        