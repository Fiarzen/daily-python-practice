import re

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cleaned_s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        left, right = 0, len(cleaned_s) - 1
        while left < right:
            if cleaned_s[left] != cleaned_s[right]:
                return False
            left += 1
            right -= 1
        return True
