#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_vault_security.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/03 13:41:06 by trakotos            #+#    #+#            #
#   Updated: 2026/04/03 17:05:33 by trakotos           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


def read_file(file_name: str) -> str:
    with open(file_name, "r") as f:
        contents = f.read()
    return contents


def write_in_file(file_name: str, contents: str) -> None:
    with open(file_name, "w") as f:
        f.write(contents)


def secure_archive(
    file_name: str, action: str, contents: str | None = None
) -> tuple[bool, str]:
    try:
        if action == "r":
            c = read_file(file_name)
            print("Using 'secure_archive' to read from a regular file:")
            return (True, c)
        elif action == "w":
            if contents is not None:
                write_in_file(file_name, contents)
                print(
                    "Using 'secure_archive' to write"
                    "previous content to a new file:"
                )
                return (True, 'Content successfully written to file')
            else:
                return (False, "Error: contents empty")
        else:
            return (False, "Action error, use 'r' or 'w'")
    except FileNotFoundError as e:
        print("Using 'secure_archive' to read from a nonexistent file:")
        return (False, f"{e}")
    except PermissionError as e:
        print("Using 'secure_archive' to read from an inaccessible file:")
        return (False, f"{e}")
    except Exception as e:
        return (False, f"Error: {e}")


if __name__ == "__main__":
    file_names = ["/not/existing/file", "/etc/shadow", "ancient_fragment.txt"]
    for f in file_names:
        res = secure_archive(f, "r")
        print(res)
        print()
        if res[0]:
            new_res = secure_archive(f.split(".")[0]+"_clone.txt", "w", res[1])
            print(new_res)
            print()
