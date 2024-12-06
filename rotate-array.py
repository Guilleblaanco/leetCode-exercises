class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        if k > 0:
            for i in range(0,k):
                nums.insert(0,nums[-1])
                del nums[-1]
        else: pass
