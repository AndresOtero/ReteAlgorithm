class Token:
    def __init__(self, parent, wme, node):
        self.parent = parent
        self.wme = wme
        self.node = node
        self.children = []
        self.joinResults = []
        self.nccResults = []
        self.owner = []
        self.parent.children.insert(0, self)
        if wme:
            wme.tokens.insert(0, self)
