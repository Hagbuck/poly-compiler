# - * - * - * - * - * - * - * #
#           IMPORT            #
# - * - * - * - * - * - * - * #
#PERSONNAL MODULE
from conf import *
from utils import *
from symbol import *

# - * - * - * - * - * - * - * #
#         FUNCTIONS           #
# - * - * - * - * - * - * - * #

def semantic_analyze(node):
    stack = [{}]

def begin_block(stack):
    table = {}
    stack.append(table)

def end_block(stack):
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


def print_stack(stack):
    print "\n-----------------------------\n"
    str = ""
    for table in stack:
        str += "--"
        for s in table:
            print str + s
    print "\n-----------------------------\n"
