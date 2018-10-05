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
    DEBUG_MSG("Start compilation.","START")

    # Delete old assemblor file (code generate during compilation)
    if os.path.isfile(assemblor_file_name) :
        os.remove(assemblor_file_name)

    # Read source file (to apply the compilation)
    full_test_code =  open(test_code_file, "r")
    lines = full_test_code.readlines()
    full_test_code.close()
    DEBUG_MSG("Source File : "+test_code_file,"INFO")
    DEBUG_MSG("Total lines : "+str(len(lines)),"INFO")

    # Launch lexical analyze
    DEBUG_MSG(debug_mod_line)
    DEBUG_MSG("Start lexical analyse.","START")
    lexique_analyze(lines)
    DEBUG_MSG("End of the lexical analyse.","OK")
    DEBUG_MSG("Token tab built.","TOKENS")
    cpt = 0
    for a_toke in tab_token :
        DEBUG_MSG(str(a_toke),"TOKEN "+str(cpt))
        cpt = cpt + 1

    # Launch synthax analyze (tree recuperation)
    DEBUG_MSG(debug_mod_line)
    DEBUG_MSG("Start synthax analyse.","START")
    racine_synthax = synthax_analyse()
    DEBUG_MSG("End of the synthax analyse.","OK")
    # Display the tree generate

    DEBUG_MSG("Tree built.","TREE")
    DEBUG_MSG("\n" + display_tree(racine_synthax,0))

    # Launch compilation (generation of the assemblor code)
    DEBUG_MSG(debug_mod_line)
    DEBUG_MSG("Start compilation stage.","START")
    compil(racine_synthax)
    DEBUG_MSG("End of the compilation stage.","OK")

    # Evalution of the final result (work only for mathematics expression)
    DEBUG_MSG(str(eval_expr(racine_synthax)),"RESULT")

    DEBUG_MSG(debug_mod_line)
    DEBUG_MSG("Compilation end.","END")
    DEBUG_MSG("Assemblor file (relative PATH) : "+assemblor_file_name,"INFO")


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
