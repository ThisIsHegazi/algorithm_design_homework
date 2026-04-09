def segregate(arr):
    n = []
    p = []
    for i in arr:
        if i < 0:
            n.append(i)
        else:
            p.append(i)
    i = j = k = 0
    for i in range(len(n)):
        arr[k] = n[i]
        k += 1
    for j in range(len(p)):
        arr[k] = p[j]
        k += 1


lst = [6, -5, 12, 10, -9, -1]
print(lst)
segregate(lst)
print(lst)
