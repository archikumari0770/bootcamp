def myPow(x: float, n: int) -> float:
    def calc(base, exp):
        if exp == 0: return 1.0
        half = calc(base, exp // 2)
        return half * half if exp % 2 == 0 else half * half * base

    res = calc(x, abs(n))
    return res if n >= 0 else 1.0 / res