#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import hashlib
# import textwrap


def file_size(file_path):
    """
    this function will return the file size
    """
    if os.path.isfile(file_path):
        file_info = os.stat(file_path)
        return convert_bytes(file_info.st_size)


def convert_bytes(num):
    """
    this function will convert bytes to MB.... GB... etc
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0


# Lets check the file size of MS Paint exe
# or you can use any file path
# file_path = r"C:\Users\pspk\Downloads\hwi_590.zip"
# print(file_size(file_path))


def hashing(files_to_hash):
    """
    hash for large files in python
    """
    block_size = 65536
    # sha = hashlib.sha512()
    with open(files_to_hash, 'rb') as a_file:
        buf = a_file.read(block_size)
        while len(buf) > 0:
            sha[0][3].update(buf)
            buf = a_file.read(block_size)
    return sha[0][3].hexdigest()


def sizing(text_size):
    """
    Create text file with name, size and SHA512 by default
    """
    if text_size:
        # information for files > to 2 MB (200000000 bytes)
        if os.stat(files).st_size >= 200000000:
            print("\nPlease wait a few minutes for '{0}' with size '{1}'"
                  .format(files, file_size(files)))

        print(files + " " +
              file_size(files) + " " +
              hashing(files_to_hash=files))
        write_file.write(files + " " +
                         file_size(files) + " " +
                         hashing(files_to_hash=files) + "\n")

    else:
        print(files + " " +
              hashing(files_to_hash=files))
        write_file.write(files + " " +
                         hashing(files_to_hash=files) + "\n")


sha = [[hashlib.sha224(),
        hashlib.sha256(),
        hashlib.sha384(),
        hashlib.sha512()],
       [hashlib.sha3_224(),
        hashlib.sha3_256(),
        hashlib.sha3_384(),
        hashlib.sha3_512()]]

current_path = os.getcwd()
listing = os.listdir(current_path)
file_hash = "hashing.txt"


with open(file=file_hash, mode="w", encoding="utf8") as write_file:
    for files in listing:
        if os.path.isfile(files):
            """
            # print(files)
            # sha512 = hashlib.sha256(files.encode()).digest_size()
            # print(sha512)

            # files_path = files
            # print(files, file_size(files_path), hasher(files_to_hash=files))
            """

            sizing(text_size=True)

