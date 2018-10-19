#CLASS SYMBOL
class Symbol:
    #Declaration
    def __init__(self, ident):
        self.col = 0
        self.line = 0
        self.ident = ident

    def __str__(self) :
        return "[" + self.ident + "] ~ (" + str(self.line) + ":" + str(self.col) + ")"
