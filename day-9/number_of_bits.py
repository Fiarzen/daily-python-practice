class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            n &= (n - 1)  # Remove the rightmost set bit
            count += 1
        return count

    def optimised_hammingweight(self, n):

        return (self.lookup[n & 0xFF] +  
                self.lookup[(n >> 8) & 0xFF] +  
                self.lookup[(n >> 16) & 0xFF] +  
                self.lookup[(n >> 24) & 0xFF])  

    def bin_count(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count('1')
