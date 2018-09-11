# - * - * - * - * - * - * - * #
#           IMPORT            #
# - * - * - * - * - * - * - * #

#PERSONNAL MODULES
from conf import *
from token import *
from utils import *
#OTHER
import re

# - * - * - * - * - * - * - * #
#         FUNCTIONS           #
# - * - * - * - * - * - * - * #

#Launch the lexical analyze line by line
def lexique_analyze(fullCode) :
    num_line = 1
    for test_code in fullCode:
        print "\nTEST CODE (Line : "+str(num_line)+") : "+test_code
        print " - - - - - - - - - - - - -"
        lexique_analyze_line(test_code,num_line)
        num_line = num_line + 1


#Fill the token tab with param code = a line
def lexique_analyze_line(code,num_line) :

    #char by char
    i = 0
    while i < len(code) :
    #for i in range(len(code)) :
        current_char = code[i]

        #space
        if(current_char == " " or current_char == "\n" or current_char == "\t") :
            current_toke = Token(None,None,None);


        #know char (for one char)
        elif(current_char in hashmap_toke) :
            current_toke = Token(hashmap_toke[current_char],num_line,i)


        #other char
        else :
            #Get the word identify
            word,rank = check_identifier(code[i:])

            #If keyword
            if word in hashmap_toke :
                current_toke = Token(hashmap_toke[word],num_line,i)

            #If int
            elif RepresentsInt(word) :
                current_toke = Token("toke_const",num_line,i)
                current_toke.val = int(word)

            #unknow char --> COMPILATION ERROR
            elif re.match(r"[a-zA-Z0-9_]*",word) == False or word == "" :
                error_compilation(Token("ERR",num_line,i+1),"Incorrect char detected : "+code[i + rank]+".")

            #identifier
            else :
                current_toke = Token("toke_id",num_line,i)
                current_toke.val = word

            #go next block
            i = i + rank - 1


        #keyword with two char
        if(i+1 < len(code) ):
            if(str(current_char + code[i+1]) in hashmap_toke) :
                current_toke = Token(hashmap_toke[str(current_char + code[i+1])],num_line,i)
                i = i + 1

        #Add in tab if this is a true token
        if(current_toke.token != None) :
            tab_token.append(current_toke)
            #print current_toke

        #next element
        i = i + 1

#Return the identifier (composed by number or/and letter)
def check_identifier(text) :
    word = ""
    i = 0
    #expression reg
    while i < len(text) and re.match(r"^[a-zA-Z0-9_]$",text[i]) :
        word += text[i]
        i = i + 1
    return word,i
