class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:

        if not dist or not speed:
            return 0
        
        time = [0] * len(dist)
        for i in range(len(dist)):
            time[i] = dist[i] / speed[i]

        time.sort()
        count = 0
        for i in range(len(time)):
            if time[i] <= i:
                break
            count += 1
        return count 