from sklearn.metrics import roc_auc_score

# Define the edges of the graph
edges = [(0, 1), (0, 2), (0, 3), (4, 5), (4, 6), (4, 7), (8, 9), (8, 10), (8, 11)]

# Define the true missing edges
true_missing_edges = [(0, 4), (0, 8)]

# Initialize node degrees
node_degrees = [0] * 12  # Assuming the graph has 12 nodes, indexed from 0 to 11

# Calculate the degree of each node
for edge in edges:
    node_degrees[edge[0]] += 1
    node_degrees[edge[1]] += 1

# Calculate the preferential attachment score for each pair of non-adjacent nodes
scores = []
labels = []
for i in range(len(node_degrees)):
    for j in range(i+1, len(node_degrees)):
        if (i, j) not in edges and (j, i) not in edges:
            # The score is the product of the degrees
            score = node_degrees[i] * node_degrees[j]
            scores.append(score)
            # If the edge is a true missing edge, label it as 1, otherwise 0
            labels.append(1 if (i, j) in true_missing_edges or (j, i) in true_missing_edges else 0)

# Calculate AUC
auc = roc_auc_score(labels, scores)

# Output the AUC value
print(f'The AUC for the graph with the missing edges (0, 4) and (0, 8) is: {auc}')
