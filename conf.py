# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
#                           Project : Compilateur (Python)                    #
#                                                                             #
#                                   File : conf.py                            #
#                                                                             #
#                           Description : Configuration file                  #
#                                                                             #
#              Contributors : Corentin TROADEC & Anthony Vuillemin            #
#                                                                             #
#                               Date : September 2018                         #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# - - - - - - - - - - - - - - - - - #
#         ALTERABLE VARS            #
# - - - - - - - - - - - - - - - - - #

# Code source file use
test_code_file = "test_code.txt"

# Log informations (save log in a file) - True tu force save, -l in console
log_file_name = "compil.log"    # File use to save log
log_activation = False          # Active log (display on console & save on file)

# Debug mod (active debug informations) - True to force debug, -d in console.
debug_mod = False

# File use to save the generated codee (Assemblor instruction)
assemblor_file_name = "../MSM/assemblor_instruct.txt"


# - - - - - - - - - - - - - - - - - #
#        INALTERABLE VARS           #
# - - - - - - - - - - - - - - - - - #

# IMPORTANT : Please don't modified this informations.

# Table use to contains all the token
tab_token = []

# Sharing index in order to browse the tab
index_tab = 0

# Dictionnary with all the keyword of our langage
# A particular symbol is associate with a token id
# symbol --> token
hashmap_toke = {
# Symbole with one char
"+" : "toke_add",
"-" : "toke_min",
"*" : "toke_mult",
"/" : "toke_div",
"^" : "toke_pow",
"%" : "toke_mod",
"=" : "toke_assign",
";" : "toke_semicolon",
">" : "toke_ge",
"<" : "toke_le",
"!" : "toke_not",
"," : "toke_virgule",
"(" : "toke_parantOpen",
")" : "toke_parantClose",
"{" : "toke_braceOpen",
"}" : "toke_braceClose",
"[" : "toke_hookOpen",
"]" : "toke_hookClose",

# Symbole with two chars
"==" : "toke_equal",
">=" : "toke_geq",
"<=" : "toke_leq",
"!=" : "toke_diff",

# Other keywords
"if" : "toke_if",
"else" : "toke_else",
"elif" : "toke_elif",
"while" : "toke_while",
"return" : "toke_return",
"true" : "toke_true",
"false" : "toke_false",
"and" : "toke_and",
"or" : "toke_or"
}


# UNAIRE OPERATOR (Dictionnary token --> node)
unaire_operator = {
    "toke_add" : "node_add_U",
    "toke_min" : "node_min_U",
    "toke_not" : "node_not_U"
}


#BINAIRE OPERATOR (Dictionnary token --> node)
binaire_operator = {

# Mathematic operators
"toke_pow" : { "type_node" : "node_pow" , "priority" : 1 , "associativity" : 1},
"toke_mult" : { "type_node" : "node_mult" , "priority" : 2 , "associativity" : 0},
"toke_div" : { "type_node" : "node_div" , "priority" : 2 , "associativity" : 0},
"toke_mod" : { "type_node" : "node_mod" , "priority" : 2 , "associativity" : 0},
"toke_add" : { "type_node" : "node_add" , "priority" : 3 , "associativity" : 0},
"toke_min" : { "type_node" : "node_min" , "priority" : 3 , "associativity" : 0},

# Logic operators
"toke_equal" : { "type_node" : "node_equal" , "priority" : 4 , "associativity" : 0},
"toke_diff" : { "type_node" : "node_diff" , "priority" : 4 , "associativity" : 0},
"toke_geq" : { "type_node" : "node_geq" , "priority" : 4 , "associativity" : 0},
"toke_leq" : { "type_node" : "node_leq" , "priority" : 4 , "associativity" : 0},
"toke_ge" : { "type_node" : "node_ge" , "priority" : 4 , "associativity" : 0},
"toke_le" : { "type_node" : "node_le" , "priority" : 4 , "associativity" : 0},

# "AND" & "OR" operators
"toke_and" : { "type_node" : "node_and" , "priority" : 5 , "associativity" : 0},
"toke_or" : { "type_node" : "node_or" , "priority" : 6 , "associativity" : 0}
}


# Node to assemblor instruction dictionnary
# (Dictionnary node --> assemblor instruction)
dict_bin_node_to_assemblor = {

# Mathematic operators
"node_add" : "add.i",
"node_min" : "sub.i",
"node_mult" : "mul.i",
"node_div" : "div.i",
"node_mod" : "mod.i",

# Logic operators
"node_equal" : "cmpeq.i",
"node_le" : "cmplt.i",
"node_ge" : "cmpgt.i",
"node_geq" : "cmpge.i",
"node_leq" : "cmple.i",
"node_diff" : "cmpne.i",
"node_and" : "and",
"node_or" : "or"
}
