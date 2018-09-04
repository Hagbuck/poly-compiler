# Poly - Compiler
# 4/9/2018
# Troadec & Vuillemin

tokens_type = {
    '+'     :   'tok_plus',
    '-'     :   'tok_less',
    '*'     :   'tok_multiply',
    '/'     :   'tok_divide',
    '%'     :   'tok_modulo',
    '='     :   'tok_affect',
    '>'     :   'tok_gt',
    '<'     :   'tok_lt',
    '('     :   'tok_bracket_op',
    ')'     :   'tok_bracket_cl',
    ';'     :   'tok_semicolomn',

    '=='    :   'tok_equals',
    '!='    :   'tok_diff',
    '>='    :   'tok_geq',
    '<='    :   'tok_leq'
}

class Token:
    def __init__(self):
        self.type   = None
        self.value  = None
        self.row    = None
        self.col    = None

    def __init__(self, token_type, value, row, col):
        self.type   = token_type
        self.value  = value
        self.row    = row
        self.col    = col

    def set_value(self, value):
        self.value = value

    def set_type(self, token_type):
        self.type = token_type

    def set_row(self, row):
        self.row = row

    def set_col(self, col):
        self.col = col

    def __str__(self):
        return '[' + str(self.type) + '] \t: ' + str(self.value) + '\t('+ str(self.row) + ':' + str(self.col) +')'

def main():
    str_input = 'toto == a_B_c >= 12'

    Tokens_list = []

    row = 0
    col = 0

    i = 0

    while i < len(str_input):

        char = str_input[i]
        # SI LE CARACTERE N'EST PAS UN ESPACE
        if char != ' ' and char != '\t' and char != '\n':

            token_type_find = False

            # ON ESSAYE DE LIRE DEUX CARACTERE
            if i + 1 < len(str_input):
                next_char = str_input[i + 1]

                # SI LE DEUXIEME CARACTERE N'EST PAS UN ESPACE
                if next_char != ' ' and next_char != '\t' and next_char != '\n':

                    # SI LE DOUBLE CARACTERE EXISTE
                    tok_type = char + next_char;
                    if tok_type in tokens_type:
                        Tokens_list.append(Token(tokens_type[tok_type], None, row, col))
                        token_type_find = True
                        i += 1 # On avance sur le prochain caractere
                        col += 1

            # SI L'INSERTION EN DOUBLE A ECHOUER
            if token_type_find == False:

                # SI LE CARACTERE EST UN OPERATOR CONNUE
                if char in tokens_type:
                    Tokens_list.append(Token(tokens_type[char], None, row, col))
                
                # SI LE CARACTERE EST UNE LETTRE, UN NOMBRE, OU UN INCONNUE
                else:
                    # SI LE CARACTERE EST UNE LETTRE
                    if char >= 'a' and char <= 'z' or char >= 'A' and char <= 'Z' or char == '_':
                        
                        string = char
                        i += 1
                        while i < len(str_input):

                            char_read = str_input[i]
                            if char_read >= 'a' and char_read <= 'z' or char_read >= 'A' and char_read <= 'Z' or char_read >= '0' and char_read <= '9' or char_read == '_':
                                string += char_read
                            else:
                                break;
                            i += 1
                            
                        Tokens_list.append(Token('tok_ident', string, row, col))

                    # SI LE CARACTERE EST UN NOMBRE
                    elif char >= '0' and char <= '9':

                        string = char
                        i += 1
                        while i < len(str_input):

                            char_read = str_input[i]
                            if char_read >= '0' and char_read <= '9':
                                string += char_read
                            else:
                                break;
                            i += 1

                        Tokens_list.append(Token('tok_const', string, row, col))

                    else:
                        print 'ERR : Invalid char at : (' + row + ':' + col + ')' 

        i += 1
        col += 1
        if char == '\n':
            row += 1
            col = 0

    for Tok in Tokens_list:
        print Tok

if __name__ == '__main__':
    main()