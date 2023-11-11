class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        # set up a graph as a dict of dicts 
        self.graph = collections.defaultdict(dict)
        # for edge in edges 
        for edge in edges : 
            # get src, dst, cost and assign 
            src, dst, cost = edge 
            self.graph[src][dst] = cost 

        # set self edge to 0 
        for i in range(n) : 
            self.graph[i][i] = 0 

        # set up a shortest paths dict while in between edge assignments 
        self.shortest_paths = dict()

    def addEdge(self, edge: List[int]) -> None:
        # update and reset shortest paths. 
        src, dst, cost = edge 
        self.graph[src][dst] = cost 
        self.shortest_paths = dict()

    def shortestPath(self, node1: int, node2: int) -> int:
        # if memoized, utilize memo 
        if (node1, node2) in self.shortest_paths : 
            return self.shortest_paths[(node1, node2)]
        else : 
            # get n as graph keys size current 
            n = len(self.graph.keys())
            # build a pq 
            pq = [(0, node1)]
            # set costs to inf and base to 0 
            cost_for_node = [inf] * n 
            cost_for_node[node1] = 0 

            # while you have a priority queue 
            while pq : 
                # pop cost and node from heap 
                cost, node = heapq.heappop(pq)
                # if cost is greater than current recorded -> continue 
                # otherwise if equal or lesser and at end return based on result (priority queue assures lowest cost) 
                if cost > cost_for_node[node] : 
                    continue 
                elif node == node2 : 
                    update = -1 if cost == inf else cost 
                    # memoize the result first though 
                    self.shortest_paths[(node1, node2)] = update
                    return update
                else : 
                    # otherwise, for each neighbor of node get travel cost 
                    for neighbor in self.graph[node] : 
                        travel_cost = self.graph[node][neighbor] 
                        # calculate new cost 
                        new_cost = cost + travel_cost 
                        # if improvement, update and heap 
                        if new_cost < cost_for_node[neighbor] : 
                            cost_for_node[neighbor] = new_cost 
                            heapq.heappush(pq, (new_cost, neighbor))
            # never found never will, not reachable currently 
            self.shortest_paths[(node1, node2)] = -1
            # return -1 
            return -1 

# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)