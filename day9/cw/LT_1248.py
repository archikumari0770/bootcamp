def numberOfSubarrays(nums: list[int], k: int) -> int:
    def atMost(goal):
        left = count = res = 0
        for right in range(len(nums)):
            count += nums[right] % 2
            while count > goal:
                count -= nums[left] % 2
                left += 1
            res += right - left + 1
        return res
    return atMost(k) - atMost(k - 1)