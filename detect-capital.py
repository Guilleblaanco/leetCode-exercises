#No funciona 
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        n = len(word)
        characters = list(map(lambda c: c, iter(word)))
        if word.isupper() == True:
            return True
        else:
            for i in range(0, n):
                if characters[0].isupper() and characters(i).islower():
                    return True
                elif word.islower():
                    return True
                else: return False

sol = Solution()
print(sol.detectCapitalUse('Hello'))





                
         