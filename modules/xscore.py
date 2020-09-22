#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
# import socket
import getpass
import hashlib
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

# ---------------------------------------------------------


#def clear():
    #""" Efface l'ecran du terminal """
    #os.system("clear")


#clear()

hash_name = "14ff5fc787cdf4915bb8bea782b408888163a2a9b3beb1bbb550420d08827882" \
            "bde95b4244bd5f18aa58c8eee57fb3b14df9abc5dc59fba36cdc3b4da9e120b0"
hash_passwd = "819b1b95d2cf09b0627ce7ebf461b2e6a711a9cf16a6a30d85e8107e309d47e3" \
              "e6b8be33623e6215f663ec8d633bce3f49fbf4c9271ba4c58f3a33489527406d"

try:
    log_on = input("\n Log On: ")
    str(log_on)
    sha_512_name = hashlib.sha512(log_on.encode()).hexdigest()

    passwd = getpass.getpass("\n Password: ")
    str(passwd)
    sha_512_passwd = hashlib.sha512(passwd.encode('utf-8')).hexdigest()

    if sha_512_name == hash_name:
        print("\n\tIdentifiant: OK")
        if sha_512_passwd == hash_passwd:
            print("\tPASSWORD: OK\n")
    else:
        print("Mauvais Identifiant, ou Mot de Passe")

    #clear()
    print("_" * 50)
    print("""\n

        """)


except KeyboardInterrupt:
    print("\nprogramme fermer par l'utilisateur\n")
