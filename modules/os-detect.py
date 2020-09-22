#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import platform
import os


def file_os(file_txt):
    """Creation file for OS Linux and Windows"""
    with open(file_txt, 'a') as file_text:
        file_text.write('Full-Name: ' + name_platform + '\n')
        file_text.write('OS: ' + name_system + '\n')
        file_text.write('Release: ' + name_release + '\n')
        file_text.write('Machine: ' + name_machine + '\n')
        file_text.write('Distribution: ' + name_distribution + '\n')
        file_text.write('Node: ' + name_node + '\n')


def clean_sys():
    """Clear screen for Windows and Linux"""
    if name_system == "windows":
        os.system('cls')

    elif name_system == "linux":
        os.system('clear')


# Create 6 variables for name system and name release on lower case
name_platform = platform.platform()
name_system = platform.system().lower()
name_release = platform.release().lower()
name_machine = platform.machine()
name_distribution = platform.dist()[0]
name_node = platform.node()

if name_system == 'linux':
    clean_sys()
    print(name_platform)

    # Change boolean value 'True' or 'False' if you want text file
    if False:
        print('[*] Create File "OS-Linux.txt"')
        file_os(file_txt='OS-Linux.txt')

elif name_system == 'windows':
    clean_sys()
    print(name_platform)

    if False:
        print('[*] Create File "OS-Windows.txt"')
        file_os(file_txt='OS-Windows.txt')

else:
    print(name_platform)
