# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
#                           Project : Compilateur (Python)                    #
#                                                                             #
#                             File : code_generator.py                        #
#                                                                             #
#         Description : Functions use to generate assemblor instruction.      #
#                                                                             #
#              Contributors : Corentin TROADEC & Anthony Vuillemin            #
#                                                                             #
#                               Date : September 2018                         #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# - - - - - - - - - - - - - - - - - #
#             IMPORT                #
# - - - - - - - - - - - - - - - - - #

# PROJECT MODULES
from conf import *
from token import *
from utils import *

# - - - - - - - - - - - - - - - - - #
#           FUNCTIONS               #
# - - - - - - - - - - - - - - - - - #

# Build assemblor instructions with the given node
def genCode(N) :

    # CONST
    if N.type == "node_const" :
        write_assemblor_file("push.i "+str(N.val))

    # BINAIRE OPERATOR
    elif N.type in dict_bin_node_to_assemblor :
        genCode(N.childs[0])
        genCode(N.childs[1])
        write_assemblor_file(dict_bin_node_to_assemblor[N.type])

    # UNAIRE MIN
    elif N.type == "node_min_U" :
        write_assemblor_file("push.i 0")
        genCode(N.childs[0])
        write_assemblor_file("sub.i")

    # UNAIRE NOT
    elif N.type == "node_not_U" :
        genCode(N.childs[0])
        write_assemblor_file("not")

    # OTHER TYPE (Ignore node and go to childs)
    else :
        print "[WARN] ~ Operation pass : "+str(N)
        genCode(N.childs[0])

# Code generator (assemblor instrutions) launch
def compil(N) :
    # Start
    write_assemblor_file(".start")
    # Generation
    genCode(N)
    # Display result and finsh the generation
    write_assemblor_file("out.i")
    write_assemblor_file("push.i 10")
    write_assemblor_file("out.c")
