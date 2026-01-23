# say elements in sets are {1,2,...,n}
class DSU:
    def __init__(self, n = 10):
        self.n = n
        self.R = [0] * (n+1) # representatives of sets, R[i] = representative of set containing i (i's rep)
    def make_set(self, x):
        self.R[x] = x

    def find_set(self, x):
        return self.R[x]
    
    def union(self, x, y):
        for i in range(1, self.n+1):
            if self.R[i] == self.R[x]:
                self.R[i] = self.R[y]
    
d = DSU(16)
for i in range(1,17):
    d.make_set(i)
for i in range(1, 16, 2):
    d.union(i, i+1)
for i in range(1, 14, 4):
    d.union(i, i+2)

d.union(1, 5)
d.union(11, 13)
d.union(1, 10)
print(d.find_set(2))
print(d.find_set(9))



