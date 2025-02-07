from collections import Counter

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # first attempt
        for i in range(len(nums)):
            num = nums.pop(i)
            if num not in nums:
                return num
            else:
                nums[i] = num
        # this solution is O(n^2)

    def second_attempt(self, nums):
        count = Counter(nums)  # Count occurrences
        for num in count:
            if count[num] == 1:
                return num  # Return unique element

    def third_attempt(self, nums):
        result = 0
        for num in nums:
            result ^= num  # When a duplicate is found it is taken away from result using XOR
            print(result)
        return result
