class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        for i in range(0,n):
            nums[i] = pow(nums[i],2)
        return sorted(nums)
