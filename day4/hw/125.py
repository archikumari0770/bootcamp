class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s1=s.lower()
        l=[]
        for i in s1:
            if i in ("abcdefghijklmnopqrstuvwxyz1234567890"):
                l.append(i)
            else:
                continue
        result = ''.join(l)
        n=len(result)
        result_final=result[::-1]
        for i in range(n):
            if result[i]==result_final[i]:
                continue
            else:
                return False
        return True 