class Rule:
    def __init__(self, name):
        self.name = name
        self.conditions = []
        self.actions = []

    def addCondition(self, condition):
        self.conditions = condition
