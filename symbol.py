#CLASS SYMBOL
class Symbol:
    #Declaration
    def __init__(self, ident, type_symbol):
        self.ident = ident

        self.type = type_symbol # var or funct
        self.nb_args = -1
        self.nb_slot = -1

    def __str__(self) :
        return "[" + self.ident + "] ~ ["+self.type+"] ~ (" + str(self.nb_args) + ":" + str(self.nb_slot) + ")"
