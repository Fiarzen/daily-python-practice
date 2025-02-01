class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    # first attempt
        # unique_elements = []
        # for i in nums:
        #     if i not in unique_elements:
        #         unique_elements.append(i)
        # nums = unique_elements
        # return len(nums)

        if not nums:
            return 0  # Edge case: empty list

            # Two-pointer technique
        k = 1  # Pointer to track unique elements
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:  # Found a new unique element
                nums[k] = nums[i]  # Place it at the correct position
                k += 1  # Move unique pointer forward

        return k  # Return the count of unique elements
