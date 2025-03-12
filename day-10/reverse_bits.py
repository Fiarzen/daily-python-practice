class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        result = 0
        for _ in range(32):
            result = (result << 1) | (n & 1)  # Shift result left, add last bit of n
            n >>= 1  # Shift n right to process the next bit
        return result
