class unionFind():
	def __init__(self, size):
		self.root = [i for i in range(size)]
		self.rank = [1] * size # height of the tree 
	
	def find(self, x):
		if x == self.root[x]:
			return x
		self.root[x] = self.find(self.root[x])
		
		return self.root[x]	
	def union(self, x, y):
		root_x = self.find(self.root[x])
		root_y = self.find(self.root[y])
		
		if root_x != root_y:
			if self.rank[root_x] > self.rank[root_y]:
				self.root[root_y] = root_x	
			elif self.rank[root_x] < self.rank[root_y]:
				self.root[root_x] = root_y
			else:			 	
				self.root[root_y] = root_x
				self.rank[root_x] += 1
	
	def connected(self, x, y):
		return self.find(x) == self.find(y)

# Test Case
print("-------------New-------------")
uf = unionFind(10)
# 1-2-5-6-7 3-8-9 4
uf.union(1, 2)
uf.union(2, 5)
uf.union(5, 6)
uf.union(6, 7)
uf.union(3, 8)
uf.union(8, 9)
print(uf.connected(1, 5))  # true
print(uf.connected(5, 7))  # true
print(uf.connected(4, 9))  # false
# 1-2-5-6-7 3-8-9-4
uf.union(9, 4)
print(uf.connected(4, 9))  # true
