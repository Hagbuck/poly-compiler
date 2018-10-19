# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
#                           Project : Compilateur (Python)                    #
#                                                                             #
#                             File : synthax_analyze.py                       #
#                                                                             #
#                   Description : Synthax analyze file and functions.         #
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
from node import *
from token import *
from utils import *

# - - - - - - - - - - - - - - - - - #
#           FUNCTIONS               #
# - - - - - - - - - - - - - - - - - #

# Launch synthax analyze
def synthax_analyse() :
    global index_tab

    # Main node (racine)
    P = Node("prog")

    # Parcour all token tab
    while index_tab < len(tab_token):
        N = get_statment()
        P.add_child(N)
    return P


# Return a tree compose by cons/id & unaire operator
def atom() :
    #GET GLOBAL VAR
    global index_tab

    #Search an atom but end of the list, so a paramter missing
    if index_tab >= len(tab_token) : # and tab_token[-1].token != "toke_parantClose" :
        error_compilation(tab_token[index_tab-1],"Operator Missing the second parameter.")
    #if index_tab < len(tab_token)-1 and
    current_toke = tab_token[index_tab]

    #UNAIRE OPERATOR
    if current_toke.token in unaire_operator :
        index_tab = index_tab + 1
        current_node = atom()
        return NodeUnaire(current_toke,current_node)

    #CONST
    elif current_toke.token == "toke_const" :
        index_tab = index_tab + 1
        return NodeToken(current_toke)

    #IDENT
    elif current_toke.token == "toke_id" :
        index_tab = index_tab + 1
        return NodeVarRef(current_toke)

    #PARANTHESE
    elif current_toke.token == "toke_parantOpen" :
        index_tab = index_tab + 1
        N = expr()

        #End expression
        if index_tab >= len(tab_token) :
            error_compilation(tab_token[len(tab_token)-1],"Parenthesis missing.")

        #Missing parenthesis
        elif tab_token[index_tab].token != "toke_parantClose" :
            error_compilation(tab_token[index_tab],"Parenthesis missing.")

        index_tab = index_tab + 1
        return N

    #IMPLICIT ELSE --> Incompatible token
    error_compilation(current_toke,"Incoherent Char : Double operator deteted.")

# Launch the synthax analyze with a high priority level
def expr() :
    return expr_launch(1000);

# Build a tree composed with the tokens tab
def expr_launch(priority) :

    global index_tab

    #Recup first atom
    A = atom()

    #End of token list ?
    if index_tab < len(tab_token)  :
        current_toke = tab_token[index_tab]

        #Toke const or id follow by a same other
        if tab_token[index_tab].token == "toke_const" or tab_token[index_tab].token  == "toke_id" :
            error_compilation(current_toke,"Constant or identifiant repetition without operator.")

        #Toke is an open paranthesis.
        if current_toke.token == "toke_parantOpen" :
            error_compilation(current_toke,"Illegal expression.")

        while current_toke.token in binaire_operator and index_tab < len(tab_token) : # -1
            #If priority superior
            if binaire_operator[current_toke.token]["priority"] >= priority :
                break


            index_tab = index_tab + 1
            #Simplify reading
            thisPriority = binaire_operator[current_toke.token]["priority"]
            thisAssociativity = binaire_operator[current_toke.token]["associativity"]

            #Build the second child (recursif)
            secondChild = expr_launch(thisPriority + thisAssociativity)

            #No second child
            if(secondChild == None) :
                error_compilation(current_toke,"Operator Missing the second parameter.")
                break


            N = BasicNode(current_toke,A,secondChild)
            A = N

            #End toke list ?
            if index_tab < len(tab_token) : #-1
                current_toke = tab_token[index_tab]

    return A

# Find a statment model and build it
def get_statment():
    global index_tab

    # Declaration (ex : var x;)
    if tab_token[index_tab].token == "toke_var":
        accept("toke_var")
        cpy_toke_id = accept("toke_id")
        accept("toke_semicolon")
        node_dcl = Node("node_dcl",cpy_toke_id.val)
        return node_dcl

    # Begining a block section
    elif tab_token[index_tab].token == "toke_braceOpen" :
        N = Node("node_block")
        accept("toke_braceOpen")
        while tab_token[index_tab].token != "toke_braceClose" :
            N.add_child(get_statment())
        accept("toke_braceClose")
        return N

    # If (and else)
    elif tab_token[index_tab].token == "toke_if" :
        accept("toke_if")
        accept("toke_parantOpen")
        T = expr()
        accept("toke_parantClose")
        B = get_statment()
        N = Node("node_cond")
        N.add_child(T)
        N.add_child(B)
        if index_tab < len(tab_token) and tab_token[index_tab].token == "toke_else" :
            #index_tab = index +1
            accept("toke_else")
            N.add_child(get_statment())
        return N

    # While
    elif tab_token[index_tab].token == "toke_while" :
        N = Node("node_loop")
        accept("toke_while")
        accept("toke_parantOpen")
        T = expr()
        accept("toke_parantClose")
        B = get_statment()
        N_cond = Node("node_cond")
        N_cond.add_child(T)
        N_cond.add_child(B)
        N_cond.add_child(Node("node_break"))
        N.add_child(N_cond)
        return N

    # For
    elif tab_token[index_tab].token == "toke_for" :
        # Main node
        main_node = Node("node_seq")
        # Gramar
        accept("toke_for")
        accept("toke_parantOpen")
        init = expr()
        accept("toke_semicolon")
        test = expr()
        accept("toke_semicolon")
        step = expr()
        accept("toke_parantClose")
        B = get_statment()

        # body & step
        seq_node = Node("seq")
        seq_node.add_child(B)
        seq_node.add_child(step)

        # Test / sequence & break
        cond_node = Node("node_cond")
        cond_node.add_child(test)
        cond_node.add_child(seq_node)
        cond_node.add_child(Node("node_break"))

        # Loop (encaps cond node)
        loop_node = Node("node_loop")
        loop_node.add_child(cond_node)

        # Add in main_node
        main_node.add_child(init)
        main_node.add_child(loop_node)

        return main_node

    # Print
    if tab_token[index_tab].token == "toke_print" :
        N = Node("node_print")
        accept("toke_print")
        N.add_child(get_statment())
        return N


    # Default expression + ";"
    else :
        A = expr()
        accept("toke_semicolon")
        D = Node("node_drop")
        D.add_child(A)
        return D

def accept(token_waiting) :
    global index_tab

    if index_tab >= len(tab_token):
        error_compilation(tab_token[-1],"Missing semicolon.")

    current_toke = tab_token[index_tab]

    if token_waiting == current_toke.token :
        index_tab = index_tab + 1
        return current_toke

    else :
        error_compilation(current_toke,"Token not excepted. '"+token_waiting+"' waiting.")
