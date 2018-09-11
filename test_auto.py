#NATIVE MODULE


#PERSONNAL MODULE
from conf import *
from utils import *
from node import *
from token import *
from lexical_analyze import *
from synthax_analyze import *


code_src_test = [
    {"src" : "5 * 2 - 4 / 2" , "res" : 5 * 2 - 4 / 2},
    {"src" : "5 * (2 - 4) / 2" , "res" : 5 * (2 - 4) / 2},
    {"src" : "-5 * (-2 - 4) / 2" , "res" : -5 * (-2 - 4) / 2},
    {"src" : "-55", "res" : -55},
    {"src" : "--55", "res" : 55},
    {"src" : "-+-55", "res" : 55},
    {"src" : "!0" , "res" : 1},
    {"src" : "!256" , "res" : 0},
    {"src" : "!-256" , "res" : 0},
    {"src" : "!!256" , "res" : 1},
    {"src" : "5 ^ 2 ^ 2" , "res" : pow(5, pow(2, 2))}
    ]



for i in range(0,len(code_src_test) ) :
    lexique_analyze_line(code_src_test[i]["src"],1)
    arbre = synthax_analyse()
    res = eval_expr(arbre)
    if res == code_src_test[i]["res"] :
        print "[CODE "+str(i)+"] ~ [VALIDE] ~ ("+code_src_test[i]["src"]+") = "+str(code_src_test[i]["res"])
    else :
        print '\033[91m' + "[CODE "+str(i)+"] ~ [ERROR] ~ ("+code_src_test[i]["src"]+") !=  "+str(res)+" [RES = "+str(code_src_test[i]["res"])+"]" + '\033[0m'
    #RESET TAB
    tab_token = []
    index_tab = 0
