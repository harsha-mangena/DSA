class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        """
        Shuffle function takes in two parameters, a list of integers and an integer 'n'.
        The function returns a list of integers. The function stores the values of the first
        'n' integers and the next 'n' integers alternatively in another array and returns
        the array.
        Parameters:
            nums (list[int]): A list of integers to be shuffled.
            n (int): An integer used for shuffling the list.
        Returns:
            res (list[int]): A list of shuffled integers.
        """
        i=0
        j=n
        res=[]

        while(i<n):
            res.append(nums[i])
            res.append(nums[j])
            i+=1
            j+=1
        return res