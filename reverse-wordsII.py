class Solution:
    def reverseWords(self, s: str) -> str:
        sliced = s.split(" ")
        b=0
        while b < len(sliced):
            sliced[b] = sliced[b][::-1]
            b+=1
        return ' '.join(sliced) 