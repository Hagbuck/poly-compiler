from conf import *
from node import *
from token import *
import datetime

#Return true if param s is an int
def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def error_compilation(token_or_node,msg) :
    #HEADER ERROR MSG
    header_error_msg = "\n\n- * - * - * - * - * - * - * - * - *  -\n"
    header_error_msg += "- * - * - COMPILATION FAILED - * - * -\n"
    header_error_msg += "- * - * - * - * - * - * - * - * - *  -\n"
    #BUILD MSG
    error_msg =  "An error has been detected -> Line "+str(token_or_node.line)
    error_msg +=" & Column "+str(token_or_node.col)+".\n"
    error_msg += msg
    #PRINT
    print header_error_msg + error_msg + "\n\n"
    #SAVE IN LOG & EXIT
    log_msg("ERROR","Error during compilation :"+error_msg)
    exit()


def log_msg(type,msg) :
    if(log_activation == True):
        now = datetime.datetime.now()
        str_now = now.strftime("%d/%m/%Y %H:%M:%S-")
        str_now += str(now.microsecond)
        log_file =  open(log_file_name, "a+")
        log_file.write("["+type+"] - "+str_now+" - "+msg+"\n")
