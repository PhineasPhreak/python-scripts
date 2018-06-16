# !/usr/bin/python3.5
# -*- coding: utf-8 -*-

import os
import os.path
import time
# import sys

# sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=32, cols=100))
# time.sleep(3)

# Console colors
BR = '\033[1m'  # Gras
W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
GR = '\033[37m'  # gray
T = '\033[93m'  # tan


def clear():
    os.system("clear")
clear()

# ------------------------------------------------------------------------

try:
    print(G + BR + "Affichage des Variables D'enviroments" + W)
    print(BR + "\nRepertoire courant:\t" + W, os.getcwd())

    core_nums = os.cpu_count()
    if core_nums < 4:
        print(BR + "Nombre de Core de votre CPU:\t" + W + R, str(core_nums) + W)
    else:
        print(BR + "Nombre de Core de votre CPU:\t" + W + G, str(core_nums) + W)

    list0 = []
    for i in range(0, 2):
        if i == 0:
            name_dict = input(C + "\nEntree votre nom: " + W)
            str(name_dict)
            list0.append(name_dict)
        elif i == 1:
            email_dict = input(C + "\nEntree une adresse couriel valide: " + W)
            str(email_dict)
            list0.append(email_dict)

    print(list0, "\nNombre de d'index ajouter: " + BR, str(len(list0)) + W)
    print(T + "-" * 45 + W)

    with open('data-dict.lst', 'w') as file_text:
        file_text.write(list0[0] + '\n')
        file_text.write(list0[1])


except KeyboardInterrupt:
    print(R + "\nFin du Programme\n" + W)
    time.sleep(1.5)
    clear()
    exit(1)
