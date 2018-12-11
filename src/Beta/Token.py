class Token:
    def __init__(self, parent, wme, node):
        self.wme = wme
        self.parent = parent
        self.node = node
        self.children = []

    @staticmethod
    def makeToken(node, parentToken, wme):
        tok = Token(parent=parentToken, wme=wme, node=node)
        parentToken.children.insert(0, tok)
        wme.tokens.insert(0, tok)
        return tok

    def deleteTokenAndDescendents(self):
        while len(self.children) != 0:
            self.children[0].deleteTokenAndDescendents()
        self.node.items.remove(self)
        self.wme.tokens.remove(self)
        self.parent.children.remove(self)
