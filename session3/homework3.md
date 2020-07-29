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
largest N distances between points if either points is inside the circle of
raidus r0. Then return the coordinates of these points. 
