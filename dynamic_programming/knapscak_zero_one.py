items = [
    {"name": "#1", "weight": 1, "profit": 4},
    {"name": "#2", "weight": 3, "profit": 9},
    {"name": "#3", "weight": 5, "profit": 12},
    {"name": "#4", "weight": 4, "profit": 11},
]
max_weight = 8
items.insert(0, {"name": "#0", "weight": 0, "profit": 0})
n = len(items)
dp: list[list[int]] = []
for i in range(n):
    dp.append([])
    for j in range(max_weight + 1):
        if i == 0 or j == 0:
            dp[i].append(0)
        elif items[i]["weight"] <= j:
            dp[i].append(
                max(
                    dp[i - 1][j], dp[i - 1][j - items[i]["weight"]] + items[i]["profit"]
                )
            )
        else:
            dp[i].append(dp[i - 1][j])
print(dp)
print(dp[n - 1][max_weight])
