class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)
        max_len = 0
        curr_sum = 0
        
        # Initially, there's no sum 0, so we add it with index -1
        hashmap[0] = -1
        
        for i in range(len(nums)):
            # Convert 0 to -1, so when sum becomes 0, it indicates equal number of 0s and 1s
            curr_sum += 1 if nums[i] == 1 else -1
            
            if curr_sum in hashmap:
                # If current sum is already present in hashmap, update max_len
                max_len = max(max_len, i - hashmap[curr_sum])
            else:
                # Else, put the current sum in the hashmap
                hashmap[curr_sum] = i
        
        return max_len