class NaiveSolution:
    def does_exist(self, arr:list[int], target):
        """
        Binary search algorithm to determine if the target integer exists in the given array of integers.

        :param arr: A list of integers to search through.
        :param target: The integer to search for in the given array.
        :return: The index of the target integer in the given array if found, otherwise -1.
        """
        low = 0
        high = len(arr)-1

        while low<=high:
            mid = (low+high)//2
            if arr[mid]==target:
                return mid
            elif arr[mid]>target:
                high = mid-1
            else:
                low = mid+1
        return -1
    def checkIfExist(self, arr: list[int]) -> bool:
        """
        Given an array of integers, this function checks if there are any two numbers in
        the array such that one is the double of the other. Returns True if such a pair
        exists, otherwise False.
        
        :param arr: A list of integers.
        :type arr: list[int]
        :return: A boolean indicating whether a pair of numbers exists that satisfies the
                 given condition.
        :rtype: bool
        """
        arr.sort()
        for i in range(len(arr)):
            if i>0:
                exists = self.does_exist(arr, arr[i]*2)
                if exists!=-1 and i!=exists:
                    return True
        return False