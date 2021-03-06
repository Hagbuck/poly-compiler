# Poly-compiler
## *\~ A python compiler*


<!--ts-->
   * [Description](#description)
      * [Un peu de vocabulaire.](#un-peu-de-vocabulaire)
      * [Le projet](#le-projet)
      * [Caractéristique](#caractéristique)
   * [Utilisation](#utilisation)
      * [Lancer la compilation](#lancer-la-compilation)
      * [Option](#option)
      * [Configuration](#configuration)
      * [Exécution du code compilé](#exécution-du-code-compilé)
         * [Installation de l'environnement (<strong>Linux</strong>)](#installation-de-lenvironnement-linux)
         * [Exécuter le code compilé (<strong>Linux</strong>)](#exécuter-le-code-compilé-linux)
   * [Description technique des langages](#description-technique-des-langages)
      * [Langage de programmation (<strong>INPUT</strong>)](#langage-de-programmation-input)
         * [Opérateurs unaires](#opérateurs-unaires)
         * [Opérateurs binaires](#opérateurs-binaires)
        * [Opérateurs logiques](#opérateurs-logiques)
        * [Variables et Fonctions](#variables-et-fonctions)
        * [Boucles](#boucles)
        * [Autres](#autres)
        * [Commenaire](#commentaire)
      * [Langage assembleur (<strong>OUTPUT</strong>)](#langage-assembleur-output)
   * [Erreur de compilation prise en compte](#erreur-de-compilation-prise-en-compte)
<!--te-->


# Description

## Un peu de vocabulaire.
Un **compilateur** est le terme utilisé pour désigner un programme qui transforme un code source écrit dans un langage de programmation en un autre langage informatique. *\~ Source : [Wikipédia](https://fr.wikipedia.org/wiki/Compilateur).*

## Le projet
**Poly-compiler** est un compilateur réalisé en python. Il transforme le langage de programmation respectant les propriétés décrites plus bas en langage pour [automate à pile](https://fr.wikipedia.org/wiki/Automate_%C3%A0_pile). Ce dernier respecte également des propriétés précises exposées ci-dessous.

## Caractéristique

 - **Langage utilisé** ~ Python 2.7.
 - **OS Support** ~ Linux, Windows, Mac. *(peu nécéssité l'installation de python.)*
 - **Configuration Possible** ~ Oui

# Utilisation

## Lancer la compilation
- Avec un éditeur de texte de votre choix, éditez le fichier "***test_code.txt***".
- Déplacez-vous dans le répertoire du projet et entrez "***python poly-compiler.py***".

## Option
À la suite de la commande d'exécution du compilateur, vous pouvez rajouter deux paramètres :
- ***-d*** ~ Active le mode débug. Cette action permet l'affichage de toutes les étapes en détails effectuées durant la compilation.
- ***-l*** ~ Active la sauvegarde de log. Les actions effectuées durant la compilation seront enregistré dans un fichier (par défaut ***compil.log***) vous permettant ainsi de les analyser si besoin.

Ces paramètres :
- Sont **insensibles** à la case.
- Peuvent être mis dans n’importe quel ordre et même concaténés (ex : ***-dL***).

Vous pouvez également lancer la compilation d'un fichier en ligne de commande en renseignant directement le **PATH** associé en paramètre.

Exemple :
``python poly-compiler -dl /sample/my_src_file.txt``

## Configuration
Ce compilateur propose certains paramétrages de configuration. Pour ce faire, ouvrez avec un éditeur de votre choix le fichier ***conf.py***. Attention cependant à ne modifier que ce qu'il y a dans le bloc **ALTERABLE VARS**.
- ***test_code_file*** ~ Par défaut renseigné à **test_code.txt**. Modifiez le paramètre pour changer le fichier source à utiliser pour la compilation. ***Non prioritaire si un fichier source est renseigné en paramètre de la ligne de commande.***
- ***log_file_name*** ~ Par défaut renseigné à **compil.log**. Modifiez le paramètre pour changer le fichier de sauvegarde des logs.
- ***log_activation*** ~ Par défaut renseigné à **False**. Mettre à **True** pour forcer dans tout les cas la sauvegarde des logs en fichier.
- ***debug_mod*** ~ Par défaut renseigné à **False**. Mettre à **True** pour forcer l'activation du mode debug dans tout les cas.
- ***debug_mod_line*** ~ **ATTENTION**. Séparateur visuel utilisé pour le mod debug et le fichier de sauvegarde des logs. Le modifier pourrait altérer la visibilité des informations.
- ***assemblor_file_name*** ~ Par défaut **assemblor_instruct.txt**. Modifiez le paramètre pour changer de fichier de sortie utilisé pour la compilation et contenant les instructions assembleur.

## Exécution du code compilé

### Installation de l'environnement (**Linux**)

- Décompressez l'archive ***msm.tgz***.
- Déplacez-vous dans le dossier décompressé.
- Compilez le programme en entrant dans un terminal : ```gcc msm.c -o msm```

### Exécuter le code compilé (**Linux**)

- Depuis la racine du projet, entrez la commande : ```./MSM/msm assemblor_instruct.txt ```.

***Note*** *: Le PATH renseigné dans la configuration peut être amené à changer selon la configuration.**

# Description technique des langages

## Langage de programmation (**INPUT**)
Poly-compiler prend en compte tous les opérateurs unaires, binaires et logiques classiques. Les priorités opératoires sont respectées et les parenthèses sont autorisées.
Seul les entiers sont manipulés. En cas de résultat normalement décimal, un entier arrondi sera donné.
Vous trouverez également ci-joint toutes les fonctionnalités embarquées par le compilateur.

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

### Opérateurs logiques
- **==** ~ Egale.
- **!=** ~ Différent.
- **>** ~ Supérieur.
- **<** ~ Inférieur.
- **>=** ~ Supérieur ou égale.
- **<=** ~ Inférieur ou égale.
- **and** ~ *Et* logique.
- **or** ~ *Ou* logique.

### Variables et Fonctions
- Déclaration de variable ~ `'var a;'`
- Assignation de variable ~ `'a = 10;'`
- Déclaration d'une fonction ~ `'foo(param1,param2,...){ [...] return myReturn;}'`
- Utilisation d'une fonction ~ `'varFoo = foo(param1,param2)'`
- Affichage d'une variable : `'print a;'` ou `'print(a);'`
- Possibilité d'utiliser une fonction comme une variable (ex : `'print foo(param1,param2) + 15 ;'`)

### Boucles
- **for** ~ `'for(init;cond;step)'`
- **while** ~ `'while(cond)'`
- **Récursivité autorisée**

### Autres
- Un bloc `'main(){}'` doit toujours être présent. Autrement, cela déclenche une erreur.
- Les fonctions doivent êtres définies avant le bloc “main”
- Une variable définie mais non initialisée vaudra par défaut 0.

### Commentaire
Vous pouvez laisser un commentaire dans le code sur une ligne dédié ou en fin de ligne en précédant votre message par le caractère "#".

## Langage assembleur (**OUTPUT**)
Le langage assembleur est décrit dans le fichier joint nommé : ***msm_instructs.txt***.

# Erreur de compilation prise en compte
Afin de prévenir certaines incohérences dans le code source compilé, des erreurs de compilation peuvent être  levées. En voici la liste :
- ***Empty file*** ~ Le fichier utilisé est vide.
- ***Incoherent char*** ~ Le caractère renseigné n'est pas pris en compte par le compilateur.
- ***Double operator deteted*** ~ Un opérateur a été répété deux fois.
- ***Operator Missing the second parameter*** ~ Un opérateur attend une expression à droite.
- ***Parenthesis missing*** ~ Une parenthèse fermante manque à l'expression.
- ***Constant or identifiant repetition without operator*** ~ Deux variables ou deux constantes ont été détécté sans opérateur séparateur.
- ***Unknow error raised.*** ~ Une erreur non gérée par le compilateur est survenue.


***Note*** *: Dans le cas où vous en trouverez davantage, n'hésitez pas à ouvrir une [issue](https://github.com/Hagbuck/poly-compiler/issues) sur notre GitHub. Merci*
