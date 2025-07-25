class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        maxgap = 0

        for i, num in enumerate(nums):
            if i == 0: continue
            maxgap = max(maxgap, abs(num - nums[i-1]))
        
        return maxgap
            
