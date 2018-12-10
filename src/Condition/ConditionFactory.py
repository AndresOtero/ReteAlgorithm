from src.Condition.Condition import *


class ConditionFactory():
    """"""

    @staticmethod
    def createCondition(attribute, condition, value):
        if condition == " = ":
            return Equal(attribute, value)
        if condition == " >= ":
            return GreaterOrEqual(attribute, value)
        if condition == " > ":
            return Greater(attribute, value)
        if condition == " < ":
            return Lesser(attribute, value)
        else:
            return LesserOrEqual(attribute, value)
