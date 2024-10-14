# Graph Traversal Using DFS
# Problem: Implement a graph traversal algorithm using Depth-First Search (DFS). Represent the graph as an adjacency list.
# Objective: Understand DFS, which explores as far as possible along a branch before backtracking.

# Class representing a graph using an adjacency list
class Graph:
    def __init__(self):
        self.adjacency_list = {}

    # Add a vertex to the graph
    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    # Add an edge between two vertices (undirected graph)
    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)

    # Depth-First Search (DFS) algorithm
    def dfs(self, start_vertex):
        visited = set()  # Set to track visited vertices
        self._dfs_recursive(start_vertex, visited)

    # Recursive helper method for DFS
    def _dfs_recursive(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=" ")  # Process the current vertex

        # Explore all adjacent vertices
        for neighbor in self.adjacency_list[vertex]:
            if neighbor not in visited:
                self._dfs_recursive(neighbor, visited)

# Example Usage
graph = Graph()

# Adding vertices to the graph
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')
graph.add_vertex('E')

# Adding edges to form the graph
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'D')
graph.add_edge('C', 'E')
graph.add_edge('D', 'E')

# Perform DFS starting from vertex 'A'
print("Depth-First Search starting from vertex A:")
graph.dfs('A')
