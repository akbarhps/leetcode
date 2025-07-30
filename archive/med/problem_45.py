from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1: return 0
        if nums[0] >= len(nums): return 1

        counter = 0
        index = 0
        while index < len(nums):
            curnum = nums[index]

            maxnextnum = -1
            nextindex = -1
            for i in range(index + 1, min(index + 1 + curnum, len(nums))):
                nextnum = nums[i]
                if i == len(nums) - 1:
                    nextindex = len(nums)
                    break
                if nextnum + i >= maxnextnum + nextindex or nextnum + i >= len(nums):
                    maxnextnum = nextnum
                    nextindex = i

            index = nextindex
            counter += 1

            if nextindex >= len(nums):
                break

        return counter


# nums = [3, 4, 3, 2, 5, 4, 3]
# print(Solution().jump(nums))

nums = [1, 1, 1, 1, 1]
print(Solution().jump(nums))

nums = [2, 1, 1, 3, 4]
print(Solution().jump(nums))
