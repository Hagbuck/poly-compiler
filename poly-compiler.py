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
from sem_analyze import *
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
    used_file = used_src_file()
    # Look for lines
    full_test_code =  open(used_file, "r")
    lines = full_test_code.readlines()
    # Look for all content (copy)
    save_file_content = open(used_file, "r")
    file_content = save_file_content.read()

    # Verify if the file is not empty
    if len(lines) == 0 or len(file_content.split()) == 0 :
        error_compilation(Token(None,0,0),"Empty file.")

    # Close file
    full_test_code.close()
    save_file_content.close()

    DEBUG_MSG("Source File : "+used_file,"INFO")
    DEBUG_MSG("Total lines : "+str(len(lines)),"INFO")

    # Launch lexical analyze
    DEBUG_MSG(debug_mod_line)
    DEBUG_MSG("Start lexical analyse.","START")
    lexique_analyze(lines)
    DEBUG_MSG("End of the lexical analyse.","OK")
    DEBUG_MSG(debug_mod_line)
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

    DEBUG_MSG(debug_mod_line)
    DEBUG_MSG("Start semantic analyze.", "START")
    semantic_analyze(racine_synthax)

    # Verify main is prensent
    mainPresent = False
    for i in range(0,racine_synthax.nbChild) :
        if racine_synthax.childs[i].val == "main" :
            mainPresent = True

    if mainPresent == False:
        error_compilation(Token(None,0,0),"No main function detected. Invalid Compilation.")

    # Continue
    DEBUG_MSG("End of the semantic analyze", "OK")
    DEBUG_MSG("Tree built.","TREE")
    DEBUG_MSG(debug_mod_line)
    DEBUG_MSG("\n" + display_tree(racine_synthax,0))

    # Launch compilation (generation of the assemblor code)
    DEBUG_MSG(debug_mod_line)
    DEBUG_MSG("Start compilation stage.","START")
    DEBUG_MSG(debug_mod_line)
    DEBUG_MSG(compil(racine_synthax))
    DEBUG_MSG(debug_mod_line)
    DEBUG_MSG("End of the compilation stage.","OK")


    DEBUG_MSG(debug_mod_line)
    DEBUG_MSG("Compilation end.","END")
    DEBUG_MSG("Assemblor file (relative PATH) : "+assemblor_file_name,"INFO")
    DEBUG_MSG(debug_mod_line)


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
            if os.path.isfile(arg) :
                DEBUG_MSG("Use an external file : "+arg,"INFO")
                change_src_file(arg)
            else :
                print "[WARN] ~ Unknow console parameter : "+arg

    # Main process
    main()
