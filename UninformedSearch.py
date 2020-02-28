from graph.GraphHandler import GraphHandler

class UninformedSearch:
    
    def __init__(self):
        self.fail            = False
        self.found           = False
        self.visitedStations = []
        self.fringe          = []

    def search(self, strategy, start, goal):

        self.fringe.append(node([start, None]))

        graphDef = GraphHandler().graphDef

        while (not self.fail) and (not self.found):
            
          if len(self.fringe) == 0:
              self.fail = True
              raise Exception("Empty fringe.")
          else:
                # stack implementation
                if (strategy == 1):
                    activeNode = self.fringe.pop() #lifo = profundidad
                else:
                    activeNode = self.fringe.pop(0) #fifo = anchura
                
                #TODO: revisar este codigo
                if (not (activeNode.data[0] in self.visitedStations)):
                    # print(activeNode.data[0])
                    self.visitedStations.append(activeNode.data[0])
                    if activeNode.data[0] == goal:
                        self.found = True
                        return activeNode
                    else:
                        rawSuccesors = graphDef[activeNode.data[0]]
                        succesors = []
                        for rawSuccesor in rawSuccesors:
                            succesor = node(rawSuccesor)
                            succesor.setParent(activeNode)

                            succesors.append(succesor)
                        
                        self.fringe = self.fringe + succesors
        
        # self.visitedStations[]
    
class node:
    def __init__(self, data):
        self.parent = None
        self.data   = data

    def setParent(self, parent):
        self.parent = parent

    def backTrack(self):
        if self.parent:
            self.parent.backTrack()
        self.printNode()
        
    def printNode(self):
        graph = GraphHandler()
        station = graph.getStationsData(self.data[0])
        line    = graph.getLinesData(self.data[1])
        print(f'{station} - {line}')