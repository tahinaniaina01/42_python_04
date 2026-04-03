#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_archive_creation.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/03 11:04:39 by trakotos            #+#    #+#            #
#   Updated: 2026/04/03 11:31:58 by trakotos           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys
import typing


def read_content_file() -> str:
    if len(sys.argv) != 2:
        raise Exception(f"Usage: {sys.argv[0]} <file>")
    file_name = sys.argv[1]
    print(f"Accessing file '{file_name}'")
    f: typing.TextIO | None = None
    try:
        f = open(file_name, "r")
        contents = f.read()
        print("---\n")
        print(contents)
        print("---")
        new_contents = contents.replace("\n", "#\n")
    except Exception as e:
        raise Exception(f"Error opening file '{file_name}': {e}")
    finally:
        if f is not None:
            print(f"File '{file_name}' closed.")
            f.close()
    return new_contents


def write_content(contents: str):
    print("\nTransform data:\n---\n")
    print(contents)
    print("---")
    file_name = input("Enter new file name (or empty): ")
    if file_name != "":
        print(f"Saving data to '{file_name}'")
        f: typing.TextIO | None = None
        try:
            f = open(file_name, "w")
            print(contents, file=f)
            print(f"Data saved in file '{file_name}'.")
        except Exception as e:
            print(e)
        finally:
            if f is not None:
                f.close()
    else:
        print("Not saving data.")


if __name__ == "__main__":
    try:
        contents = read_content_file()
        write_content(contents)
    except Exception as e:
        print(e)
