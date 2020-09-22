#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import fs
from fs import open_fs
import gnupg

gpg = gnupg.GPG(gnupghome="/home/sammy/.gnupg")
home_fs = open_fs(".")

files_dir = []

files = [f for f in os.listdir(".") if os.path.isfile(f)]
for f in files:
    files_dir.append(f)

for i in files_dir:
    with open("../../signatures/" + i + ".sig", "rb") as f:
        verify = gpg.verify_file(f, i)
        print(i + " ", verify.status)

