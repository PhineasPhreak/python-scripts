#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
from time import sleep
from platform import system


def dashes(num):
    """Fonction pour la suppression de plusieurs tirets (2 ou 3)"""
    final_name = new_name[0:].replace('-' * num, '-')
    os.renames(path + new_name, path + final_name)
    # print(is_file, '\t Rename to: ', final_name)
    sleep(0.2)


# Important: nom du fichier Python dans le repertoire courant
name_python = 'Rename-By-Dashes.py'

# Variable 'path' definie le repertoire courant
path = ''

# Determine si le fichier Python est executer sous 'Windows', 'Linux', 'Apple'
# et commande pour effacer l'ecran pour Windows et Linux
if system().lower() == 'windows':
    path = os.getcwd() + '\\'
    os.system('cls')

elif system().lower() == 'linux':
    path = os.getcwd() + '/'
    os.system('clear')

# Creation d'une liste du contenue du repertoire courant
# avec le suppression du nom du fichier Python dans la
# declarer plus tot 'name_python'
listing = os.listdir(path)
listing.remove(name_python)

# Creation variables courante dans le sript python
new_name = ''
file_count = 0
folder_count = len(listing)

# print(listing)
print('\nCurrent directories:')
print(path, '\n')

# Boucle 'for' pour supprimer l'espace vide et deux et trois tirets
# sur chaque fichier du repertoire
for is_file in listing:

    # Determine si les fichier sont des 'Fichier' ou 'Dossier'
    if os.path.isfile(path + is_file):
        file_count += 1
        print(is_file, ' ======> ', 'Done')
        # print(is_file, '\t Is it a File?: ', os.path.isfile(path + is_file))

        try:
            # Analyse tous les characteres de la liste
            new_name = is_file[0:].replace(' ', '-')
            # Renommer tous les fichiers avec des tirets
            os.renames(path + is_file, path + new_name)
            # print(is_file, '\t Rename to: ', new_name)
            sleep(0.2)

            if '-'*3 in new_name[0:]:
                # Execution de la fonction 'dashes' avec le parametre 'num
                dashes(num=3)

            elif '-'*2 in new_name[0:]:
                dashes(num=2)

        except FileExistsError:
            # Message d'erreur au cas ou le fichier renommer existe deja
            print('Sorry, this file "{}" already exist. \n'.format(new_name))

# Affiche le nombre de fichier et de dossier
print('\nNumber of files: \t', file_count, '\nNumber of folders: \t', folder_count - file_count)
exit(input('\n Press ENTER '))
