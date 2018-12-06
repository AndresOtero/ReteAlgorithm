class AlphaMemory:
    def __init__(self, condition):
        self.condition = condition
        self.wmes = []
        self.succesors = []

    def addIfCompare(self, wme):
        if self.condition.compare(wme.value):
            self.wmes.append(wme)
