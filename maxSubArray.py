def maxSubArray(nums: list[int]) -> int:
    max_global = nums[0]
    max_local = max_global
    for i in range(1,len(nums)):
        max_local = max(nums[i],nums[i]+max_local)
        if max_local > max_global:
            max_global=max_local
    return max_global
            