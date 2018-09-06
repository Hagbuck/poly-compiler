#CLASS TOKEN
class Token :
    #Declaration
    def __init__(self,token,line,col) :
        self.val = None
        self.token = token
        self.line = line
        self.col = col

    #Give a val (optionnal)
    def set_val(val) :
        self.val = val

    #For display token
    def __str__(self) :
        return "["+str(self.token)+"] - "+str(self.val)+" - ("+str(self.line)+";"+str(self.col)+")"
