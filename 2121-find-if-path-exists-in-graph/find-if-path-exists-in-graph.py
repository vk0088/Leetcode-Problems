from collections import defaultdict

class Solution(object):

    def DFSUtil(self, adj, source, destination, visited):
        visited[source] = True
        for node in adj[source]:
            if node == destination:
                return True
            if visited[node] == False:
                if self.DFSUtil(adj,node,destination, visited):
                    return True
        return False

    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        if source == destination:
            return True

        adj = defaultdict(list)
        visited = defaultdict(bool)

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        return self.DFSUtil(adj,source,destination,visited)




        