# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
#                           Project : Compilateur (Python)                    #
#                                                                             #
#                                   File : utils.py                           #
#                                                                             #
# Description : Contain all the differents utils use during the compilation.  #
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

# SYSTEM MODULES
import datetime


# - - - - - - - - - - - - - - - - - #
#           FUNCTIONS               #
# - - - - - - - - - - - - - - - - - #

# Return true if param s is an int
def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

# Exit the program and give information about an error during the compilation
def error_compilation(token_or_node,msg) :
    # HEADER ERROR MSG
    header_error_msg = '\033[91m'+"\n+ ----------------------------------- +\n"
    header_error_msg +=    "| ....... COMPILATION FAILED ........ | \n"
    header_error_msg +=    "+ ----------------------------------- +\n"+'\033[0m'
    # BUILD MSG
    error_msg = "[ERROR] ~ " + msg +"\n"
    error_msg +=  "[ERROR] ~ An error has been detected : Line "+str(token_or_node.line)
    error_msg +=" & Column "+str(token_or_node.col)+"."
    error_msg += "\n[ERROR] ~ "+str(token_or_node)
    #P RINT
    print header_error_msg + '\033[93m' + error_msg +'\033[0m'
    # SAVE IN LOG & EXIT
    log_msg("ERROR","Error during compilation :\n"+error_msg,True)
    log_msg("END / ERROR","Compilation end with an error statement.",True)
    print '\033[91m'+ "[END / ERROR] ~ Compilation end with an error statement.\n" +'\033[0m'
    exit()


# Write logs in an file
def log_msg(type,msg, compil_error = False) :
    # Already display when this is a compilation error msg.
    if compil_error == False :
        print "["+type+"] ~ " + msg

    if(log_activation == True):
        now = datetime.datetime.now()
        str_now = now.strftime("%d/%m/%Y %H:%M:%S-")
        str_now += str(now.microsecond)
        log_file =  open(log_file_name, "a+")
        log_file.write("["+type+"] - "+str_now+" ~ "+msg+"\n")


# Active debug mod
def active_debug_mod() :
    global debug_mod
    debug_mod = True

# Return debug mod statement
def stat_debug_mode() :
    return debug_mod

# Display debug message if debug mod is on
def DEBUG_MSG(msg,type = "") :
    # debug mod on ?
    if debug_mod == True :
        if type != "" :
            print "["+type+"] ~ "+msg
        else :
            print msg

# Active debug mod
def active_log_save() :
    global log_activation
    log_activation = True

# Write an instruction (assemblor) in the specific file
def write_assemblor_file(text) :
    ass_file = open(assemblor_file_name,"a+")
    ass_file.write(text+"\n")

# Give the result of the expression pass
def eval_expr(node) :
    #CONST
    if node.type == "node_const" :
        return node.val

    #UNAIRE OPERATOR
    elif node.type == "node_add_U" :
        return eval_expr(node.childs[0])
    elif node.type == "node_min_U" :
        return - eval_expr(node.childs[0])
    #!
    elif node.type == "node_not_U" :
        if eval_expr(node.childs[0]) == 0 :
            return 1
        else :
            return 0

    #BINAIRE NATURAL OPERATOR
    elif node.type == "node_add" :
        return eval_expr(node.childs[0]) + eval_expr(node.childs[1])
    elif node.type == "node_min" :
        return eval_expr(node.childs[0]) - eval_expr(node.childs[1])
    elif node.type == "node_mult" :
        return eval_expr(node.childs[0]) * eval_expr(node.childs[1])
    elif node.type == "node_div" :
        return eval_expr(node.childs[0]) / eval_expr(node.childs[1])
    elif node.type == "node_pow" :
        return pow(eval_expr(node.childs[0]),eval_expr(node.childs[1]))

    #BINAIRE LOGIC OPERATOR
    elif node.type == "node_equal" :
        return booleanToInt(eval_expr(node.childs[0]) == eval_expr(node.childs[1]))
    elif node.type == "node_le" :
        return booleanToInt(eval_expr(node.childs[0]) < eval_expr(node.childs[1]))
    elif node.type == "node_ge" :
        return booleanToInt(eval_expr(node.childs[0]) > eval_expr(node.childs[1]))
    elif node.type == "node_geq" :
        return booleanToInt(eval_expr(node.childs[0]) >= eval_expr(node.childs[1]))
    elif node.type == "node_leq" :
        return booleanToInt(eval_expr(node.childs[0]) <= eval_expr(node.childs[1]))
    elif node.type == "node_diff" :
        return booleanToInt(eval_expr(node.childs[0]) != eval_expr(node.childs[1]))
    elif node.type == "node_and" :
        return booleanToInt(eval_expr(node.childs[0]) and eval_expr(node.childs[1]))
    elif node.type == "node_or" :
        return booleanToInt(eval_expr(node.childs[0]) or eval_expr(node.childs[1]))


# Convert boolean to Int
# OR et AND attention evaluation - en python tout les enfants ne sont pas evalues
def booleanToInt(p_bool) :
    if(p_bool) :
        return 1
    else :
        return 0
