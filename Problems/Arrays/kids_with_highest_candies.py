class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        """
        Given a list of candies, and an extra amount of candies, this function
        returns a list of booleans indicating if each kid can have the greatest
        number of candies after adding the extra candies or not. It takes two
        parameters:
        
        - candies: A list of integers indicating the number of candies each kid
          has initially.
        
        - extraCandies: An integer representing the number of extra candies that
          can be added to each kid's candies.
          
        The function returns a list of booleans, where each boolean indicates
        whether the corresponding kid can have the greatest number of candies
        or not.
        """
        max_candies = max(candies)
        result = []

        for i in candies:
            if i+extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)
        
        return result
