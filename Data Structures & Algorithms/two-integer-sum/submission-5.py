class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for i in range(len(nums)):
            remainder = target - nums[i]
            dictionary[remainder] = i
        for j in range(len(nums)):
            if nums[j] in dictionary:
                other_idx = dictionary[nums[j]]
                if other_idx != j:
                    return [j, other_idx]