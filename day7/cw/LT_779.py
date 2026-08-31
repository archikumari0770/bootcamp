def kthGrammar(n: int, k: int) -> int:
    if n == 1: return 0
    parent = kthGrammar(n - 1, (k + 1) // 2)
    is_odd = k % 2 == 1
    return parent if is_odd else 1 - parent