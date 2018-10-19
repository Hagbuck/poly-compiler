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

# Main function for the semantic analyse
# TODO 
def semantic_analyze(node):
    stack = [{}]


# At the begin of a block, create a new table map of symbol
def begin_block(stack):
    table = {}
    stack.append(table)


# At the end of a block, remove the symbol table previously generated
def end_block(stack):
    # Do not remove the first table
    if len(stack) > 1:
        stack.pop()


# Create a new symbol into the stack
def new_symbol(ident, stack):
    
    T = stack[-1]
    if ident in T:
        error_compilation(None, "Error : " + ident + " is already defined")
        return
    
    S = Symbol(ident)
    T[ident] = S
    return S


# Research an ident into the stack
def search_symbol(ident, stack):
    i = len(stack) - 1
    
    while i >= 0:
        T = stack[i]
        if ident in T:
            return T[ident]
        i -= 1
    
    error_compilation(None, "Error : " + ident + " is not defined")


# Display the stack
def print_stack(stack):
    print "\n-----------------------------\n"
    str = ""
    for table in stack:
        str += "--"
        for s in table:
            print str + s
    print "\n-----------------------------\n"
