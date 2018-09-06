from conf import *
from utils import *

class Node :
    #Declaration
    def __init__(self,token) :
        self.type = getTypeForLeave(token.token)
        self.val = token.val
        self.line = token.line
        self.col = token.col
        self.childs = []
        self.nbChild = 0

    def __str__(self) :
        return "["+self.type+"] ~ "+str(self.val)+" ~ ("+str(self.line)+";"+str(self.col)+") ~ "+str(self.nbChild)+" child(s)"

#For unaire operators
class NodeUnaire(Node) :

    def __init__(self,token,child):
        #inherit def
        Node.__init__(self,token)
        #others declarations
        self.type = getUnaireId(token.token)
        self.childs.append(child)
        self.nbChild = 1

#For binaire and others operators
class BasicNode(Node) :

    def __init__(self,token,child1,child2) :
        #inherit def
        Node.__init__(self,token)
        self.type =  "TODO"
        self.childs.append(child1)
        self.childs.append(child2)
        self.nbChild = 2

    #Add a child
    def add_child(self,child) :
        self.childs.append(child)
        self.nbChild = self.nbChild + 1

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

#Display the tree since a node given
def display_tree(node,level) :
    #DISPLAY NODE
    string_space = ""
    for i in range(0,level) :
        string_space += "\t"
    print string_space + str(node)
    #DISPLAY CHILDS
    if node != None :
        for child in node.childs :
            display_tree(child,level + 1)
