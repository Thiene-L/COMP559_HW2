from sklearn.metrics import roc_auc_score
import numpy as np

# Define the degree of each node for the graph
# Here we first initialize the degree of all nodes to 0
node_degrees = np.zeros(12, dtype=int)

# Define the edges of the graph
edges = [(0, 1), (0, 2), (0, 3), (4, 5), (4, 6), (4, 7), (8, 9), (8, 10), (8, 11)]

# Update the degree of a node based on its edges
for edge in edges:
    node_degrees[edge[0]] += 1
    node_degrees[edge[1]] += 1

# Define a function that computes preference attachment scores
def calculate_scores(node_degrees, edges):
    n = len(node_degrees)
    scores = {}
    for i in range(n):
        for j in range(i + 1, n):
            if (i, j) not in edges and (j, i) not in edges:
                # 计算偏好依附分数
                score = node_degrees[i] * node_degrees[j]
                scores[(i, j)] = score
    return scores

# Calculate the preference attachment score of non-edges
non_edge_scores = calculate_scores(node_degrees, edges)

# Define true missing edges
true_edges = [(0, 4)]  # (0, 4) 是真实缺失的边

# Generate label and score arrays for ROC AUC calculation
y_true, y_scores = [1 if edge in true_edges else 0 for edge in non_edge_scores], list(non_edge_scores.values())

# Calculate AUC
auc = roc_auc_score(y_true, y_scores)

# Output AUC
print(f'The AUC for the graph with the missing edge (0, 4) is: {auc}')