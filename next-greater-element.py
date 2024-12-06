class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        i = 0
        arr = []
        while i < len(nums1):
            for j in range(0, len(nums2)):
                if nums1[i] == nums2[j]:
                    if j+1 >= len(nums2):
                        arr.append(-1)
                    elif nums2[j+1] > nums2[j]:
                        arr.append(nums2[j+1])
                    else: arr.append(-1)
            i+=1
        return arr