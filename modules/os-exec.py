#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import platform as plt
import subprocess

your_system = plt.system().upper()
your_release = plt.release()


if your_system == 'WINDOWS':
    if your_release == '10':
        print('Your system is Windows 10.')
        subprocess.run('cmd.exe')
    else:
        print('Your system is Windows 7 or other.')


if your_system == 'LINUX':
    subprocess.run('/bin/bash')
