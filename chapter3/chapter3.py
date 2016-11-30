#!/usr/bin/python

import sys
import os
import hashlib

if len(sys.argv) < 3:
    print "You need to specify two directories:"
    print sys.argv[0], "<directory 1> <directory 2>"
    sys.exit()

directory1 = sys.argv[1]
directory2 = sys.argv[2]

for directory in [directory1, directory2]:
    if not os.access(directory, os.F_OK):
        print "Directory isn't a valid directory!"
        sys.exit()

def md5(file_path):
    """"Return an MD5 checksum for a file"""
    read_file = file(file_path)
    the_hash = hashlib.md5()
    for line in read_file.readlines():
        the_hash.update(line)
    return the_hash.hexdigest()

def directory_listing(dir_name):
    """Return all the files in a directory"""
    dir_file_list = {}
    dir_root = None
    dir_trim = 0
    for path, dirs, files in os.walk(dir_name):
        if dir_root is None:
            dir_root = path
            dir_trim = len(dir_root)
        trimmed_path = path[dir_trim:]
        if trimmed_path.startswith(os.path.sep):
            trimmed_path = trimmed_path[1:]
        for each_file in files:
            file_path = os.path.join(trimmed_path, each_file)
            dir_file_list[file_path] = True
    return (dir_file_list, dir_root)

dir1_file_list, dir1_root = directory_listing(directory1)
dir2_file_list, dir2_root = directory_listing(directory2)

for file_path in dir2_file_list:
    if file_path not in dir1_file_list:
        print file_path, "not found in directory 1"
    else:
        #print file_path, "found file in directory 1 and 2"
        file1 = os.path.join(dir1_root, file_path)
        file2 = os.path.join(dir2_root, file_path)
        if md5(file1) != md5(file2):
            print file1, "and", file2, "differ"
        del dir1_file_list[file_path]

for key, value in dir1_file_list.items():
    print key, "not found in directory 2"