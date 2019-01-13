# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
#                           Project : Compilateur (Python)                    #
#                                                                             #
#                                 File : token.py                             #
#                                                                             #
#      Description : Contains all token class declarations and functions.     #
#                                                                             #
#                Contributors : Corentin TROADEC & Anthony Vuillemin          #
#                                                                             #
#                               Date : September 2018                         #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #


# - - - - - - - - - - - - - - - - - #
#           CLASS : Token           #
# - - - - - - - - - - - - - - - - - #
class Token :
    # Declaration
    def __init__(self,token,line,col) :
        self.val = None
        self.token = token
        self.line = line
        self.col = col

    # Give a val (optionnal)
    def set_val(val) :
        self.val = val

    # Display token method
    def __str__(self) :
        return "["+str(self.token)+"] - "+str(self.val)+" - ("+str(self.line)+";"+str(self.col)+")"
