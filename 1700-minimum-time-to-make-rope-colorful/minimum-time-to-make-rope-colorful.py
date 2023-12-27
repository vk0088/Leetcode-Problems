class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        pq = []
        ans = 0
        i = 1
        while i < len(colors):
            if colors[i] == colors[i-1]:
                color = colors[i]
                j = i - 1
                while j < len(colors) and colors[j] == color:
                    heapq.heappush(pq, neededTime[j])
                    j += 1
                
                while len(pq) > 1:
                    ans += heapq.heappop(pq)
                
                heapq.heappop(pq)

                i = j
            else:
                i += 1
        return ans
