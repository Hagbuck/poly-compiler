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
    P = Node("Prog")

    global index_tab

    while index_tab < len(tab_token):
        N = statment()
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

    #CONST & ID TOKEN
    elif current_toke.token == "toke_const" or current_toke.token == "toke_id" :
        index_tab = index_tab + 1
        return Node(current_toke)

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

def statment():
    global index_tab

    if tab_token[index_tab].token == "toke_var":
        accept("toke_var")
        accept("toke_id")
        accept("toke_semicolon")

    else :
        A = expr()
        accept("toke_semicolon")
        D = Node("drop")
        D.add_child(A)
        return D

def accept(token_waiting)
    global index_tab

    current_toke = tab_token[index_tab + 1]

    if token_waiting == current_toke.token:
        index_tab = index_tab + 1
    else 
        error_compilation(current_toke,"Token not excepted")