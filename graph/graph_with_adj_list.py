class Vertex:

    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

    def __str__(self):
        return f'{self.id} connected to: {[x.id for x in self.connectedTo]}'

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    
    def addVertex(self, key: int):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n: int):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def addEdge(self, f: int, t: int, cost=0):
        if f not in self.vertList:
            newVertex = self.addVertex(f)
        
        if t not in self.vertList:
            newVertex = self.addVertex(t)

        self.vertList[f].addNeighbor(self.vertList[t], cost)
    
    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())
    
    def __contains__(self, n):
        return n in self.vertList


g = Graph()
for i in range(6):
    g.addVertex(i)

g.addEdge(0,1,2)
g.addEdge(1,3,2)
g.addEdge(5,3,2)
g.addEdge(3,5,2)

for vertex in g:
    print(vertex)
    print(vertex.getConnections())
