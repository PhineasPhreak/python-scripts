# !/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import os
import time
import sys

# sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=32, cols=100))
os.system("clear")
# time.sleep(3)
# os._exit(True)

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

print(P + "DEEPIN and XUBUNTU and GNOME UBUNTU\n" + W)
os.system("hostnamectl\n")

# Are you root?
if os.geteuid():
    sys.exit('[' + R + '-' + W + '] Lancer en tant que Root\n')

try:

    print("\n [" + BR + O + "*" + W + "]" + BR + " Installation d'outils supplémentaires")

    print(" [" + BR + O + "*" + W + "]" + BR + " Mise a Jour des Depots\n")
    os.system("apt-get update")
    print("\n [" + BR + G + "+" + W + "]" + BR + " Depot a Jour\n")

    installed = ['nmap',
                 'zenmap',
                 'ssh',
                 'hping3',
                 'nikto',
                 'transmission',
                 'rsync',
                 'htop',
                 'dstat',
                 'recordmydesktop',
                 'git',
                 'hexedit',
                 'gcp',
                 'bleachbit',
                 'forensics-all',
                 'rkhunter',
                 'fwbuilder',
                 'idle-python2.7'
                 'idle-python3.6',
                 'zathura',
                 'irrsi',
                 'hexchat',
                 'macchanger',
                 'unix2dos',
                 'wavemon',
                 'pv',
                 'aria2',
                 'dmtx-utils',
                 'iec16022',
                 'qrencode',
                 'lshw',
                 'lsscsi',
                 'dmidecode',
                 'bwm-ng',
                 'bmon',
                 'iftop']

    count = 0
    for depot in installed:
        count += 1
        print(" [" + BR + O + "*" + W + "]" + BR + " Installation de {}\n".format(depot))
        os.system("sudo apt-get install -y " + depot)
        print("\n [" + BR + G + "+" + W + "]" + BR + " {} Installer".format(depot))
        print(G + "\n Installation numero: " + R + str(count) + W)

except KeyboardInterrupt:
    print(R + "\n Interruption du programme par l'utilisateur \n" + W)
