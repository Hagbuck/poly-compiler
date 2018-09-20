# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
#                           Project : Compilateur (Python)                    #
#                                                                             #
#                             File : poly-compiler.py                         #
#                                                                             #
#                           Description : Main file project                   #
#                                                                             #
#              Contributors : Corentin TROADEC & Anthony Vuillemin            #
#                                                                             #
#                               Date : September 2018                         #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# - - - - - - - - - - - - - - - - - #
#             IMPORT                #
# - - - - - - - - - - - - - - - - - #

# PROJECT MODULES
from conf import *
from utils import *
from node import *
from token import *
from lexical_analyze import *
from synthax_analyze import *
from code_generator import *

# SYSTEM MODULES
import os

# - - - - - - - - - - - - - - - - - #
#                VARS               #
# - - - - - - - - - - - - - - - - - #

# Globals vars in file "conf.py"
# Please check this file to change the configuration.



# - - - - - - - - - - - - - - - - - #
#                MAIN               #
# - - - - - - - - - - - - - - - - - #
def main():
    log_msg("INFO","Start compilation.")

    # Delete old assemblor file (code generate during compilation)
    if os.path.isfile(assemblor_file_name) :
        os.remove(assemblor_file_name)

    # Read source file (to apply the compilation)
    full_test_code =  open(test_code_file, "r")
    lines = full_test_code.readlines()
    full_test_code.close()

    # Launch lexical analyze
    lexique_analyze(lines)

    # Launch synthax analyze (tree recuperation)
    racine_synthax = synthax_analyse()
    # Display the tree generate
    display_tree(racine_synthax,0)

    # Launch compilation (generation of the assemblor code)
    compil(racine_synthax)

    # Evalution of the final result (work only for mathematics expression)
    print "[RESULT] -> " +str(eval_expr(racine_synthax))

    log_msg("INFO","Compilation end.")


if __name__ == "__main__":
    # Execute only if run as a script
    main()
