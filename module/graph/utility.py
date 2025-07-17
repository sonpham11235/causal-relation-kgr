import networkx as nx
import matplotlib.pyplot as plt

def new_directed_graph():
    """Create a new directed graph."""
    return nx.DiGraph()

def add_nodes(graph: nx.DiGraph, head: str, tail: str, weight: float = 1.0) -> nx.DiGraph:
    """Add nodes to the graph."""
    if (head not in graph.nodes):
        graph.add_node(head)
    if (tail not in graph.nodes):
        graph.add_node(tail)
    graph.add_edge(head, tail, weight)
    return graph

def visualize_graph(graph: nx.DiGraph, title: str = "Directed Graph") -> None:
    """Draw the directed graph."""
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=16, font_color='black', arrows=True)
    edge_labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    plt.title(title)
    plt.show()