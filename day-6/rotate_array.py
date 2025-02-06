class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # first attempt
        n = len(nums)
        k = k % n  
        nums[:] = nums[-k:] + nums[:-k]

    def rotate_in_place(self, nums, k):
        n = len(nums)
        k = k % n  

        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start, end = start + 1, end - 1

        reverse(0, n - 1)
        print(nums)      
        reverse(0, k - 1)
        print(nums)      
        reverse(k, n - 1)
        print(nums)     
