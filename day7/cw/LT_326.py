def isPowerOfThree(n: int) -> bool:
    # 3^19 = 1162261467 is the largest power of 3 fitting in a signed 32-bit integer
    return n > 0 and 1162261467 % n == 0