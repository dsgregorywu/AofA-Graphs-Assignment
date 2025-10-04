import csv
from typing import Optional
from graph_impl import Graph
from graph_interfaces import IGraph, IVertex, IEdge
from graph_impl import Vertex, Edge, Graph
file_path = "graph.txt"

def read_graph(file_path: str) -> Graph:
    graph = Graph()
    vertices = {}
    try:
        with open(file_path, "r") as f:
            reader = csv.reader(f)
            next(reader, None)  # Skip header
            for row in reader:
                if not row or len(row) < 4:  # Skip any row without all 4 values
                    continue
                source, destination, highway, distance = row
                print(source, destination, highway, distance)
                if not source.strip() or not destination.strip():
                    continue
                if source not in vertices:
                    vertices[source] = Vertex(source)
                    graph.add_vertex(vertices[source])
                if destination not in vertices:
                    vertices[destination] = Vertex(destination)
                    graph.add_vertex(vertices[destination])
                try:
                    edge = Edge(f"{source}->{destination}", vertices[destination], float(distance))
                except Exception as e:
                    print(f"Skipping edge due to error: {e}")
                    continue
                vertices[source].add_edge(edge)
                graph.add_edge(edge)
    # Handle errors and exceptions
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return graph
    except Exception as e:
        print(f"Error reading file: {e}")
        return graph
    return graph

def print_dfs(graph: Graph, start_vertex: IVertex) -> None: 
    """Print the DFS traversal of the graph starting from the start vertex"""
    visited = set()
    stack = [start_vertex]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            print("Visiting:", vertex.get_name())
            visited.add(vertex)
            # Add neighbors to stack in reverse order
            neighbors = list(graph.get_neighbors(vertex))
            for neighbor in reversed(neighbors):
                if neighbor not in visited:
                    stack.append(neighbor)
    print("DFS complete")
    print(" ")

def print_bfs(graph: Graph, start_vertex: IVertex) -> None: 
    """Print the BFS traversal of the graph starting from the start vertex"""
    visited = set()
    queue = [start_vertex]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            print("Visiting:", vertex.get_name())
            visited.add(vertex)
            for neighbor in graph.get_neighbors(vertex):
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)
    print("BFS complete")


def main() -> None:
    graph: IGraph = read_graph("graph.txt")
    start_vertex_name: str  = input("Enter the start vertex name: ")
    start_vertex: Optional[IVertex]= next((v for v in graph.get_vertices() if v.get_name() == start_vertex_name), None)
    if start_vertex is None:
        print("Start vertex not found")
        return
    print_dfs(graph, start_vertex)
    print_bfs(graph, start_vertex)


if __name__ == "__main__":
    main()