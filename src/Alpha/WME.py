class WME:
    def __init__(self, attribute, symbol, value):
        self.value = value
        self.symbol = symbol
        self.attribute = attribute
        self.alphaMemsItems = []
        self.tokens = []

    def __str__(self):
        return  str(self.attribute)+str(self.symbol)+str(self.value)