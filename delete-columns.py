class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        for i in strs:
            if strs[0][i] != sorted(strs[0][i], key=str.lower):
                strs.remove(strs[0][i])
        print(len(strs))

                



sol = Solution()
print(sol.minDeletionSize(["abc", "bce", "cae"]))