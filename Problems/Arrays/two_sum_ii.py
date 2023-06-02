class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        """
        Given a list of integers `numbers` and a target integer `target`, returns a list containing the indices of the two numbers in `numbers` whose sum is equal to `target`. The list is 1-indexed.

        Args:
            numbers (List[int]): A list of integers
            target (int): Target integer

        Returns:
            List[int]: A list containing the indices of the two numbers in `numbers` whose sum is equal to `target`. The list is 1-indexed. If such numbers do not exist, [-1,-1] is returned.
        """
        low = 0
        high = len(numbers)-1

        while low<=high:
            if numbers[low]+numbers[high] == target:
                return [low+1, high+1]

            elif numbers[low]+numbers[high] < target:
                low += 1

            else:
                high -= 1
        return [-1, -1]