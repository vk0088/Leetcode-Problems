class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}
        for i in arr:
            if i in freq: freq[i] += 1
            else: freq[i] = 1
        
        duplicate = []
        for i in freq:
            if freq[i] in duplicate: return False
            duplicate.append(freq[i])
        
        return True