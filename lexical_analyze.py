# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
#                           Project : Compilateur (Python)                    #
#                                                                             #
#                             File : lexical_analyze.py                       #
#                                                                             #
#                   Description : Lexical analyze file and functions.         #
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
from token import *
from utils import *

# SYSTEM MODULES
import re

# - - - - - - - - - - - - - - - - - #
#           FUNCTIONS               #
# - - - - - - - - - - - - - - - - - #

# Launch the lexical analyze line by line
def lexique_analyze(fullCode) :
    # Index line
    num_line = 1
    # For each lines
    for test_code in fullCode:
        print "\nCURRENT CODE (Line : "+str(num_line)+") : "+test_code
        print " - - - - - - - - - - - - -"
        # Read line and build token
        lexique_analyze_line(test_code,num_line)
        # Next line
        num_line = num_line + 1


# Fill the token tab
def lexique_analyze_line(code,num_line) :

    i = 0
    while i < len(code) : #for each char in expression

        current_char = code[i]

        # Char is a space
        if(current_char == " " or current_char == "\n" or current_char == "\t") :
            current_toke = Token(None,None,None);


        # Char recognized (ONE CHAR)
        elif(current_char in hashmap_toke) :
            current_toke = Token(hashmap_toke[current_char],num_line,i)


        # Other char
        else :

            # Get the complete expression (ex : a word, an number or a keyword)
            word,rank = check_identifier(code[i:])

            # If keyword found
            if word in hashmap_toke :
                current_toke = Token(hashmap_toke[word],num_line,i)

            # If number found
            elif RepresentsInt(word) :
                current_toke = Token("toke_const",num_line,i)
                current_toke.val = int(word)

            # Char unknow --> COMPILATION ERROR
            elif re.match(r"[a-zA-Z0-9_]*",word) == False or word == "" :
                # Take only expression with number, char and underscore
                error_compilation(Token("ERR",num_line,i+1),"Incorrect char detected : "+code[i + rank]+".")

            # Is a identifier
            else :
                current_toke = Token("toke_id",num_line,i)
                current_toke.val = word

            # Go to the next block
            i = i + rank - 1


        # Expression found is a keyword with two char
        if(i+1 < len(code) ):
            if(str(current_char + code[i+1]) in hashmap_toke) :
                current_toke = Token(hashmap_toke[str(current_char + code[i+1])],num_line,i)
                i = i + 1

        # Add the token found if it isn't a None token
        if(current_toke.token != None) :
            tab_token.append(current_toke)

        # Go to the next char
        i = i + 1

# Return a identifier (composed by number or/and letter)
def check_identifier(text) :
    word = ""
    i = 0
    # Regular expression
    while i < len(text) and re.match(r"^[a-zA-Z0-9_]$",text[i]) :
        word += text[i]
        i = i + 1
    return word,i
