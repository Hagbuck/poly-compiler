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

nb_label = 0

# Build assemblor instructions with the given node
def genCode(N) :

    global nb_label

    str_code = ""

    if N.type == "prog" :
        str_code += "push.i 0\n"
        write_assemblor_file("push.i 0")
        for statment in N.childs :
            str_code += genCode(statment)
        return str_code

    # CONST
    elif N.type == "node_const" :
        write_assemblor_file("push.i "+str(N.val))
        return "push.i "+str(N.val) + "\n"

    # POW
    elif N.type == "node_pow" :
        # Eval right child
        n = eval_expr(N.childs[1])
        # Build expression pow
        # General case
        if n != 0 :
            return pow_compil(n,N) + "\n"
        # Exception with pow 0
        else :
            str_code = "push.i 1\npush.i 0\nadd.i\n"
            write_assemblor_file(str_code)
            return str_code

    # BINAIRE OPERATOR
    elif N.type in dict_bin_node_to_assemblor :
        str_code += genCode(N.childs[0])
        str_code +=  genCode(N.childs[1])
        write_assemblor_file(dict_bin_node_to_assemblor[N.type])
        return str_code + dict_bin_node_to_assemblor[N.type]+ "\n"

    # UNAIRE MIN
    elif N.type == "node_min_U" :
        str_code += "push.i 0\n"
        write_assemblor_file("push.i 0")
        str_code += genCode(N.childs[0])
        write_assemblor_file("sub.i")
        return str_code + "sub.i" + "\n"

    # UNAIRE NOT
    elif N.type == "node_not_U" :
        str_code = genCode(N.childs[0])
        write_assemblor_file("not")
        return str_code + "not" + "\n"

    # DROP (End of a statment)
    elif N.type == "node_drop" :
        str_code = genCode(N.childs[0])
        write_assemblor_file("drop")
        return str_code + "drop\n"

    # REFERENCE to a variable
    elif N.type == "node_varRef" :
        str_code = "get "+str(N.slot)+"\n"
        write_assemblor_file(str_code)
        return str_code

    # ASSIGNATION
    elif N.type == "node_assign" :
        str_code = genCode(N.childs[1])
        write_assemblor_file("dup")
        write_assemblor_file("set " + str(N.childs[0].slot))
        str_code += "dup\nset "+str(N.childs[0].slot)+"\n"
        return str_code

    # DEFINITION
    elif N.type == "node_dcl" :
        return str_code

    # COND
    elif N.type == "node_cond" :
        # 3 childs -> if else
        if N.nbChild == 3 :
            L1 = nb_label
            nb_label = nb_label + 1
            L2 = nb_label
            nb_label = nb_label + 1

            genCode(N.childs[0])                    # <test>
            write_assemblor_file("jumpf l" + L1)    # jumpf L1
            genCode(N.childs[1])                    # <body1>
            write_assemblor_file("jump " + L2)      # jump L2
            write_assemblor_file(".l" + L1)         # .L1
            genCode(n.childs[2])                    # <body2>
            write_assemblor_file(".l" + L2)         # .L2

        else : # simple if
            L = nb_label
            nb_label = nb_label + 1

            genCode(N.childs[0])                    # <test>
            write_assemblor_file("jump.f l" + L)    # jumpf L
            genCode(N.childs[1])                    # <body>
            write_assemblor_file(".l" + L)          # .L

    # OTHER TYPE (Ignore node and go to childs)
    else :
        DEBUG_MSG("Ignore node : "+str(N),"WARN")
        str_code += genCode(N.childs[0]) + "\n"
        return str_code

# pow function for assemblor
def pow_compil(n,N) :
    str_code = genCode(N.childs[0])
    main_code = str_code
    write_assemblor_file(str_code)
    for i in range(1,n) :
        write_assemblor_file(str_code)
        write_assemblor_file("mul.i")
        main_code += str_code
        main_code += "mul.i" + "\n"
    return main_code + "\n"


# Code generator (assemblor instrutions) launch
def compil(N) :
    # Start
    write_assemblor_file(".start")
    # Generation
    main_code = "\n" + genCode(N)
    # Display result and finsh the generation
    write_assemblor_file("out.i")
    write_assemblor_file("push.i 10")
    write_assemblor_file("out.c")
    return main_code
