class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}                          # empty dictionary to remember numbers we've seen
        for i, num in enumerate(nums):     # i = index, num = value, at each step
            complement = target - num      # the number we'd need to reach target
            if complement in seen:         # have we already seen that number?
                return [seen[complement], i]   # yes! return both indices
            else:
                seen[num] = i              # no, so remember this number's index
