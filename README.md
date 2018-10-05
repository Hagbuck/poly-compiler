# Poly-compiler
## *~ A python compiler*

# Description

## Un peu de vocabulaire..
Un **compilateur** est le terme utilisé pour désigner un programme qui transforme un code source écrit dans un langage de programmation en un autre langage informatique.
*~ Source : [Wikipédia](https://fr.wikipedia.org/wiki/Compilateur).*

## Le projet
**Poly-compiler** est un compilateur réalisé en python. Il transforme le langage de programmation respectant les propriétés décrites plus bas en langage pour [automate à pile](https://fr.wikipedia.org/wiki/Automate_%C3%A0_pile). Ce dernier respecte également des propriétés précises exposées ci-dessous.

## Caractéristique


 - **Langage utilisé** ~ Python 2.7.
 - **OS Support** ~ Linux, Windows, Mac. *(peu nécéssité l'installation de python.)*
 - **Programation Objet** ~ Oui
 - **Configuration Possible** ~ Oui

# Utilisation

## Lancer la compilation
- Avec un éditeur de texte de votre choix, éditez le fichier "***test_code.txt***".
- Mettez-vous dans le répertoire du projet et entrez "*python poly-compiler.py*".

## Option
À la suite de la commande citée plus haut, vous pouvez rajouter deux paramètres :
- ***-d*** ~ Active le mode débug. Cette action permet l'affichage de toutes les étapes en détails effectuées durant la compilation.
- ***-l*** ~ Active la sauvegarde de log. Les actions effectuées durant la compilation seront enregistré dans un fichier (par défaut ***compil.log***) vous permettant ainsi de les analyser si besoin.

Ces paramètres :
- Sont **insensibles** à la case.
- Peuvent être mis dans n’importe quel ordre et même concaténés (ex : ***-dl***).

## Configuration
Ce compilateur propose certains paramétrages de configuration. Pour ce faire, ouvrez avec un éditeur de votre choix le fichier ***conf.py***. Attention cependant à ne modifier que ce qu'il y a dans le bloc **ALTERABLE VARS**.
- ***test_code_file*** ~ Par défaut renseigné à **test_code.txt**. Modifiez le paramètre pour changer le fichier source à utiliser pour la compilation.
- ***log_file_name*** ~ Par défaut renseigné à **compil.log**. Modifiez le paramètre pour changer le fichier de sauvegarde des logs.
- ***log_activation*** ~ Par défaut renseigné à **False**. Mettre à **True** pour forcer dans tout les cas la sauvegarde des logs en fichier.
- ***debug_mod*** ~ Par défaut renseigné à **False**. Mettre à **True** pour forcer l'activation du mode debug dans tout les cas.
- ***debug_mod_line*** ~ **ATTENTION**. Séparateur visuel utilisé pour le mod debug et le fichier de sauvegarde des logs. Le modifier pourrait altérer la visibilité des informations.
- ***assemblor_file_name*** ~ Par défaut **assemblor_instruct.txt**. Modifiez le paramètre pour changer de fichier de sortie utilisé pour la compilation et contenant les instructions assembleur.

# Description technique des langages

## Langage de programmation (**INPUT**)
Pour le moment le compilateur ne prend en compte que les expressions mathématiques. Il prend en compte tous les opérateurs unaires, binaires et logiques classiques. Les priorités opératoires sont respectées et les parenthèses sont autorisées.

### Opérateurs unaires
- **-** ~ "moins" unaire.
- **+** ~ "plus" unaire.
- **!** ~ Not.

### Opérateurs binaires
- **+** ~ Addition.
- **-** ~ Soustraction.
- **\*** ~ Multiplication.
- **/** ~ Division.
- **%** ~ Modulo.
- **^** ~ Exponentiel.

## Opérateurs logiques
- **==** ~ Egale.
- **!=** ~ Différent.
- **>** ~ Supérieur.
- **<** ~ Inférieur.
- **>=** ~ Supérieur ou égale.
- **<=** ~ Inférieur ou égale.
- **and** ~ *Et* logique.
- **or** ~ *Ou* logique.


## Langage assembleur (**OUTPUT**)
Le langage assembleur est décrit dans le fichier joint nommé : ***msm_instructs.txt***.
