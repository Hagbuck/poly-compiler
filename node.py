# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
#                           Project : Compilateur (Python)                    #
#                                                                             #
#                                 File : node.py                              #
#                                                                             #
#      Description : Contains all node class declarations and functions.      #
#                                                                             #
#                Contributors : Corentin TROADEC & Anthony Vuillemin          #
#                                                                             #
#                               Date : September 2018                         #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# - - - - - - - - - - - - - - - - - #
#             IMPORT                #
# - - - - - - - - - - - - - - - - - #

# PROJECT MODULES
from conf import *
from utils import *


# - - - - - - - - - - - - - - - - - #
#           CLASS : Node            #
# - - - - - - - - - - - - - - - - - #
class Node() :

    def __init__(self,type,val = None) :
        self.type = type
        self.val = val
        self.childs = []
        self.nbChild = 0
        self.slot = None

    #Add a child
    def add_child(self,child) :
        self.childs.append(child)
        self.nbChild = self.nbChild + 1

    # Display method
    def __str__(self) :
        return "["+self.type+"] ~ "+str(self.val)+"  ~ "+str(self.nbChild)+" child(s)"



# For node to token
class NodeToken(Node) :
    # Constructor
    def __init__(self,token) :
        self.type = getTypeForLeave(token.token)
        self.val = token.val
        self.line = token.line
        self.col = token.col
        self.childs = []
        self.nbChild = 0
        self.slot = None

    # Display method
    def __str__(self) :
        return "["+self.type+"] ~ "+str(self.val)+" ~ ("+str(self.line)+";"+str(self.col)+") ~ "+str(self.nbChild)+" child(s)"


# - - - - - - - - - - - - - - - - - #
#        CLASS : NodeUnaire         #
# - - - - - - - - - - - - - - - - - #
# For unaire operator  : contain one child.
class NodeUnaire(NodeToken) :

    def __init__(self,token,child):
        # inherit def
        NodeToken.__init__(self,token)
        # others declarations
        self.type = getUnaireId(token.token)
        self.childs.append(child)
        self.nbChild = 1

# - - - - - - - - - - - - - - - - - #
#         CLASS : BasicNode         #
# - - - - - - - - - - - - - - - - - #
# For all the others node : contain at least two childs.
class BasicNode(NodeToken) :

    def __init__(self,token,child1,child2) :
        #inherit def
        NodeToken.__init__(self,token)
        # others declarations
        self.type =  getType(token.token)
        self.childs.append(child1)
        self.childs.append(child2)
        self.nbChild = 2


class NodeVarRef(NodeToken) :

    def __init__(self,token,idx = 0) :
        #inherit def
        NodeToken.__init__(self,token)
        self.type = "node_varRef"
        self.idx = idx
        self.nbChild = 0

    # Display method
    def __str__(self) :
        return "["+self.type+"] ~ "+str(self.val)+" ~ ("+str(self.line)+";"+str(self.col)+") ~ slot #"+str(self.slot)

# - - - - - - - - - - - - - - - - - #
#           FUNCTIONS               #
# - - - - - - - - - - - - - - - - - #

#Get node type in relation with the token type
def getUnaireId(token_type) :
    if token_type in unaire_operator:
        return unaire_operator[token_type]
    else :
        return False

#Get type of a node with no child (leave)
def getTypeForLeave(token_type) :
    if token_type == "toke_const" :
        return "node_const"
    else :
        return "node_id"

#Get type
def getType(token_type) :
    if token_type in binaire_operator :
        return binaire_operator[token_type]["type_node"]
    else :
        error_compilation(token,"Incompatible token")

#Display the tree since a node given
def display_tree(node,level) :
    #DISPLAY NODE
    string_space = ""
    for i in range(0,level) :
        string_space += "\t"
    # Tree string - print
    return_str = string_space + str(node) + "\n"
    #DISPLAY CHILDS
    if node != None :
        for child in node.childs :
            # Add string child in string racine
            return_str += display_tree(child,level + 1)
    return return_str
