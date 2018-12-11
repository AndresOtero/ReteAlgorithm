from src.Alpha.ItemInAlphaMemory import ItemInAlphaMemory


class AlphaMemory:
    def __init__(self, condition):
        self.condition = condition
        self.items = []
        self.succesors = []

    def addIfCompare(self, wme):
        if self.condition.compareValue(wme.value):
            newItem=ItemInAlphaMemory(wme,self)
            self.items.insert(0,newItem)
            wme.alphaMemsItems.insert(0,newItem)
            for child in self.succesors:
                child.rightActivation(wme)

