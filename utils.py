# - * - * - * - * - * - * - * #
#           IMPORT            #
# - * - * - * - * - * - * - * #
from conf import *
from node import *
from token import *
import datetime


# - * - * - * - * - * - * - * #
#         FUNCTIONS           #
# - * - * - * - * - * - * - * #
#Return true if param s is an int
def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

#Exit the program and give information about an error during the compilation
def error_compilation(token_or_node,msg) :
    #HEADER ERROR MSG
    header_error_msg = '\033[91m'+"\n+ ----------------------------------- +\n"
    header_error_msg +=    "| ....... COMPILATION FAILED ........ | \n"
    header_error_msg +=    "+ ----------------------------------- +\n"+'\033[0m'
    #BUILD MSG
    error_msg = "[ERROR] ~ " + msg +"\n"
    error_msg +=  "[ERROR] ~ An error has been detected : Line "+str(token_or_node.line)
    error_msg +=" & Column "+str(token_or_node.col)+".\n"
    #PRINT
    print header_error_msg + '\033[93m' + error_msg +'\033[0m'
    #SAVE IN LOG & EXIT
    log_msg("ERROR","Error during compilation :"+error_msg)
    exit()


#Write logs in an file
def log_msg(type,msg) :
    if(log_activation == True):
        now = datetime.datetime.now()
        str_now = now.strftime("%d/%m/%Y %H:%M:%S-")
        str_now += str(now.microsecond)
        log_file =  open(log_file_name, "a+")
        log_file.write("["+type+"] - "+str_now+" - "+msg+"\n")


def write_assemblor_file(text) :
    #print text + "\n"
    ass_file = open(assemblor_file_name,"a+")
    ass_file.write(text+"\n")

#Give the result of the expression
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

    #BINAIRE
    elif node.type == "node_add" :
        return eval_expr(node.childs[0]) + eval_expr(node.childs[1])
    elif node.type == "node_min" :
        return eval_expr(node.childs[0]) - eval_expr(node.childs[1])
    elif node.type == "node_mult" :
        return eval_expr(node.childs[0]) * eval_expr(node.childs[1])
    elif node.type == "node_div" :
        return eval_expr(node.childs[0]) / eval_expr(node.childs[1])

    #OTHER
