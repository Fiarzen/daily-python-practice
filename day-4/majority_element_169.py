class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # first attempt
        # count_1 = 0
        # count_2 = 0
        # num_1 = nums[0]
        # for num in nums:
        #     if num == num_1:
        #         count_1 += 1
        #     else:
        #         num_2 = num
        #         count_2 += 1
        # if count_1 > count_2:
        #     return num_1
        # else:
        #     return num_2
        most_common = None
        count = 0

        for num in nums:
            if count == 0:
                most_common = num
            count += 1 if num == most_common else -1
        return most_common

nums = [2,2,1,1,1,2,2]
sol = Solution()
print(sol.majorityElement(nums))

