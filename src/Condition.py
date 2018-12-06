from abc import ABC, abstractmethod


class Condition(ABC):
    """"""

    def __init__(self, name, value):
        self.name = name
        self.value = value

    @abstractmethod
    def compare(self):
        pass


class Equal(Condition):
    """"""

    def __init__(self, name, value):
        super().__init__(name=name, value=value)

    def compare(self, value):
        return self.value == value


class GreaterOrEqual(Condition):
    """"""

    def __init__(self, name, value):
        super().__init__(name=name, value=value)

    def compare(self, value):
        return self.value <= value


class LessOrEqual(Condition):
    """"""

    def __init__(self, name, value):
        super().__init__(name=name, value=value)

    def compare(self, value):
        return self.value >= value
