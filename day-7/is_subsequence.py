class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # first attempt
        x = ""
        for letter in t:
            if letter in s:
                x += letter
        print(x)
        if x == s:
            return True
        else:
            return False
    