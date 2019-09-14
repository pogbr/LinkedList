class Node:
    def __init__(self, dadoinicial):
        self.dado = dadoinicial
        self.proximo = None
    def getDado(self):
        return self.dado
    def getProximo(self):
        return self.proximo
    def setDado(self, novodado):
        self.dado = novodado
    def setProximo(self, novoproximo):
        self.proximo = novoproximo
        
     