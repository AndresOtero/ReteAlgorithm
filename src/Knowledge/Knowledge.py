# noinspection SpellCheckingInspection
from src.InputFiles.Constants import Constants


class Knowledge:
    def __init__(self):
        self.attributeDicc = {}

    def hasAttribute(self, attributeKey):
        return attributeKey in self.attributeDicc

    def hasValue(self, value):
        return True if value in [symbolValueTuple for symbolValueTuple in self.attributeDicc.values()] else False

    def hasKeyValue(self, attributeKey, value):
        return self.hasAttribute(attributeKey) and self.hasValue(value)

    def getValue(self, attributeKey):
        return self.attributeDicc[attributeKey][1]

    def getSymbol(self, attributeKey):
        return self.attributeDicc[attributeKey][0]

    def addAttribute(self, attributeKey, symbol, value):
        self.attributeDicc[attributeKey] = [symbol, value]

    def __str__(self):
        knowString="Las conclusiones son las siguientes:\n"
        for key in self.attributeDicc:
            if Constants.hasKey(key):
                knowString+=" - "+ str(key) +" : "+str(Constants.getConstant(key,self.getValue(key)))+"\n"
            else:
                knowString+=" - "+ str(key) +" : "+str(self.getValue(key))+"\n"
        return knowString
