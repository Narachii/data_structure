lass unionFind():
	def __init__(self, size):
		self.root = [i for i in range(size)]
	
	def find(self, x):
		while x != self.root[x]:
			x = self.root[x]
			
		return self.root[x]
	
	def union(self, x, y):
		root_x = self.find(self.root[x])
		root_y = self.find(self.root[y])
		
		if root_x != root_y:
			self.root[root_y] = root_x
	
	def connection(self, x, y):
		return self.find(x) == self.find(y)
		
print("-------------New-------------")
uo = unionFind(4)
uo.union(0,2)
uo.find(2)
print(uo.connection(0,2))
print(uo.connection(0,3))
