#CLASS SYMBOL
class Symbol:
    #Declaration
    def __init__(self, ident, type_symbol):
        self.col = 0
        self.line = 0
        
        self.ident = ident

        self.type = type_symbol # var or funct
        self.nb_args = -1
        self.nb_slot = -1

    def __str__(self) :
        return "[" + self.ident + "] ~ (" + str(self.line) + ":" + str(self.col) + ")"
