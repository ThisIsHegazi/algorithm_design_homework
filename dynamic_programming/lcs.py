import pprint

text_01 = "HELLOWORLD"
text_02 = "OHELOD"
n = len(text_01)
m = len(text_02)
text_01 = f" {text_01}"
text_02 = f" {text_02}"
table = []
for i in range(m + 1):
    table.append([])
    for j in range(n + 1):
        if i == 0 or j == 0:
            table[i].append(0)
        elif text_02[i] == text_01[j]:
            table[i].append((table[i - 1][j - 1]) + 1)
        else:
            table[i].append(max(table[i][j - 1], table[i - 1][j]))
string = ""
i = m
j = n
while i > 0 and j > 0:
    if table[i][j] > table[i][j - 1]:
        if table[i - 1][j] == table[i][j]:
            i -= 1
        else:
            string = f"{text_02[i]}{string}"
            i -= 1
            j -= 1
    else:
        j -= 1
print(string)

print("-" * 50)
pprint.pprint(table)
pprint.pprint(table[-1][-1])
