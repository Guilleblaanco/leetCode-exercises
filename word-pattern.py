class Solution:
    def wordPattern(self, pattern: str, word: str) -> bool:
        word = word.split(' ')
        pcnt = len(set(pattern))
        wcnt = len(set(word))
        
        if pcnt != wcnt or len(word) != len(pattern):
            return False
        
        return pcnt == len(set(zip(pattern, word)))