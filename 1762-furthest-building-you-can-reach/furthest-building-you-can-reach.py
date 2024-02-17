class Solution:
    def furthestBuilding(self, ht: List[int], bricks: int, ladders: int) -> int:
        heap = []
        for i in range(len(ht)-1):
            diff = ht[i+1] - ht[i]
            if diff <=0: continue
            heappush(heap, diff)
            if len(heap) > ladders:
                bricks -= heappop(heap)
                if bricks < 0: return i
        return len(ht)-1