from heapq import heappop, heappush

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        connections = [set() for _ in range(n)]
        prices = {}
        for from_, to, price in flights:
            connections[from_].add(to)
            prices[from_, to] = price

        visited = [n] * n  # Visited cities in the least amount of stops

        seen = [(0, 0, src)]
        while seen:
            cost, stops, city = heappop(seen)

            # Done?
            if city == dst:
                return cost

            # Only visit a city if it's unvisited or if you're visiting it in fewer stops
            if stops >= visited[city]:
                continue
            visited[city] = stops

            # We can only go directly to the destination if we've reached the maximum number of stops
            if stops == k:
                if dst in connections[city]:
                    heappush(seen, (cost + prices[city, dst], stops, dst))
                continue
            stops += 1

            # Add valid connections
            for next_city in connections[city]:
                if stops >= visited[next_city]:
                    continue
                new_cost = cost + prices[city, next_city]
                heappush(seen, (new_cost, stops, next_city))
        return -1