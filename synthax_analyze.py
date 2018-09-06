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
    return atom()

#Return a tree compose by leave (cont or id) & unaire operator
def atom() :
    #GET GLOBAL VAR
    global index_tab
    current_toke = tab_token[index_tab]

    #UNAIRE OPERATOR
    if current_toke.token in unaire_operator :
        index_tab = index_tab + 1
        current_node = synthax_analyse()
        return NodeUnaire(current_toke,current_node)

    #CONST & ID TOKEN
    elif current_toke.token == "toke_const" or current_toke.token == "toke_id" :
        index_tab = index_tab + 1
        return Node(current_toke)
