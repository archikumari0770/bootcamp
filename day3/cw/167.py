class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        lower=0
        higher=n-1
        for i in range(n):
            if numbers[lower]+numbers[higher]==target:
                return lower+1,higher+1
            elif numbers[lower]+numbers[higher]>target:
                higher=higher-1
                continue
            elif  numbers[lower]+numbers[higher]<target:
                lower=lower+1
                continue
            
        

