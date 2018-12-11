class TestAtJoinNode:
    def __init__(self, fieldOfArg1, fieldOfArg2):
        self.fieldOfArg2 = fieldOfArg2
        self.fieldOfArg1 = fieldOfArg1

    @staticmethod
    def getJoinTestFromCondition(condition, earlierConditions):
        result = None
        for e in earlierConditions:
            if condition.name == e.name:
                result = TestAtJoinNode(condition, e)
        return result
