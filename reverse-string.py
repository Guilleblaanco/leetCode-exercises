class Solution:
    def reverseString(self, s: list[str]) -> None:
        a=int(len(s)/2)
        b=len(s)-1
        for i in range(0,a):
            s[i],s[b]=s[b],s[i]
            b-=1