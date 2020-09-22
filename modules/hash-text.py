#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import hashlib
import platform
# import uuid
# import time
# import timeit
# import random
# import sys

# sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=32, cols=100))
# time.sleep(3)

# Console colors
BR = '\033[1m'   # Gras
W = '\033[0m'    # white (normal)
R = '\033[31m'   # red
G = '\033[32m'   # green
O = '\033[33m'   # orange
B = '\033[34m'   # blue
P = '\033[35m'   # purple
C = '\033[36m'   # cyan
GR = '\033[37m'  # gray
T = '\033[93m'   # tan

# ----------------------------------------------------------------------------------------------

# Alternative de Hash256 pour le mot de passe de votre compte Linux ou Mac
# ------------------------------------------------------------------------
# def hash_password(password):
#     # uuid is used to generate a random number
#     salt = uuid.uuid4().hex
#     return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt
#
#
# def check_password(hashed_password, user_password):
#     password, salt = hashed_password.split(':')
#     return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()
#
# new_pass = input('Please enter a password: ')
# hashed_password = hash_password(new_pass)
# print('The string to store in the db is: ' + hashed_password)
# old_pass = input('Now please enter the password again to check: ')
#
# if check_password(hashed_password, old_pass):
#     print('You entered the right password')
# else:
#     print('I am sorry but the password does not match')
# -----------------------------------------------------------------------------------------------

name_system = platform.system().lower()

def clean_sys():
    """Clear screen for Windows and Linux"""
    if name_system == "windows":
        os.system('cls')

    elif name_system == "linux":
        os.system('clear')


def hash_main():
    # Affichage du menu d'accueil du programme
    clean_sys()
    print(BR + '  _   _           _')
    print(' | | | | __ _ ___| |___ ')
    print(' | |_| |/ _` / __| `_  |')
    print(' |  _  | (_| \__ \ | | |')
    print(' |_| |_|\__,_|___/_| |_|' + W)
    print(B + "\nVos Choix: " + P + "'md5', 'sha1', 'sha224', 'sha256', 'sha384',\n"
                                    "'sha512', 'all', 'help', 'read', 'history', 'del', 'exit'" + W)


def help_in():
    # Definition des termes md5, sha1, etc dans une commande "help" qui appelle la fonction "help_in"
    print("""\nDescription:
    Ce programme permet de faire un Hash de votre texte,
    pour la protection de vos mot de passe par exemple
    ou pour touts autre utilisation, etc

    md5:\tPermet de faire un hash avec l'algorithme md5
    pour plus d'information: https://fr.wikipedia.org/wiki/MD5

    sha-1:\tSHA-1 (Secure Hash Algorithm) est une fonction de hachage
    \tcryptographique conçue par la National Security Agency des États-Unis
    \tpour plus d'information: https://fr.wikipedia.org/wiki/SHA-1

    sha-224; sha-256; sha-384; sha-512

    \tSHA-256 et SHA-512 dont les algorithmes sont similaires mais opèrent
    \tsur des tailles de mot différentes (32 bits pour SHA-256 et 64 bits pour SHA-512),
    \tSHA-224 et SHA-384 qui sont essentiellement des versions des précédentes
    \tdont la sortie est tronquée, et plus récemment SHA-512/256 et SHA-512/224
    \tqui sont des versions tronquées de SHA-512. Le dernier suffixe indique le
    \tnombre de bits du haché.

    all:\tCette commande permet de faire faire un Hash avec
    tous les algorithmes proposer. """)


def func_write_file(a, b, c):
    # Fonction pour la creation du fichier texte "hash-text-editor.txt"
    # Avec demande "Oui" ou "Non" pour la creation du fichier texte
    # IDEM pour la commande "all" a la ligne(229)
    is_valid2 = 0
    while not is_valid2:
        write_file2 = input(B + "\n Ecrire dans un fichier texte " + P + "[o-n] " + B + " : " + W)
        str(write_file2)

        if write_file2 == "o":
            with open(file_txt, 'a') as file_text:
                file_text.write("\n" + a)
                file_text.write(b + ' :: ')
                file_text.write(c)
            print(G + "Ecriture sur le fichier {} effectuer success".format(file_txt) + W)
            is_valid2 = 1

        elif write_file2 == "n":
            print("Pas d'ecriture dans le fichier texte")
            is_valid2 = 1

        elif write_file2.isdigit():
            print(R + "Erreur un chiffre n'est pas valeur correct" + W)

        else:
            print(O + "Ce choix ou cette commande n'existe pas" + W)

# Le bloc d'instruction TRY sert fondamentalement a arrêter
# le programme si l'utilisateur presse "Ctrl+C"
try:
    # Appel de la fonction "hash_main()" declarer plus haut
    hash_main()

    # declaration de la variable d'environement pour le fichier texte
    file_txt = "hash-text-editor.txt"
    # declaration du dictionnaire vide, qui ajoute l'historique des commandes taper
    history = []
    k = 0
    while k < 1:
        # Interaction avec l'utilisateur pour les commandes declarer plus bas dans le "if" et "elif"
        # Convertie cette valeur en "chaîne de caractère", ajout de la commande au dictionnaire
        choice = input(C + "\n Entre Votre Choix : " + W)
        str(choice)
        history.append(choice)

        # Condition du "if" pour le nom de la commande taper
        # Utilisation de la librairie "hashlib" pour l'utilisation des algorithmes de hash md5, sha1, etc
        # IDEM pour les lignes suivantes: (144, 153, 162, 171, 180, 189, 198)
        if choice == "md5":
            hash_md5 = input(T + "\n Entrer Votre Texte : " + W)
            str(hash_md5)
            # print("\n")
            md5 = hashlib.md5(hash_md5.encode('utf-8')).hexdigest()
            print("\n" + G + md5 + W)

            func_write_file(a="md5: ", b=hash_md5, c=md5)

        elif choice == "sha1":
            hash_sha1 = input(T + "\n Entrer Votre Texte : " + W)
            str(hash_sha1)

            sha1 = hashlib.sha1(hash_sha1.encode('utf-8')).hexdigest()
            print("\n" + G + sha1 + W)

            func_write_file(a="sha1: ", b=hash_sha1, c=sha1)

        elif choice == "sha224":
            hash_sha224 = input(T + "\n Entrer Votre Texte : " + W)
            str(hash_sha224)

            sha224 = hashlib.sha224(hash_sha224.encode('utf-8')).hexdigest()
            print("\n" + G + sha224 + W)

            func_write_file(a="sha224: ", b=hash_sha224, c=sha224)

        elif choice == "sha256":
            hash_sha256 = input(T + "\n Entrer Votre Texte : " + W)
            str(hash_sha256)

            sha256 = hashlib.sha256(hash_sha256.encode('utf-8')).hexdigest()
            print("\n" + G + sha256 + W)

            func_write_file(a="sha256: ", b=hash_sha256, c=sha256)

        elif choice == "sha384":
            hash_sha384 = input(T + "\n Entrer Votre Texte : " + W)
            str(hash_sha384)

            sha384 = hashlib.sha384(hash_sha384.encode('utf-8')).hexdigest()
            print("\n" + G + sha384 + W)

            func_write_file(a="sha384: ", b=hash_sha384, c=sha384)

        elif choice == "sha512":
            hash_sha512 = input(T + "\n Entrer Votre Texte : " + W)
            str(hash_sha512)

            sha512 = hashlib.sha512(hash_sha512.encode('utf-8')).hexdigest()
            print("\n" + G + sha512 + W)

            func_write_file(a="sha512: ", b=hash_sha512, c=sha512)

        elif choice == "all":
            hash_all = input(T + "\n Entrer Votre Texte : " + W)
            str(hash_all)

            # Creation de la liste pour la commande "all"
            all_hash = [hashlib.md5(hash_all.encode('utf-8')).hexdigest(),
                        hashlib.sha1(hash_all.encode('utf-8')).hexdigest(),
                        hashlib.sha224(hash_all.encode('utf-8')).hexdigest(),
                        hashlib.sha256(hash_all.encode('utf-8')).hexdigest(),
                        hashlib.sha384(hash_all.encode('utf-8')).hexdigest(),
                        hashlib.sha512(hash_all.encode('utf-8')).hexdigest()]

            kind_hash = ['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512']

            # Le TRY ici sert a éviter tout problème dans la boucle "for"
            # La boucle "for" écrit dans le terminal touts les hash et leur correspondance
            # Suivie de l'écriture dans le fichier texte si l'utilisateur le decide "Oui ou "Non"
            try:
                u = 0
                for list_all_hash in all_hash:
                    u += 1
                    kind_value = kind_hash[u - 1]
                    print(kind_value + " : " + str(list_all_hash))

            except IndexError:
                print(R + BR + "\n Un erreur c'est produite dans la boucle for\n"
                               " le contenu afficher peut contenir des erreurs.\n" + W)

            is_valid = 0
            while not is_valid:
                write_file = input(B + "\n Ecrire dans un fichier texte " + P + "[o-n] " + B + " : " + W)
                str(write_file)

                if write_file.isdigit():
                    print(R + "Erreur un chiffre n'est pas valeur correct" + W)

                elif write_file == "o":
                    t = 0
                    for all_list in all_hash:
                        t += 1
                        kind_value = kind_hash[t - 1]
                        with open(file_txt, 'a') as file_text_all:
                            file_text_all.write("\n" + str(kind_value) + " ")

                            file_text_all.write(hash_all + ' :: ')
                            file_text_all.write(str(all_list))

                    print(G + "Ecriture sur le fichier {} effectuer succes".format(file_txt) + W)
                    is_valid = 1

                elif write_file == "n":
                    print("Pas d'ecriture dans le fichier texte")
                    is_valid = 1
                else:
                    print(O + "Ce choix ou cette commande n'existe pas" + W)

        # La commande "read" sert a lire le fichier texte declarer dans la variable "file_txt",
        # et l'exception "try" sert a indiquer si le fichier texte existe
        elif choice == "read":
            try:
                with open(file_txt, 'r') as read_file:
                    print(read_file.read())

            except FileNotFoundError:
                print(R + "Aucun fichier a lire car le fichier,\n"
                          "'{}' n'existe pas.".format(file_txt))

        # Affiche la fonction "help_in()"
        elif choice == "help":
            help_in()

        # Supprime les espaces vide ou les commande vide dans l'historique de commande
        elif choice == "":
            history.remove("")
            hash_main()

        # Quitte le programme
        elif choice == "exit":
            clean_sys()
            exit(1)

        # Condition dans qui affiche un message d'erreur si l'utilisateur écrit un ou des chiffre(s)
        elif choice.isdigit():
            print(R + "Les valeurs numeriques ne sont pas accepter" + W)

        # Supprime le fichier texte "hash-text-editor.txt", si la creation c'est faite auparavant
        # Et afficher un message d'erreur si le ficher n'existe pas
        elif choice == "del":
            try:
                os.remove(file_txt)
                print(G + "Fichier supprimer avec succes" + W)

            except FileNotFoundError:
                print(R + "Aucun fichier a supprimer.\n"
                          "Le fichier '{}' n'existe pas.".format(file_txt))

        # Affiche l'historique des commande taper
        elif choice == "history":
            i = 0
            print("Liste des commandes tapez :\n")
            for list_history in history:
                i += 1
                print(B + str(i) + W + " " + list_history)

        else:
            print(O + "Ce choix ou cette commande n'existe pas" + W)

# Fin de l'exception "try" si l'utilisateur quitte le programme
except KeyboardInterrupt:
    print(R + BR + "\n\n Interruption du Programme\n" + W)
    # os.remove(file_txt)
    exit(1)
