class QuickUnion:
    def __init__(self, size):
        self.root = [i for i in range(size)]

    def find(self, x):
        # Time O(H)
        while x != self.root[x]:
            x = self.root[x]
        return x

    def union(self, x, y):
        # Time O(H)
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            self.root[root_y] = root_x


    def connected(self, x, y):
        # Time O(H)
        return self.find(x) == self.find(y)

uf = QuickUnion(10) #[0,1,2,3,4,5,6,7,8,9]
uf.union(1,3)
uf.union(2,5)
print(uf.connected(1,3)) #True
print(uf.root) #[0, 1, 2, 1, 4, 2, 6, 7, 8, 9]

uf.union(1,5)
print(uf.connected(1,2)) #True
print(uf.root) #[0, 1, 1, 1, 4, 2, 6, 7, 8, 9]
