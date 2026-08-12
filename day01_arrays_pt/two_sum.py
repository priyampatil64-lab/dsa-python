# 1. Two Sum
# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums, target):
        seen = {}                          # empty dictionary to remember numbers we've seen
        for i, num in enumerate(nums):     # i = index, num = value, at each step
            complement = target - num      # the number we'd need to reach target
            if complement in seen:         # have we already seen that number?
                return [seen[complement], i]   # yes! return both indices
            else:
                seen[num] = i              # no, so remember this number's index


if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2, 7, 11, 15], 9))   # [0, 1]
    print(sol.twoSum([3, 2, 4], 6))        # [1, 2]
    print(sol.twoSum([3, 3], 6))           # [0, 1]
