class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_prod = [1] * n
        right_prod = [1] * n

        left_prod[1] = nums[0]
        for i in range(2, n):
            left_prod[i] = left_prod[i-1] * nums[i-1]


        right_prod[n-2] = nums[n-1]
        
        for j in range(n-3,-1, -1):
            right_prod[j] = right_prod[j+1] * nums[j+1]

        res = [1] * n
        for i in range(n):
            res[i] = left_prod[i] * right_prod[i]

        print(f"Left prod: {left_prod}")
        print(f"Right prod: {right_prod}")
        return res
