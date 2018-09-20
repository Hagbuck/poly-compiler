#NATIVE MODULE


#PERSONNAL MODULE
from conf import *
from utils import *
from node import *
from token import *
from lexical_analyze import *
from synthax_analyze import *

test_natural_operator = True
test_logic_operator   = True

#TEST NATURAL OPERATOR (UNAIRE & BINAIRE)
code_src_test_natural_operator = [
    {"src" : "5 * 2 - 4 / 2" , "res" : 5 * 2 - 4 / 2},
    {"src" : "5 * (2 - 4) / 2" , "res" : 5 * (2 - 4) / 2},
    {"src" : "-5 * (-2 - 4) / 2" , "res" : -5 * (-2 - 4) / 2},
    {"src" : "(5 + 5) * (3 - 1)" , "res" : (5 + 5) * (3 - 1)},
    {"src" : "-55", "res" : -55},
    {"src" : "--55", "res" : 55},
    {"src" : "-+-55", "res" : 55},
    {"src" : "!0" , "res" : 1},
    {"src" : "!256" , "res" : 0},
    {"src" : "!-256" , "res" : 0},
    {"src" : "!!256" , "res" : 1},
    {"src" : "5 ^ 2 ^ 2" , "res" : pow(5, pow(2, 2))},
    {"src" : "(5 ^ 2) ^ 2" , "res" : pow(pow(5,2),2)}
    ]

#TEST LOGIC OPERATOR
code_src_test_logic_operator = [
    #TEST SIMPLE
    {"src" : "5 and 5" , "res" : 1},
    {"src" : "5 == 5" , "res" : 1},
    {"src" : "5 != 5" , "res" : 0},
    {"src" : "5 <= 5" , "res" : 1},
    {"src" : "5 >= 5" , "res" : 1},
    {"src" : "5 < 6" , "res" : 1},
    {"src" : "5 > 6" , "res" : 0},
    {"src" : "5 <= 6" , "res" : 1},
    {"src" : "5 >= 6" , "res" : 0},
    {"src" : "5 or 6" , "res" : 1},

    #TEST COMPLEX
    {"src" : "(5 != 6) and (5 < 6)" , "res" : 1},
    {"src" : "(5 != 6) and (5 > 6)" , "res" : 0},
    {"src" : "(5 != 6) or (5 < 6)" , "res" : 1},
    {"src" : "(5 != 6) or (5 > 6)" , "res" : 1},
    {"src" : "(5 != 5) or (5 < 6)" , "res" : 1},
    {"src" : "(5 != 5) or (5 > 6)" , "res" : 0},
    ]

if test_natural_operator :
    print "==================================="
    print "====== TEST NATURAL OPERATOR ======"
    print "==================================="

    for i in range(0,len(code_src_test_natural_operator) ) :
        lexique_analyze_line(code_src_test_natural_operator[i]["src"],1)
        arbre = synthax_analyse()
        res = eval_expr(arbre)
        if res == code_src_test_natural_operator[i]["res"] :
            print "[CODE "+str(i)+"] ~ [VALIDE] ~ "+code_src_test_natural_operator[i]["src"]+" [=] "+str(code_src_test_natural_operator[i]["res"])
        else :
            print '\033[91m' + "[CODE "+str(i)+"] ~ [ERROR] ~ "+code_src_test_natural_operator[i]["src"]+" [!=]  "+str(res)+" [RES = "+str(code_src_test_natural_operator[i]["res"])+"]" + '\033[0m'
        #RESET TAB
        tab_token = []
        index_tab = 0


if test_logic_operator :
    print "==================================="
    print "======= TEST LOGIC OPERATOR ======="
    print "==================================="

    for i in range(0,len(code_src_test_logic_operator) ) :
        lexique_analyze_line(code_src_test_logic_operator[i]["src"],1)
        arbre = synthax_analyse()
        res = eval_expr(arbre)
        if res == code_src_test_logic_operator[i]["res"] :
            print "[CODE "+str(i)+"] ~ [VALIDE] ~ "+code_src_test_logic_operator[i]["src"]+" [=] "+str(code_src_test_logic_operator[i]["res"])
        else :
            print '\033[91m' + "[CODE "+str(i)+"] ~ [ERROR] ~ "+code_src_test_logic_operator[i]["src"]+" [!=]  "+str(res)+" [RES = "+str(code_src_test_logic_operator[i]["res"])+"]" + '\033[0m'
        #RESET TAB
        tab_token = []
        index_tab = 0
