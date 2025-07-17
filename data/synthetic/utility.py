import numpy as np
import random
import networkx as nx

def generate_covariance_from_adjacency(adj_matrix):
    n = adj_matrix.shape[0]
    cov_matrix = np.eye(n)
    for i in range(n):
        for j in range(i+1, n):
            if adj_matrix[i, j] == 1:
                cov_matrix[i, j] = 0.8
                cov_matrix[j, i] = 0.8
    return cov_matrix

def generate_joint_chi_squared_data(adj_matrix, df=2, n_samples=1000):
    n_vars = adj_matrix.shape[0]
    
    # Generate covariance matrix based on adjacency
    cov_matrix = generate_covariance_from_adjacency(adj_matrix)
    
    # Ensure it's positive definite (required for multivariate normal)
    eps = 1e-6
    cov_matrix += eps * np.eye(n_vars)

    # Generate multivariate normal samples
    mean = np.zeros(n_vars)
    normal_data = np.random.multivariate_normal(mean, cov_matrix, size=(df * n_samples))

    # Reshape and compute sum of squares (Chi-squared with df degrees)
    normal_data = normal_data.reshape(n_samples, df, n_vars)
    chi_squared_data = np.sum(normal_data ** 2, axis=1)  # shape: (n_samples, n_vars)

    return chi_squared_data

def correlation_heatmap(data):
    import seaborn as sns
    import matplotlib.pyplot as plt
    
    corr = np.corrcoef(data, rowvar=False)  # correlation between columns
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title('Correlation Between Variables')
    plt.show()

def adjacency_matrix_from_graph(graph: nx.DiGraph):
    """Convert a directed graph to an adjacency matrix."""
    nodes = list(graph.nodes)
    n = len(nodes)
    adj_matrix = np.zeros((n, n), dtype=int)
    
    for i, head in enumerate(nodes):
        for j, tail in enumerate(nodes):
            if graph.has_edge(head, tail):
                adj_matrix[i, j] = 1
    
    return adj_matrix