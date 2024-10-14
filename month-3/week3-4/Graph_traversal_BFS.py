# Graph Traversal Using BFS
# Problem: Implement a graph traversal algorithm using Breadth-First Search (BFS). Represent the graph as an adjacency list.
# Objective: Practice BFS, a common graph traversal technique, to explore all nodes at the present depth level before moving on to nodes at the next depth level.


from collections import deque

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

    # Breadth-First Search (BFS) algorithm
    def bfs(self, start_vertex):
        visited = set()  # Set to track visited vertices
        queue = deque([start_vertex])  # Queue to manage BFS traversal
        visited.add(start_vertex)
        
        while queue:
            current_vertex = queue.popleft()  # Dequeue a vertex
            print(current_vertex, end=" ")  # Process the current vertex

            # Explore all adjacent vertices
            for neighbor in self.adjacency_list[current_vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

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

# Perform BFS starting from vertex 'A'
print("Breadth-First Search starting from vertex A:")
graph.bfs('A')
