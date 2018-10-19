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
from conf import *
from utils import *
from symbol import *

# - - - - - - - - - - - - - - - - - #
#           FUNCTIONS               #
# - - - - - - - - - - - - - - - - - #

stack = [{}]

# Main function for the semantic analyse
def semantic_analyze(node):

    global nb_slot

    if node.type == "node_dcl":
        S = new_symbol(node.val);
        
        S.slot = nb_slot
        nb_slot = nb_slot + 1

    elif node.type == "node_varRef":
        S = search_symbol(node.val)
        node.slot = S.slot

    elif node.type == "node_block":
        begin_block()
        
        for child in node.childs:
            semantic_analyze(child)

        end_block()

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
def new_symbol(ident):
    
    T = stack[-1]
    if ident in T:
        error_compilation(None, "Error : " + ident + " is already defined")
        return
    
    S = Symbol(ident)
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
    
    error_compilation(None, "Error : " + ident + " is not defined")


# Display the stack
def print_stack():
    print "\n-----------------------------\n"
    str = ""
    for table in stack:
        str += "--"
        for s in table:
            print str + s
    print "\n-----------------------------\n"
