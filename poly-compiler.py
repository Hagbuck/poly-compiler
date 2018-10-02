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
import sys

# - - - - - - - - - - - - - - - - - #
#                VARS               #
# - - - - - - - - - - - - - - - - - #

# Globals vars in file "conf.py"
# Please check this file to change the configuration.



# - - - - - - - - - - - - - - - - - #
#                MAIN               #
# - - - - - - - - - - - - - - - - - #
def main():
    log_msg("START","Start compilation.")

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

    if stat_debug_mode() :
        display_tree(racine_synthax,0)

    # Launch compilation (generation of the assemblor code)
    compil(racine_synthax)

    # Evalution of the final result (work only for mathematics expression)
    DEBUG_MSG(str(eval_expr(racine_synthax)),"RESULT")

    log_msg("END","Compilation end.")
    log_msg("INFO","Assemblor file (relative PATH) : "+assemblor_file_name)


# Execute only if run as a script
if __name__ == "__main__":

    # Active debug mod ?
    #if len(sys.argv) > 1 :

    for arg in sys.argv :

        if arg.lower() == "-d"  :
            active_debug_mod()
            DEBUG_MSG("DEBUG MOD : ON.","INFO")

        elif arg.lower() == "-l" :
            active_log_save()
            DEBUG_MSG("LOG SAVE : ON.","INFO")

        elif arg.lower() == "-ld" or arg == "-dl" :
            active_debug_mod()
            active_log_save()
            DEBUG_MSG("DEBUG MOD : ON.","INFO")
            DEBUG_MSG("LOG SAVE : ON.","INFO")

        elif arg != sys.argv[0] :
            print "[WARN] ~ Unknow console parameter : "+arg

    # Main process
    main()
