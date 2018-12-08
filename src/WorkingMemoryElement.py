from src.Alpha.TestNode import FieldToTestEnum


class WorkingMemoryElement:
    """"""

    def __init__(self, identifier, attribute, value):
        self.identifier = identifier
        self.attribute = attribute
        self.value = value
        self.alphaMemItems = []
        self.tokens = []
        self.negativeJoinResults = []

    def get(self, fieldToTest):
        if FieldToTestEnum.IDENTIFIER == fieldToTest:
            return self.identifier

        if FieldToTestEnum.ATTRIBUTE == fieldToTest:
            return self.attribute

        if FieldToTestEnum.VALUE == fieldToTest:
            return self.value

    def getListOfFields(self):
        return [self.identifier,self.attribute,self.value]