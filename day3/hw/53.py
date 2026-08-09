class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #using kadane's algo
        curr=nums[0]
        maxi=nums[0]
        n=len(nums)
        for i in range(1,n):
            curr=max(nums[i],nums[i]+curr)
            maxi=max(maxi,curr)
        return maxi