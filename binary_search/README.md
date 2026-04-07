# binary search
### Input
- **arr**: sorted array, **num**: number to find
### Processes

1. define **low** at the begining and **high** at the last
2. get the **midpoint** between low and high
3. while low <= high do the following
    - if mid == key then return midpoint
    - else if key > x[midpoint] then low = mid + 1 and contiune
    - if key < x[midpoint] then high = mid -1 and contiune
4. if loop ended and not found return -1
### Output
- num index if found or -1 if not found