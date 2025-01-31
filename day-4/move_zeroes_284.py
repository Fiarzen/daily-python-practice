class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #  first attempt using additional list
        # list_2 = [i for i in nums if i != 0]
        # list_3 = [i for i in nums if i == 0]
        # solution = list_2 + list_3
        # print(solution)
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0 and nums[left] == 0:
                nums[left], nums[right] = nums[right], nums[left]

            if nums[left] != 0:
                left += 1


nums = [0, 1, 0, 3, 12]
sol = Solution()
sol.moveZeroes(nums)
print(nums)
