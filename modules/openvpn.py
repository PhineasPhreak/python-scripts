# !/usr/bin/env python3.5
# -*- coding: utf-8 -*-

import urllib

# Console colors
BR = '\033[1m'   # Gras
S = '\033[4m'    # Soulignement
W = '\033[0m'    # white (normal)
R = '\033[31m'   # red
G = '\033[32m'   # green
O = '\033[33m'   # orange
B = '\033[34m'   # blue
P = '\033[35m'   # purple
C = '\033[36m'   # cyan
GR = '\033[37m'  # gray
T = '\033[93m'   # tan

# ============================================================================================

try:
    url = "http://monip.org/"
    ip = ''

    print(B + 'Open link URL: \n' + P + url + W)

    ip = urllib.urlopen(url).readlines()
    ip = ip[7]
    ip = ip.replace('<P ALIGN="center"><FONT size=8><BR>IP : ', '')
    ip = ip.replace('<br></font><font size=3><i>LFbn-1-7983-127.w90-112.abo.wanadoo.fr</i><br></font><font size=1><br><br>Pas de proxy détecté - No Proxy detected</font></html>', '')
    ip = ip.strip()

    internet = urllib.urlopen(url).readlines()
    internet = internet[7]
    internet = internet.replace('<P ALIGN="center"><FONT size=8><BR>IP : ' + ip + '<br></font><font size=3><i>', '')
    internet = internet.replace('</i><br></font><font size=1><br><br>Pas de proxy détecté - No Proxy detected</font></html>', '')
    internet = internet.strip()

    print('\n' + C + BR + 'IP External: \t' + G + BR + ip + W)
    print(C + BR + 'Internet: \t' + G + BR + internet + W)

except IOError:
    print(R + 'Probleme avec la connexion' + W)
    exit(1)

except KeyboardInterrupt:
    print(R + 'Quitter le Programme' + W)
    exit(1)
