# Insertion Sort:
### Input
- **x** as list of numbers to sort
### processes
1. define **x** as list
2. get **n** as the length of the items
3. read items from the user
4. for i starting for 1 to i < n
    1. val = x[i]
    2. for j starting from i-1 down to j >= 0
        - if val < x[j]
            - x[j+1] = x[j]
        - else
            - break the inside loop
        x[j+1] = val
5. print x
### Output
- sorted **x**