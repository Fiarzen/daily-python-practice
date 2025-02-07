class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # first attempt
        for x in range(len(min(strs, key=len))):
            char = strs[0][x]
            for i in range(len(strs)):
                if x >= len(strs[i]) or strs[i][x] != char:
                    return strs[0][:x]
        return min(strs, key=len)

    def alternative_solution(self, strs):
        prefix = strs[0]

        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix
