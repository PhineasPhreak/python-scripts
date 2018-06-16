#! /usr/bin/env python3.5
# -*- coding: utf-8 -*-

import os
import sys

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


if os.geteuid():
    sys.exit('[' + R + '-' + W + '] Lancer en tant que Root\n')


print("Service" + B + " SSH" + W + " STATUS\n")
os.system("service ssh status")
