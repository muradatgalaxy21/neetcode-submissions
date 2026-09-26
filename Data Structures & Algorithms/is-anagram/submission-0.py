class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictAnagram = {}  
        if len(s) == len(t):
            for i,j in zip(s,t):
                dictAnagram[i] = dictAnagram.get(i, 0) + 1
                dictAnagram[j] = dictAnagram.get(j, 0) - 1
            return all(value == 0 for value in dictAnagram.values())
        else:
            return False
    
        