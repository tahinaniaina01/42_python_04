#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_ancient_text.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/03 10:27:05 by trakotos            #+#    #+#            #
#   Updated: 2026/04/03 10:53:38 by trakotos           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys
import typing


def print_content_file() -> None:
    if len(sys.argv) != 2:
        raise Exception(f"Usage: {sys.argv[0]} <file>")
    file_name = sys.argv[1]
    print(f"Accessing file '{file_name}'")
    f: typing.IO | None = None
    try:
        f = open(file_name, "r")
        print("---\n")
        print(f.read())
        print("---")
    except Exception as e:
        raise Exception(f"Error opening file '{file_name}': {e}")
    finally:
        if f is not None:
            print(f"File '{file_name}' closed.")
            f.close()


if __name__ == "__main__":
    try:
        print_content_file()
    except Exception as e:
        print(e)
