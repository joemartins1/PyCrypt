import platform
import os


def clear():
    user_os = platform.system()
    if user_os == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def string_to_char(string):
    char_list = []
    for char in string:
        char_list.append(char)
    return char_list


def char_to_string(char_list):
    string = "".join(char_list)
    return string


def char_is_lower(char):
    if ord(char) >= 97 and ord(char) <= 122:
        return True
    else:
        return False


def char_is_upper(char):
    if ord(char) >= 65 and ord(char) <= 90:
        return True
    else:
        return False


def char_is_letter(char):
    if char_is_lower(char) or char_is_upper(char):
        return True
    else:
        return False


def read_txt(filename):
    file =  open(filename, "r")
    return file.read()


def write_txt(filename, message):
    with open(filename, "x") as file:
        file.write(message)

