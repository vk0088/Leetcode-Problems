class Solution {

    //Edge class for Adjacency list representation of graph
    public class Edge {
        int src;
        int dest;

        // Constructor for Edge class
        public Edge(int s, int d) {
            this.src = s;
            this.dest = d;
        }
    }

    // Method to create the graph from the given edges
    public void createGraph(ArrayList<Edge> graph[], int n, int[][] edges) {

        // Initialize adjacency list for each vertex
        for (int i = 0; i < n; i++) {
            graph[i] = new ArrayList<>();
        }

        // Add edges to the graph
        for (int i = 0; i < edges.length; i++) {
            int src = edges[i][0];
            int dest = edges[i][1];

            // Undirected Graph -> have to add edge in both directions
            graph[src].add(new Edge(src, dest)); 
            graph[dest].add(new Edge(dest, src)); 
        }
    }

    // Method to calculate the indegree of each vertex in the graph
    public void indeg(ArrayList<Edge> graph[], int indeg[]) {
        for (int i = 0; i < graph.length; i++) {
            for(int j = 0; j < graph[i].size(); j++){
                indeg[i]++;
            }
        }
    }
   
    public void removeLeaves(int n, ArrayList<Edge>[] graph, int[] indeg, List<Integer> ans) {
        Queue<Integer> q = new LinkedList<>();

        // Add leaf nodes (indegree 1) to the queue initially
        for (int i = 0; i < indeg.length; i++) {
            if (indeg[i] == 1) {
                q.add(i);
            }
        }
        
        while (n > 2) {
            int size = q.size();
            n -= size;

            for (int i = 0; i < size; i++) {
                int node = q.poll(); //leaf node

                // Update indegree of all adjacent nodes
                for(int k = 0; k < graph[node].size(); k++){

                    Edge e = graph[node].get(k);
                    indeg[e.dest]--;

                    // If the indegree becomes 1 after decrementing, add it to the queue
                    if (indeg[e.dest] == 1) {
                        q.add(e.dest);
                    }
                }
            }
        }

        // Answer
        while (!q.isEmpty()) {
            ans.add(q.poll());
        }
    }

    public List<Integer> findMinHeightTrees(int n, int[][] edges) {
        // Create Graph - Adjacency List
        ArrayList<Edge> graph[] = new ArrayList[n];

        // If there's only one node, it is the root of the tree
        if(n == 1){
            return Collections.singletonList(0);
        }

        createGraph(graph, n, edges);
        
        // Calculate the indegree of each vertex
        int indeg[] = new int[n];
        indeg(graph, indeg);

        //Answer List
        List<Integer> ans = new ArrayList<>();
        
        removeLeaves(n, graph, indeg, ans); 
        return ans;
    }
}
