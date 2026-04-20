labels = ["1", "2", "3", "4", "5", "6"]
graph = [
    [0, 6.7, 5.2, 2.8, 5.6, 3.6],
    [6.7, 0, 5.7, 7.3, 5.1, 3.2],
    [5.2, 5.7, 0, 3.4, 8.5, 4.0],
    [2.8, 7.3, 3.4, 0, 8, 4.4],
    [5.6, 5.1, 8.5, 8, 0, 4.6],
    [3.6, 3.2, 4, 4.4, 4.6, 0],
]
v = 6
selected = [False for _ in range(v)]
selected[0] = True
print(selected)
selected_edges_count = 0
final_tree_cost = 0
while selected_edges_count < v - 1:
    minimum_weight = float("inf")
    from_v = -1
    to_v = -1
    for i in range(v):
        if selected[i]:
            for j in range(v):
                if graph[i][j] > 0 and graph[i][j] < minimum_weight and not selected[j]:
                    minimum_weight = graph[i][j]
                    from_v = i
                    to_v = j
    selected_edges_count += 1
    final_tree_cost += minimum_weight
    print(f"{labels[from_v]} - {labels[to_v]}: {minimum_weight}")
    selected[to_v] = True
print(final_tree_cost)
