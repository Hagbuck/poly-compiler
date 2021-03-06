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
import conf
from sem_analyze import *
from token import *
from utils import *

# - - - - - - - - - - - - - - - - - #
#           FUNCTIONS               #
# - - - - - - - - - - - - - - - - - #

nb_label = 0
list_label_end = [] #label for end loop
list_label_begin = [] #label for start loop
list_label_step = [] #label for step loop

# Build assemblor instructions with the given node
def genCode(N) :

    global nb_label

    str_code = ""

    # MAIN NODE (prog)
    if N.type == "prog" :
        for functions in N.childs :
            str_code += str(genCode(functions))
        return str_code

    # FUNCTIONS
    if N.type == "funct" :
        str_code += "." + N.val + "\n"
        write_assemblor_file("." + N.val)
        # Get symbol
        S = search_symbol(N.val)

        # Slots reservation
        for i in range(0,S.nb_slot) :
            str_code += "push.i 0\n"
            write_assemblor_file("push.i 0")

        # Gen code for last child
        str_code += genCode(N.childs[-1])
        # end function bloc

        str_code += 'push.i 0\nret\n'
        write_assemblor_file("push.i 0\nret")
        return str_code

    # FUNCTION REFERENCE
    if N.type == "funct_ref" :
        str_code += "prep "+N.val+"\n"
        write_assemblor_file("prep "+N.val)
        # Generate childs code
        for ch in N.childs :
            str_code += genCode(ch)
        # End block
        str_code += "call "+str(N.nbChild)+"\n"
        write_assemblor_file("call "+str(N.nbChild))
        return str_code

    # RETURN
    if N.type == "return" :
        str_code += genCode(N.childs[0]) + "\n"
        str_code += "ret\n"
        write_assemblor_file("ret")
        return str_code

    # CONST
    elif N.type == "node_const" :
        write_assemblor_file("push.i "+str(N.val))
        return "push.i "+str(N.val) + "\n"

	# POW
    elif N.type == "node_pow" :
        write_assemblor_file("prep pow_system")
        str_code += genCode(N.childs[0])
        str_code += genCode(N.childs[1])
        write_assemblor_file("call 2")
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

    # Loop
    elif N.type == "node_loop" :
        Ldebut = nb_label
        nb_label = nb_label + 1
        Lfin = nb_label
        nb_label = nb_label + 1
        Lstep = nb_label
        nb_label = nb_label + 1
        # save end label
        list_label_begin.append(Ldebut)
        list_label_end.append(Lfin)
        list_label_step.append(Lstep)
        DEBUG_MSG("Begin Loop Label .l"+str(Ldebut)+" -> "+str(N),"INFO")
        DEBUG_MSG("End Loop Label .l"+str(Lfin)+" -> "+str(N),"INFO")
        DEBUG_MSG("Step Loop Label .l"+str(Lstep)+" -> "+str(N),"INFO")
        # label boucle
        str_code += ".l" + str(Ldebut) + "\n"
        write_assemblor_file(".l" + str(Ldebut))
        # corps boucle
        str_code += genCode(N.childs[0])
        # end boucle
        str_code += "jump l" + str(Ldebut) + "\n"
        write_assemblor_file("jump l" + str(Ldebut))
        # exit boucle

        str_code += ".l" + str(Lfin) + "\n"
        write_assemblor_file(".l" + str(Lfin))

        list_label_end.pop()
        list_label_begin.pop()
        list_label_step.pop()

        return str_code

    #BREAK
    elif N.type == "break" :
        # Break outside loop
        if(len(list_label_end) == 0 ):
            error_compilation(N,"`break` statement not within loop.")

        str_code += "jump l" + str(list_label_end[-1]) + " \n"
        write_assemblor_file( "jump l" + str(list_label_end[-1]))
        return str_code

    #CONTINUE
    elif N.type  == "continue" :
        # Continue outside loop
        if(len(list_label_step) == 0):
            error_compilation(N,"`continue` statement not within loop.")

        str_code += "jump l" + str(list_label_step[-1]) + " \n"
        write_assemblor_file( "jump l" + str(list_label_step[-1]))
        # JUMP TO THE STEP
        return str_code

    #STEP
    elif N.type  == "step" :
        # Continue outside loop
        if(len(list_label_begin) == 0 ):
            error_compilation(N,"`continue` statement not within loop.")
        # EXEC BODY STEP
        str_code += ".l" +str(list_label_step[-1])
        write_assemblor_file(".l"+ str(list_label_step[-1]))
        # Verif if this isn't an empty node (while case)
        if(N.nbChild >= 1) :
            genCode(N.childs[0])

        # Jump to the top of loop
        str_code += "jump l" + str(list_label_begin[-1]) + " \n"
        write_assemblor_file( "jump l" + str(list_label_begin[-1]))
        return str_code

    # COND
    elif N.type == "node_cond" :
        str_code += ""
        # 3 childs -> if else
        if N.nbChild == 3 :
            L1 = nb_label
            nb_label = nb_label + 1
            L2 = nb_label
            nb_label = nb_label + 1

            str_code += genCode(N.childs[0])            # <test>
            write_assemblor_file("jumpf l" + str(L1))   # jumpf L1
            str_code += "jumpf l" + str(L1) + "\n"
            str_code += genCode(N.childs[1])            # <body1>
            write_assemblor_file("jump l" + str(L2))     # jump L2
            str_code += "jump l" + str(L2) + "\n"
            write_assemblor_file(".l" + str(L1))        # .L1
            str_code += ".l" + str(L1) + "\n"
            str_code += genCode(N.childs[2])            # <body2>
            write_assemblor_file(".l" + str(L2))        # .L2
            str_code += ".l" + str(L2) + "\n"

            DEBUG_MSG("Label .l"+str(L1)+" -> "+str(N.childs[1]),"INFO")
            DEBUG_MSG("Label .l"+str(L2)+" -> "+str(N.childs[2]),"INFO")

        else : # simple if
            L = nb_label
            nb_label = nb_label + 1

            str_code += genCode(N.childs[0])            # <test>
            write_assemblor_file("jumpf l" + str(L))   # jumpf L
            str_code += "jumpf l" + str(L) + "\n"
            str_code += genCode(N.childs[1])            # <body>
            write_assemblor_file(".l" + str(L))         # .L
            str_code += ".l" + str(L) + "\n"
            DEBUG_MSG("Label .l"+str(L)+" -> "+str(N.childs[1]),"INFO")

        return str_code

    # PRINT
    if N.type == "node_print" :
        str_code += genCode(N.childs[0])
        str_code += "out.i\n"
        write_assemblor_file("out.i")
        # Dispaly '\n'
        write_assemblor_file("push.i 10")
        write_assemblor_file("out.c")
        return str_code

    # OTHER TYPE (Ignore node and go to childs)
    else :
        # For all childs, generate code
        for i in range(0,N.nbChild) :
            str_code += genCode(N.childs[i]) + "\n"
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
    write_assemblor_file(".start\nprep main\ncall 0\nhalt")
    main_code = ".start\nprep main\ncall 0\nhalt\n"
    # Generation
    main_code += "\n\n" + genCode(N)
    return main_code
