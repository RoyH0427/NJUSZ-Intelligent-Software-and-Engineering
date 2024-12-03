import numpy as np
import pandas as pd
import scipy.sparse as sp
import heapq

def load_positions(file_path):
    data = pd.read_csv(file_path, sep='\t', header=None, names=["node", "x", "y", "is_anchor"])
    return data

def load_distances(file_path):
    data = pd.read_csv(file_path, sep='\t', header=None, names=["node1", "node2", "distance"])
    return data

# Dijkstra
def dijkstra(hop_matrix, start_node):
    num_nodes = hop_matrix.shape[0]
    distances = np.full(num_nodes, np.inf)
    distances[start_node] = 0
    priority_queue = [(0, start_node)]

    while priority_queue:
        current_dist, current_node = heapq.heappop(priority_queue)
        if current_dist > distances[current_node]:
            continue

        for neighbor in range(num_nodes):
            if hop_matrix[current_node, neighbor] != np.inf:
                distance = hop_matrix[current_node, neighbor]
                new_dist = current_dist + distance
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(priority_queue, (new_dist, neighbor))

    return distances

# DV-HOP
def dv_hop_positioning(positions, distances):
    # 计算每个锚节点之间的跳数
    anchors = positions[positions["is_anchor"] == 1].copy()
    nodes = positions.copy()
    num_nodes = len(nodes)
    hop_matrix = np.full((num_nodes, num_nodes), np.inf)
    np.fill_diagonal(hop_matrix, 0)

    # 构建跳数矩阵
    for _, row in distances.iterrows():
        node1, node2, dist = int(row["node1"] - 1), int(row["node2"] - 1), row["distance"]
        hop_matrix[node1, node2] = 1
        hop_matrix[node2, node1] = 1

    # 使用Dijkstra算法计算锚节点之间的最短跳数
    hop_counts = {}
    for anchor_idx in anchors["node"]:
        anchor_idx = int(anchor_idx) - 1
        hop_counts[anchor_idx] = dijkstra(hop_matrix, anchor_idx)

    # 计算平均每跳距离
    avg_hop_distances = {}
    for anchor_idx in anchors["node"]:
        anchor_idx = int(anchor_idx) - 1
        total_distance = 0
        total_hops = 0
        for other_anchor_idx in anchors["node"]:
            other_anchor_idx = int(other_anchor_idx) - 1
            if anchor_idx != other_anchor_idx and hop_counts[anchor_idx][other_anchor_idx] < np.inf:
                dist = np.sqrt((nodes.iloc[anchor_idx]["x"] - nodes.iloc[other_anchor_idx]["x"]) ** 2 +
                               (nodes.iloc[anchor_idx]["y"] - nodes.iloc[other_anchor_idx]["y"]) ** 2)
                hops = hop_counts[anchor_idx][other_anchor_idx]
                total_distance += dist
                total_hops += hops
        avg_hop_distances[anchor_idx] = total_distance / total_hops if total_hops > 0 else 0

    # 估算未知节点与锚节点之间的距离
    estimated_positions = []
    unknowns = positions[positions["is_anchor"] == 0].copy()
    for _, unknown in unknowns.iterrows():
        node_idx = int(unknown["node"] - 1)
        anchor_distances = []
        anchor_positions = []
        for anchor_idx in anchors["node"]:
            anchor_idx = int(anchor_idx) - 1
            hops = hop_counts[anchor_idx][node_idx]
            if hops < np.inf:
                anchor_distances.append(hops * avg_hop_distances[anchor_idx])
                anchor_positions.append([nodes.iloc[anchor_idx]["x"], nodes.iloc[anchor_idx]["y"]])

        # 使用最小二乘法估算未知节点位置
        if len(anchor_positions) >= 3:
            A = []
            b = []
            for i in range(1, len(anchor_positions)):
                x1, y1 = anchor_positions[0]
                x2, y2 = anchor_positions[i]
                d1 = anchor_distances[0]
                d2 = anchor_distances[i]
                A.append([2 * (x2 - x1), 2 * (y2 - y1)])
                b.append(d1 ** 2 - d2 ** 2 - x1 ** 2 + x2 ** 2 - y1 ** 2 + y2 ** 2)
            A = np.array(A)
            b = np.array(b)
            position = np.linalg.lstsq(A, b, rcond=None)[0]
            estimated_positions.append({"node": unknown["node"], "x": position[0], "y": position[1]})

    return pd.DataFrame(estimated_positions, columns=["node", "x", "y"])

# 计算 RMSE
def calculate_rmse(estimated_positions, true_positions):
    merged = pd.merge(estimated_positions, true_positions, on="node", suffixes=('_est', '_true'))
    rmse = np.sqrt(np.sum((merged["x_est"] - merged["x_true"]) ** 2 + (merged["y_est"] - merged["y_true"]) ** 2) / len(merged))
    return rmse

def main():
    positions = load_positions("net1_pos.txt")
    distances = load_distances("net1_topo_error_0.txt")

    located_positions = dv_hop_positioning(positions, distances)
    
    # 将所有未知节点的坐标保存到文件中
    located_positions["node"] = located_positions["node"].astype(int)
    located_positions.to_csv("DV-Hop_pos_error_0.txt", sep='\t', index=False, header=False)

    true_positions = positions[positions["is_anchor"] == 0][["node", "x", "y"]]
    rmse = calculate_rmse(located_positions, true_positions)
    print(f"RMSE: {rmse:.4f}")

if __name__ == "__main__":
    main()