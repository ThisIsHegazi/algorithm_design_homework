import pprint

labels = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
data = [
    [0, 2, 4, 3, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 7, 4, 6, 0, 0, 0],
    [0, 0, 0, 0, 3, 2, 4, 0, 0, 0],
    [0, 0, 0, 0, 4, 1, 5, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 4, 0],
    [0, 0, 0, 0, 0, 0, 0, 6, 3, 0],
    [0, 0, 0, 0, 0, 0, 0, 3, 3, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]
n = len(data)
states = [dict()] * n
states[-1] = {"from": "", "to": "J", "cost": 0}
# input:data and labels

for i in range(n - 2, -1, -1):
    curr_min = 10**10
    min_point = ""
    states[i] = {"from": labels[i], "to": "", "cost": curr_min}
    for j in range(i + 1, n):
        if data[i][j] == 0:
            continue
        new_cost = data[i][j] + states[j]["cost"]
        if new_cost < curr_min:
            curr_min = new_cost
            min_point = labels[j]
        states[i]["cost"] = curr_min
        states[i]["to"] = min_point

# print items with new lines in between
print("-" * 50)
pprint.pprint(states)
print("-" * 50)
print(f"Minimum Cost is: {states[0]['cost']}")
print("-" * 50)


path = ["A"]
for state in states:
    if state["from"] == path[-1]:
        path.append(state["to"])
print("route:")
print(path)
