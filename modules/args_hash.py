#! /usr/bin/python3.5
# -*- coding: utf-8 -*-

import os
import datetime

# Console colors
W = '\033[0m'    # white (normal)
R = '\033[31m'   # red
G = '\033[32m'   # green
O = '\033[33m'   # orange
B = '\033[34m'   # blue
P = '\033[35m'   # purple
C = '\033[36m'   # cyan
GR = '\033[37m'  # gray
T = '\033[93m'   # tan

# ---------------------------------------------------------------------------------------
# Pour d'autre variables d'enviromment utiliser cette syntax pour Unix et Windows
# os.environ[""]

# user = os.environ["USERNAME"]
# date_today = str(datetime.date.today())
# ---------------------------------------------------------------------------------------


def clear():
    os.system("clear")

clear()

date_today = str(datetime.date.today())
current_dir = os.getcwd()
# current_dir2 = ""
user = os.environ["USERNAME"]
rep2 = ""


def loop():
    list_current_dir = current_dir.split("/")
    # print(list_current_dir)

    i = None
    u = 0
    for i in list_current_dir:
        u += 1
        # print(str(u) + " : " + i)
    rep2 = "/" + i
    global rep2


def banner(date=date_today, rep=current_dir, name=user):
    if len(rep) <= 30:
        print(T + "\n[" + B + date + T + "]" + W + " - " + GR +
              rep + " - " + T + "[" + B + name + T + "]\n" + W)
        loop()

    if len(rep) >= 30:
        loop()
        print(T + "\n[" + B + date_today + T + "]" + W + " - " + GR +
              rep2 + " - " + T + "[" + B + user + T + "]\n" + W)


try:
    banner()

    while True:
        command = str(input(G + user + W + ":" + P + rep2 + GR + "# "))

        if command in ("yes", "no"):
            print("ii")

        elif command in " ":
            clear()
            banner()

        elif command in "exit":
            print(R + "Fin du Programme\n" + W)
            exit(1)

        else:
            print(T + "Cette commande n'existe pas\n" + W)
            pass

except KeyboardInterrupt:
    print(R + "\nInterruption du Programme\n" + W)
