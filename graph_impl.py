from pyparsing import Optional
from graph_interfaces import IEdge, IGraph, IVertex

# Edge implementation ---------------------------------------------------------#
class Edge(IEdge):
    def __init__(self, name: str, destination: IVertex, weight: float = 1.0):
        self._name = name
        self._destination = destination
        self._weight = weight

    def get_name(self) -> str:
        """Return the name/ID of the edge."""
        return self._name

    def set_name(self, name: str) -> None:
        """Set the name/ID of the edge."""
        self._name = name

    def get_destination(self) -> IVertex:
        """Return the destination vertex of the edge."""
        return self._destination

    def get_weight(self) -> float:
        """Return the weight of the edge."""
        return self._weight

    def set_weight(self, weight: float) -> None:
        """Set the weight of the edge."""
        self._weight = weight

# Vertex implementation -------------------------------------------------------#
class Vertex(IVertex):
    def __init__(self, name: str):
        """
        Vertex in a directed graph.
        :param name: Name/ID of the vertex
        """
        self._name = name
        self._edges = [] 
        self._visited = False

    def get_name(self) -> str:
        """Return the name/ID of the vertex."""
        return self._name

    def set_name(self, name: str) -> None:
        """Set the name/ID of the vertex."""
        self._name = name

    def add_edge(self, edge: IEdge) -> None:
        """Add an outgoing edge from this vertex."""
        self._edges.append(edge)

    def remove_edge(self, edge_name: str) -> None:
        """Remove an outgoing edge by name."""
        self._edges = [e for e in self._edges if e.get_name() != edge_name]

    def get_edges(self) -> list:
        """Return all outgoing edges from this vertex."""
        return self._edges

    def set_visited(self, visited: bool) -> None:
        """Set the visited flag for traversal algorithms."""
        self._visited = visited

    def is_visited(self) -> bool:
        """Return whether this vertex has been visited."""
        return self._visited

# Graph implementation --------------------------------------------------------#

class Graph(IGraph):
    def __init__(self):
        """
        Directed graph implementation.
        Vertices and edges are stored in dictionaries for fast lookup.
        """
        self._vertices = {}  
        self._edges = {}    

    def add_vertex(self, vertex: IVertex) -> None:
        """Add a vertex to the graph."""
        self._vertices[vertex.get_name()] = vertex

    def remove_vertex(self, vertex_name: str) -> None:
        """Remove a vertex and all its edges from the graph."""
        if vertex_name in self._vertices: del self._vertices[vertex_name]
        # Remove all edges that have this vertex as destination
        to_remove = [ename for ename, edge in self._edges.items()
        if edge.get_destination().get_name() == vertex_name]
        for ename in to_remove: del self._edges[ename]

    def add_edge(self, edge: IEdge) -> None:
        """Add an edge to the graph and to the source vertex."""
        self._edges[edge.get_name()] = edge

    def remove_edge(self, edge_name: str) -> None:
        """Remove an edge from the graph by name."""
        if edge_name in self._edges:
            del self._edges[edge_name]

    def get_vertices(self) -> list:
        """Return all vertices in the graph."""
        return list(self._vertices.values())

    def get_edges(self) -> list:
        """Return all edges in the graph."""
        return list(self._edges.values())
    
    def get_vertex(self, vertex_name: str) -> IVertex:
        """Return a vertex by name."""
        for v in self._vertices.values():
            if v.get_name() == vertex_name:
                return v
        raise ValueError(f"Vertex '{vertex_name}' not found")
    
    def get_neighbors(self, vertex: IVertex) -> list:
        """Return all neighboring vertices connected by outgoing edges."""
        neighbors = []
        for edge in vertex.get_edges():
            neighbors.append(edge.get_destination())
        return neighbors