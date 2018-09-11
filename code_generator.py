# - * - * - * - * - * - * - * #
#           IMPORT            #
# - * - * - * - * - * - * - * #

#PERSONNAL MODULE
from conf import *
from node import *
from utils import *

# - * - * - * - * - * - * - * #
#         FUNCTIONS           #
# - * - * - * - * - * - * - * #

def code_generator(node):
    gencode(node)

def gencode(node):
    if node.type == "node_const":
        print "push.i " + str(node.val)

    elif node.type in node_linker:
        gencode(node.childs[0])
        gencode(node.childs[1])
        print node_linker[node.type]

    elif node.type == "node_min_U":
        print "push.i 0"
        gencode(node.childs[0])
        print("sub.i");

    elif node.type == "node_add_U":
        print "push.i 0"
        gencode(node.childs[0])
        print("add.i");
