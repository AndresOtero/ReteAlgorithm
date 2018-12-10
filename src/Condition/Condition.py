from abc import ABC, abstractmethod


class Condition(ABC):
    """"""

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def compare(self, knowledge, attributeKey):
        knowledgeSymbol = knowledge.getSymbol(attributeKey)
        if knowledgeSymbol == self.getSymbol() or knowledgeSymbol == " = ":
            return self.compareValue(knowledge.getValue(attributeKey))
        return False

    @abstractmethod
    def getSymbol(self):
        pass

    @abstractmethod
    def compareValue(self, param):
        pass


class Equal(Condition):
    """"""

    def getSymbol(self):
        return " = "

    def __init__(self, name, value):
        super().__init__(name=name, value=value)

    def compareValue(self, value):
        return self.value == value


class GreaterOrEqual(Condition):
    """"""

    def getSymbol(self):
        return " >= "

    def __init__(self, name, value):
        super().__init__(name=name, value=value)

    def compareValue(self, value):
        return self.value <= value


class Greater(Condition):
    """"""

    def getSymbol(self):
        return " > "

    def __init__(self, name, value):
        super().__init__(name=name, value=value)

    def compareValue(self, value):
        return self.value < value


class LesserOrEqual(Condition):
    """"""

    def getSymbol(self):
        return " <= "

    def __init__(self, name, value):
        super().__init__(name=name, value=value)

    def compareValue(self, value):
        return self.value >= value


class Lesser(Condition):
    """"""

    def getSymbol(self):
        return " < "

    def __init__(self, name, value):
        super().__init__(name=name, value=value)

    def compareValue(self, value):
        return self.value > value
