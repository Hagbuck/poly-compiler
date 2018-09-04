# - * - * - * - * - * - * - * #
#           IMPORT            #
# - * - * - * - * - * - * - * #
import re


# - * - * - * - * - * - * - * #
#           CLASS             #
# - * - * - * - * - * - * - * #

#CLASS TOKEN
class Token :
    #Declaration
    def __init__(self,token,line,col) :
        self.val = None
        self.token = token
        self.line = line
        self.col = col

    #Give a val (optionnal)
    def set_val(val) :
        self.val = val

    #For display token
    def __str__(self) :
        return "["+str(self.token)+"] - "+str(self.val)+" - ("+str(self.line)+";"+str(self.col)+")"

# - * - * - * - * - * - * - * #
#           VARS              #
# - * - * - * - * - * - * - * #

#contains all tokens
tab_token = []

#Code text (TEST)
test_code = "if(a == b)c=123"

#dictionnary of keyord
hashmap_toke = {
#ONE CHAR
"+" : "toke_plus",
"-" : "toke_mois",
"*" : "toke_mult",
"/" : "toke_div",
"=" : "toke_assign",
";" : "toke_semicolon",
">" : "toke_ge",
"<" : "toke_le",
"(" : "toke_parantOpen",
")" : "tole_parantClose",

#TWO CHAR
"==" : "toke_equal",
">=" : "toke_geq",
"<=" : "toke_leq",

#OTHER KEYWORD
"if" : "toke_if",
"else" : "toke_else",
"elif" : "toke_elif",
"while" : "toke_while"
}

# - * - * - * - * - * - * - * #
#         FUNCTIONS           #
# - * - * - * - * - * - * - * #

#Verify if param s is an int
def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

#Fill the token tab with param code
def lexique_analyze(code) :

    #char by char
    i = 0
    while i < len(code) :
    #for i in range(len(code)) :
        current_char = code[i]

        #space
        if(current_char == " ") :
            current_toke = Token(None,None,None);


        #know char (for one char)
        elif(current_char in hashmap_toke) :
            current_toke = Token(hashmap_toke[current_char],1,i)


        #other char
        else :
            #Get the word identify
            word,rank = check_identifier(code[i:])

            #If keyword
            if word in hashmap_toke :
                current_toke = Token(hashmap_toke[word],1,i)

            #If int
            elif RepresentsInt(word) :
                current_toke = Token("toke_const",1,i)
                current_toke.val = int(word)

            #identifier
            else :
                current_toke = Token("toke_id",1,i)
                current_toke.val = word
            #go next block
            i = i + rank - 1


        #keyword with two char
        if(i+1 < len(code) ):
            if(str(current_char + code[i+1]) in hashmap_toke) :
                current_toke = Token(hashmap_toke[str(current_char + code[i+1])],1,i)
                i = i + 1

        #Add in tab if this is a true token
        if(current_toke.token != None) :
            tab_token.append(current_toke)
            print current_toke

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


# - * - * - * - * - * - * - * #
#            MAIN             #
# - * - * - * - * - * - * - * #
def main():
    print "TEST CODE : "+test_code
    print " - - - - - - - - - - - - -"
    lexique_analyze(test_code)
    print " - - - - - - - - - - - - -"

if __name__ == "__main__":
    # execute only if run as a script
    main()
