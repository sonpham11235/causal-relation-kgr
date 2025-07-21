from data.synthetic import utility, car_insurance
from module.graph import utility as graph_utility

gt = car_insurance.ground_truth()
adj_matrix = utility.adjacency_matrix_from_graph(gt)
cov_matrix = utility.generate_covariance_from_adjacency(adj_matrix)
joint_probability_data = utility.generate_joint_chi_squared_data(adj_matrix, df=2, n_samples=5)

with open("joint_probability_data.txt", "w") as f:
    for row in joint_probability_data:
        f.write(" ".join(map(str, row)) + "\n")