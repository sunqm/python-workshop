1. Read the code below and rewrite it using only numpy functions (without for loop,
if-else statements). Benchmark your implementation. How much is it faster than
the naive python implementation? (hint: use np.isin)

```
def func1(names, db):
    idx = []
    for i in names:
        if i in db:
            idx.append(db.index(i))
    return idx
```

2. Use only numpy functions (without for loop, if-else statements) to find the
largest 3 distances between points if either points is inside the circle of
raidus r0. Then return these points. E.g.

```
>>> coordinates = np.array(
[[0.968, 0.313],
 [0.692, 0.876],
 [0.895, 0.085],
 [0.039, 0.17 ],
 [0.878, 0.098]]
)
>>> cirle_r0 = 0.9
>>> print(search_pairs(coordinates, cirle_r0))

# The indices of the relevant points in the original coordinates
[[2 1]
 [3 0]
 [3 1]]
```
