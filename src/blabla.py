import numpy as np

rng = np.random.default_rng(42)

X = rng.integers(0, 101, size=(10, 3))

print(X)

def blablabla (X):
    return sum (X) / len(X)

blablabla(X)

#import sys --> ça permet d'importer des modules et de manipuler le chemin d'accès aux modules.
#from pathlib import Path --> ça permet de manipuler les chemins de fichiers et dossiers de manière plus simple et plus sûre.
#sys.path.append(str(Path.cwd().resolve().parent)) --> ça permet d'aller chercher le dossier parent pour pouvoir importer des fonctions de ce dossier, dans un cd avant.
#from src import blabla 

#__init__.py --> ça permet de transformer un dossier en package, pour pouvoir importer des fonctions de ce dossier.

#visiblement c'est pour aller chercher des fonctions.