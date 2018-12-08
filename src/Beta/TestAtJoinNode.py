class TestAtJoinNode:
    def __init__(self, fieldOfArg1, conditionNumberOfArg2, fieldOfArg2):
        self.fieldOfArg2 = fieldOfArg2
        self.conditionNumberOfArg2 = conditionNumberOfArg2
        self.fieldOfArg1 = fieldOfArg1

    @staticmethod
    def getJoinTestsfromCondition(condition, earlierConds):
        result = []
        for field in condition.getFields():
            v=TestAtJoinNode.getVariable(field)
            for cond in earlierConds:
                if cond.hasVariable(v):
                    



    @staticmethod
    def getVariable(field):
        return ""
