import numpy as np
import pandas as pd
from scipy.optimize import least_squares

def load_positions(file_path):
    data = pd.read_csv(file_path, sep='\t', header=None, names=["node", "x", "y", "is_anchor"])
    return data

def load_distances(file_path):
    data = pd.read_csv(file_path, sep='\t', header=None, names=["node1", "node2", "distance"])
    return data

# 最小二乘法
def least_squares_position(anchors, distances):
    def residuals(vars, anchors, distances):
        x, y = vars
        res = []
        for (anchor_x, anchor_y), dist in zip(anchors, distances):
            res.append(((x - anchor_x) ** 2 + (y - anchor_y) ** 2) ** 0.5 - dist)
        return res

    initial_guess = np.mean(anchors, axis=0)
    result = least_squares(residuals, initial_guess, args=(anchors, distances))
    return result.x

# 迭代多边定位算法
def iterative_trilateration(positions, distances):
    anchors = positions[positions["is_anchor"] == 1].copy()
    unknowns = positions[positions["is_anchor"] == 0].copy()
    located_positions = []

    while not unknowns.empty:
        newly_located = []
        
        # 为每个未知节点计算相邻锚节点的数量和几何稳定性指标
        def evaluate_node(unknown):
            adj = distances[(distances["node1"] == unknown["node"]) | (distances["node2"] == unknown["node"])]
            adj = adj.copy()
            adj["anchor"] = adj.apply(lambda row: row["node2"] if row["node1"] == unknown["node"] else row["node1"], axis=1)
            anchor_subset = adj[adj["anchor"].isin(anchors["node"])]
            num_adj_anchors = len(anchor_subset)
            
            if num_adj_anchors >= 3:
                anchor_positions = anchors.set_index("node").loc[anchor_subset["anchor"], ["x", "y"]].values
                # 计算几何分布的稳定性
                centroid = np.mean(anchor_positions, axis=0)
                stability = np.std(np.linalg.norm(anchor_positions - centroid, axis=1))
                return num_adj_anchors, stability
            return num_adj_anchors, float('inf')  # 如果少于3个锚节点，不适合定位

        # 为每个未知节点计算相邻锚节点数量和几何稳定性
        unknowns[["num_adj_anchors", "stability"]] = unknowns.apply(lambda row: evaluate_node(row), axis=1, result_type="expand")

        # 按照相邻锚节点数量降序排列，若相同则按几何稳定性升序排列
        unknowns = unknowns.sort_values(by=["num_adj_anchors", "stability"], ascending=[False, True])

        for idx, unknown in unknowns.iterrows():
            # 获取与该未知节点相邻的锚节点及其距离
            adjacent = distances[(distances["node1"] == unknown["node"]) | (distances["node2"] == unknown["node"])]
            adjacent = adjacent.copy()
            adjacent["anchor"] = adjacent.apply(lambda row: row["node2"] if row["node1"] == unknown["node"] else row["node1"], axis=1)
            adjacent = adjacent[adjacent["anchor"].isin(anchors["node"])]

            if len(adjacent) >= 3:
                anchor_positions = anchors.set_index("node").loc[adjacent["anchor"], ["x", "y"]].values
                anchor_distances = adjacent["distance"].values
                # 使用加权最小二乘法定位该未知节点
                x, y = least_squares_position(anchor_positions, anchor_distances)
                # 更新锚节点集合
                anchors = pd.concat([anchors, pd.DataFrame([{"node": unknown["node"], "x": x, "y": y, "is_anchor": 1}])], ignore_index=True)
                newly_located.append(idx)
                located_positions.append({"node": unknown["node"], "x": x, "y": y})

        if not newly_located:
            print("No more nodes can be located. Exiting iteration.")
            break  # 如果本轮没有新定位的节点，退出迭代

        # 从未知节点集合中移除已定位的节点
        unknowns = unknowns.drop(newly_located)

    return pd.DataFrame(located_positions, columns=["node", "x", "y"])

# 计算 RMSE
def calculate_rmse(estimated_positions, true_positions):
    merged = pd.merge(estimated_positions, true_positions, on="node", suffixes=('_est', '_true'))
    rmse = np.sqrt(np.sum((merged["x_est"] - merged["x_true"]) ** 2 + (merged["y_est"] - merged["y_true"]) ** 2) / len(merged))
    return rmse

def main():
    positions = load_positions("net1_pos.txt")

    # 5%
    distances_5 = load_distances("net1_topo_error_5.txt")
    located_positions_5 = iterative_trilateration(positions, distances_5)

    # 10%
    distances_10 = load_distances("net1_topo_error_10.txt")
    located_positions_10 = iterative_trilateration(positions, distances_10)

    true_unknowns = positions[positions["is_anchor"] == 0][["node", "x", "y"]]
    rmse_5 = calculate_rmse(located_positions_5, true_unknowns)
    rmse_10 = calculate_rmse(located_positions_10, true_unknowns)

    print(f"RMSE for 5% error: {rmse_5:.4f}")
    print(f"RMSE for 10% error: {rmse_10:.4f}")

    # 将所有未知节点的坐标保存到文件中
    located_positions_5["node"] = located_positions_5["node"].astype(int)
    located_positions_10["node"] = located_positions_10["node"].astype(int)
    located_positions_5.to_csv("IL_pos_5.txt", sep='\t', index=False, header=False)
    located_positions_10.to_csv("IL_pos_10.txt", sep='\t', index=False, header=False)

if __name__ == "__main__":
    main()