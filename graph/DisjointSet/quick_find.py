class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]

    def find(self, x):
        return self.root[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            for i in range(len(self.root)):
                if self.root[i] == root_y:
                    self.root[i] = root_x


    def connected(self, x, y):
        return self.find(x) == self.find(y)


uf = UnionFind(10)

uf.union(1,2)
uf.union(2,5)
print(uf.root) #[0, 1, 1, 3, 4, 1, 6, 7, 8, 9]
print(uf.connected(1,5)) #True

uf.union(3,7)
uf.union(7,2)
print(uf.root) #[0, 3, 3, 3, 4, 3, 6, 3, 8, 9]
print(uf.connected(1,7)) #True
print(uf.connected(0,7)) #False

