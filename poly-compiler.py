# - * - * - * - * - * - * - * #
#           IMPORT            #
# - * - * - * - * - * - * - * #
#PERSONNAL MODULE
from conf import *
from utils import *
from node import *
from token import *
from lexical_analyze import *
from synthax_analyze import *


# - * - * - * - * - * - * - * #
#           VARS              #
# - * - * - * - * - * - * - * #

#! consult "conf.py" for global vars



# - * - * - * - * - * - * - * #
#            MAIN             #
# - * - * - * - * - * - * - * #
def main():
    log_msg("INFO","Start compilation.")

    #OPEN FILE
    full_test_code =  open(test_code_file, "r")
    lines = full_test_code.readlines()
    full_test_code.close()
    #LEXICAL ANALYZE
    lexique_analyze(lines)
    #SYNTHAX ANALYZE
    racine_synthax = synthax_analyse()
    display_tree(racine_synthax,0)

    #DISPLAY RESULT
    print "[RESULT] -> " +str(eval_expr(racine_synthax))
    log_msg("INFO","Compilation end.")


if __name__ == "__main__":
    # execute only if run as a script
    main()
