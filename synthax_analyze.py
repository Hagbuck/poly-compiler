# - * - * - * - * - * - * - * #
#           IMPORT            #
# - * - * - * - * - * - * - * #

#PERSONNAL MODULE
from conf import *
from node import *
from token import *
from utils import *

# - * - * - * - * - * - * - * #
#         FUNCTIONS           #
# - * - * - * - * - * - * - * #

def synthax_analyse() : #atom
    return expr()

#Return a tree compose by leave (cont or id) & unaire operator
def atom() :
    #GET GLOBAL VAR
    global index_tab
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
        if tab_token[index_tab].token != "toke_parantClose" :
            error_compilation(tab_token[index_tab],"Synthax Error")
        index_tab = index_tab + 1
        return N

    #IMPLICIT ELSE --> Incompatible token
    error_compilation(current_toke,"Synthax Error")


def expr() :
    return expr_launch(1000);

def expr_launch(priority) :

    global index_tab

    #Recup first atom
    A = atom()

    #End of token list ?
    if index_tab < len(tab_token) :
        current_toke = tab_token[index_tab]


        while current_toke.token in binaire_operator and index_tab < len(tab_token)-1:
            #If priority superior
            if binaire_operator[current_toke.token]["priority"] >= priority :
                break


            index_tab = index_tab + 1
            #Simplify reading
            thisPriority = binaire_operator[current_toke.token]["priority"]
            thisAssociativity = binaire_operator[current_toke.token]["associativity"]

            #Build Node (recursif)
            N = BasicNode(current_toke,A,expr_launch(thisPriority + thisAssociativity))
            A = N

            #End toke list ?
            if index_tab < len(tab_token) :
                current_toke = tab_token[index_tab]

    return A
