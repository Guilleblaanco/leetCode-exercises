class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        arr = sorted(arr)
        diff = 0
        diff = arr[1] - arr[0]
        j = 1
        i = 0
        while j < len(arr):
            if diff != arr[j] - arr[i]:
                return False
            j+=1
            i+=1
        return True