from sklearn.metrics import average_precision_score

# 定义边缘
edges = [(0, 1), (0, 2), (0, 3), (4, 5), (4, 6), (4, 7), (8, 9), (8, 10), (8, 11)]

# 定义单个缺失边的情况和双缺失边的情况
true_missing_edges_single = [(0, 4)]
true_missing_edges_double = [(0, 4), (0, 8)]

# 初始化节点度数
node_degrees = [0] * 12

# 计算节点的度数
for edge in edges:
    node_degrees[edge[0]] += 1
    node_degrees[edge[1]] += 1

# 计算非邻接节点对的偏好依附分数
scores = []
labels_single = []
labels_double = []
for i in range(len(node_degrees)):
    for j in range(i+1, len(node_degrees)):
        if (i, j) not in edges and (j, i) not in edges:
            score = node_degrees[i] * node_degrees[j]
            scores.append(score)
            labels_single.append(1 if (i, j) in true_missing_edges_single or (j, i) in true_missing_edges_single else 0)
            labels_double.append(1 if (i, j) in true_missing_edges_double or (j, i) in true_missing_edges_double else 0)

# 计算单个缺失边的MAP
map_single = average_precision_score(labels_single, scores)

# 计算双缺失边的MAP
map_double = average_precision_score(labels_double, scores)

# 输出MAP值
print(f'MAP for single missing edge (0, 4): {map_single}')
print(f'MAP for double missing edges (0, 4) and (0, 8): {map_double}')
