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
    "toke_add" : "node_add_U",
    "toke_min" : "node_min_U",
    "toke_not" : "node_not_U"
}


#BINAIRE OPERATOR
binaire_operator = {
"toke_pow" : { "type_node" : "node_pow" , "priority" : 1 , "associativity" : 1},
"toke_mult" : { "type_node" : "node_mult" , "priority" : 2 , "associativity" : 0},
"toke_div" : { "type_node" : "node_div" , "priority" : 2 , "associativity" : 0},
"toke_mod" : { "type_node" : "node_mod" , "priority" : 2 , "associativity" : 0},
"toke_add" : { "type_node" : "node_add" , "priority" : 3 , "associativity" : 0},
"toke_min" : { "type_node" : "node_min" , "priority" : 3 , "associativity" : 0}
}

#NODE LINKER OUTPUT CODE
node_linker = {
"node_mult" : "mul.i",
"node_div" : "div.i",
"node_mod" : "mod.i",
"node_add" : "add.i",
"node_min" : "sub.i"
}
