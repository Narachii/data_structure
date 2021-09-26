class unionFind:
	def __init__(self, size):
		self.root = [i for i in range(size)]
		
	
	def find(self, vertex):
		return self.root[vertex]
		
	
	def union(self, v1, v2):
		x = self.find(v1)
		y = self.find(v2)
		
		if not x == y:
			for i in range(len(self.root)):
				if self.root[i] == y:
					self.root[i] = x
					
	
	def connection(self, v1, v2):
		return self.find(v1) == self.find(v2)

print("-------------New-------------")
uo = unionFind(4)
uo.union(0,2)
uo.find(2)
print(uo.connection(0,2))
print(uo.connection(0,3))
