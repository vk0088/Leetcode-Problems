class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meet = [[] for _ in range(n)] 
        meetings.sort(key=lambda x: x[2])
        meet[0].append((0, [firstPerson]))
        for a, b, t in meetings:
            if len(meet[a]) > 0 and meet[a][-1][0] == t:
                meet[a][-1][1].append(b)
            else:
                meet[a].append((t, [b]))
            if len(meet[b]) > 0 and meet[b][-1][0] == t:
                meet[b][-1][1].append(a)
            else:
                meet[b].append((t, [a]))
        knows = set()
        heap = [(0, 0)]
        while len(heap) > 0 and len(knows) < n:
            t, p = heappop(heap)
            if p in knows:
                continue
            knows.add(p)
            i = bisect_left(meet[p], (t, []))
            for nt, nps in meet[p][i:]:
                for np in nps:
                    if not np in knows:
                        heappush(heap, (nt, np))
        return list(knows)