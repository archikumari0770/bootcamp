def isPowerOfFour(n: int) -> bool:
    # Must be a power of two and have its single '1' bit at an odd position (0x55555555 mask)
    return n > 0 and (n & (n - 1)) == 0 and (n & 0x55555555) != 0