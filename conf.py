#contains all tokens
tab_token = []

#parcours tab_token
index_tab = 0

#Code text (TEST)
test_code_file = "test_code.txt"

#LOG INFO
log_file_name = "compil.log"
log_activation = False

#dictionnary of keyord
hashmap_toke = {
#ONE CHAR
"+" : "toke_plus",
"-" : "toke_moins",
"*" : "toke_mult",
"/" : "toke_div",
"^" : "toke_exp",
"=" : "toke_assign",
";" : "toke_semicolon",
">" : "toke_ge",
"<" : "toke_le",
"!" : "toke_not",
"," : "toke_virgule",
"(" : "toke_parantOpen",
")" : "tole_parantClose",
"{" : "toke_braceOpen",
"}" : "toke_braceClose",
"[" : "toke_hookOpen",
"]" : "toke_hookClose",

#TWO CHAR
"==" : "toke_equal",
">=" : "toke_geq",
"<=" : "toke_leq",

#OTHER KEYWORD
"if" : "toke_if",
"else" : "toke_else",
"elif" : "toke_elif",
"while" : "toke_while",
"return" : "toke_return",
"true" : "toke_true",
"false" : "toke_false"
}


#UNAIRE OPERATOR
unaire_operator = {
    "toke_plus" : "node_plus",
    "toke_moins" : "node_moins",
    "toke_not" : "node_not"
}
