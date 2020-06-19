#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# give credits
__author__ = "John Wilkinson, stack overflow, python  docu, and google"

import re
import os
import sys
import shutil
import subprocess
import argparse


def get_special_paths(dirname):
    """Given a dirname, returns a list of all its special files."""
    absolute_paths = []
    for root, dirs, files in os.walk(os.path.abspath(dirname),  topdown=True):
        for name in files:
            special_file = re.findall(r'__(\w+)__', name)
            if special_file:
                absolute_paths.append(os.path.join(root, name))
        break
    return absolute_paths


def copy_to(path_list, dest_dir):
    """copy file to folder, if folder doesnt exist then create it"""
    if not os.path.isdir(dest_dir):
        os.makedirs(dest_dir)
    for path in path_list:
        shutil.copy(path, dest_dir)
    return


def zip_to(path_list, dest_zip):
    """give name for zip file to be created in currentdir"""
    print("Command I am going to do:")
    for path in path_list:
        print("zip -j " + dest_zip + " " + path)
        subprocess.run(['zip', '-j', dest_zip, path])
    return


def main(args):
    """Main driver code for copyspecial."""
    # This snippet will help you get started with the argparse module.
    # from the official documentation
    parser = argparse.ArgumentParser(
                                    prog='copy_special',
                                    description='Process some integers.',
                                    usage='%(prog)s [options]',
                                    epilog="And that's how ya copy special")

    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('from_dir', help='declare target directory')
    # TODO: add one more argument definition to parse the 'from_dir' argument
    ns = parser.parse_args(args)

    # TODO: you must write your own code to get the coand line args.
    # Read the docs and examples for the argparse module about how to o this.
    # Parsing command line arguments is a must-have skill.
    # This is input data validation. If something is wrong (or missing) with
    # any required args, the general rule is to print a usage message and
    # exit(1).
    # Your code here: Invoke (call) your functions
    result_paths = get_special_paths(ns.from_dir)
    if not sys.argv:
        parser.print_usage()
    if ns.todir:
        copy_to(result_paths, ns.todir)
    elif ns.tozip:
        zip_to(result_paths, ns.tozip)
    else:
        for path in result_paths:
            print(path)


if __name__ == "__main__":
    main(sys.argv[1:])
