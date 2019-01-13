# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
#                           Project : Compilateur (Python)                    #
#                                                                             #
#                                File : sem_analyse.py                        #
#                                                                             #
#             Description : Semantique analyze file and functions             #
#                                                                             #
#                Contributors : Corentin TROADEC & Anthony Vuillemin          #
#                                                                             #
#                               Date : September 2018                         #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# - - - - - - - - - - - - - - - - - #
#             IMPORT                #
# - - - - - - - - - - - - - - - - - #
#
#PERSONNAL MODULE
import conf
from utils import *
from symbol import *

# - - - - - - - - - - - - - - - - - #
#           FUNCTIONS               #
# - - - - - - - - - - - - - - - - - #

stack = [{}]

# Main function for the semantic analyse
def semantic_analyze(node):
            
    # Variable declaration node
    if node.type == "node_dcl":
        S = new_symbol(node.val, "var");

        S.slot = conf.nb_slot
        conf.nb_slot = conf.nb_slot + 1
        
    # Assign node, check if the assignement go well to a varRef
    elif node.type == "node_assign":
        if node.childs[0].type != "node_varRef":
            error_compilation(node, "Error : cannot assign " + str(node.childs[1].val) + " to " + str(node.childs[0].val)+ " because " + str(node.childs[0].val) + " is not a varRef")
        semantic_analyze(node.childs[0])
        semantic_analyze(node.childs[1])
    
    # Variable reference node
    elif node.type == "node_varRef":
        S = search_symbol(node.val)
        node.slot = S.slot

    # Block node
    elif node.type == "node_block":
        begin_block()

        for child in node.childs:
            semantic_analyze(child)

        end_block()

    # Declaration function node
    elif node.type == "funct":
        conf.nb_slot = 0
        S = new_symbol(node.val, "funct")
        S.nb_args = node.nbChild - 1

        begin_block()

        for child in node.childs:
            semantic_analyze(child)

        end_block()
        S.nb_slot = conf.nb_slot - S.nb_args
        DEBUG_MSG("[STACK] ~ ["+S.ident+"] ~ USED SLOTS : "+str(S.nb_slot)+".")

    # Call function node
    elif node.type == "funct_ref":
        S = search_symbol(node.val)

        if S.type != "funct":
            error_compilation(node, "Error : " + S.ident + " isn't a function.")

        elif S.nb_args != node.nbChild:
            error_compilations(node, "Error : " + S.ident + " require " + S.nb_args + " arguments.")

        for child in node.childs:
            semantic_analyze(child)

    else:
        for child in node.childs:
            semantic_analyze(child)


# At the begin of a block, create a new table map of symbol
def begin_block():
    table = {}
    stack.append(table)


# At the end of a block, remove the symbol table previously generated
def end_block():
    # Do not remove the first table
    if len(stack) > 1:
        stack.pop()


# Create a new symbol into the stack
def new_symbol(ident, type_symbol):

    T = stack[-1]
    if ident in T:
        error_compilation(None, "Error : " + ident + " is already defined.")
        return

    S = Symbol(ident, type_symbol)
    T[ident] = S
    return S


# Research an ident into the stack
def search_symbol(ident):
    i = len(stack) - 1

    while i >= 0:
        T = stack[i]
        if ident in T:
            return T[ident]
        i -= 1

    error_compilation(None, "Error : " + ident + " is not defined.")


# Display the stack
def print_stack():
    print "\n-----------------------------\n"
    str = ""
    for table in stack:
        str += "--"
        for s in table:
            print str + s
    print "\n-----------------------------\n"
