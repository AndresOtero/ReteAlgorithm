from src.Alpha.ItemInAlphaMemory import ItemInAlphaMemory


class AlphaMemory:
    def __init__(self):
        self.items = []
        self.succesors = []
        self.referenceCount = 0

    def alphaMemoryActivation(self, wme):
        item = ItemInAlphaMemory(wme,self)
        self.wmes.insert(0, item)
        self.wmes.alphaMemItems.insert(0, item)
        for child in self.succesors:  # Join nodes
            child.rightActivation(wme)
