from module.graph import utility

def ground_truth():
    """Create a directed graph for car insurance claims."""
    graph = utility.new_directed_graph()

    # nodes and edges
    graph = utility.add_nodes(graph, "Age", "GoodStudent")
    graph = utility.add_nodes(graph, "Age", "SocioEcon")
    graph = utility.add_nodes(graph, "Age", "RiskAversion")
    graph = utility.add_nodes(graph, "SocioEcon", "RiskAversion")
    graph = utility.add_nodes(graph, "SocioEcon", "GoodStudent")
    graph = utility.add_nodes(graph, "SocioEcon", "MakeModel")
    graph = utility.add_nodes(graph, "SocioEcon", "VehicleYear")
    graph = utility.add_nodes(graph, "RiskAversion", "VehicleYear")
    graph = utility.add_nodes(graph, "RiskAversion", "DrivQuality")
    graph = utility.add_nodes(graph, "MakeModel", "RuggedAuto")
    graph = utility.add_nodes(graph, "VehicleYear", "RuggedAuto")
    graph = utility.add_nodes(graph, "RuggedAuto", "ThisCarDam")
    graph = utility.add_nodes(graph, "DrivQuality", "Accident")
    graph = utility.add_nodes(graph, "Accident", "ThisCarDam")

    # visualize the graph
    utility.visualize_graph(graph, "Car Insurance Claims Graph")

def noisy():
    gt = ground_truth()
    """Create a noisy version of the ground truth graph."""
    return gt