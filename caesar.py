"""
    - Provides simple or advanced (in progress) chiffre based on the caesar chiffre
    - Fore further information get a coffee and read the caesar_README.md or the github documentation ()

"""


import sys
import secrets
import random
from typing import overload, TypeVar

if sys.version_info >= (3, 5):
    chiffre = TypeVar("chiffre", bound = str | int)
else:
    chiffre = type(str) | type(int)

class _Chiffre:
    @staticmethod
    def _caesar_shift():
        return random.randint(1, 100)
    @staticmethod
    def _gaius_shift():
        __shift = []
        shift: int
        for i in range(26):
            __shift.append(i)
        numb_of_zeros = len(str(len(__shift)))
        return shift * (10 ** numb_of_zeros) + len(__shift)

def caesar_shift(custom = None):
    if custom == None:
        return _Chiffre._caesar_shift()
    else:
        if type(custom) == int and len(custom) <= 2:
            return custom

def caesar(string, shift) -> chiffre:  ### Baic caesar chiffre
    if callable(shift):
        print("")
        raise TypeError(f"{shift} is a function, you would loose you decryption key. For more information look at the README.md")
    else:
        _string = []
        string_caesar = ""

        if type(string) == str:
            for char in string:
                if type(char) == str:
                    char_ascii = ord(char)
                    char_caesar = chr(char_ascii + shift)
                    _string.append(char_caesar)

                elif type(char) == int:
                    char_caesar += shift
                    _string.append(char_caesar)

            for char in _string:
                string_caesar += str(char)

            return string_caesar

        elif type(string) == int:
            for numb in string:
                if type(numb) == int:
                    numb_caesar += shift
                    string.append(numb_caesar)

                elif type(numb) == str:
                    numb_ascii = ord(char)
                    numb_caesar = chr(numb_ascii + shift)
                    string.append(numb_caesar)

            for char in _string:
                string_caesar += str(char)

            return string_caesar

        else:
            raise ValueError(f"Transfer parameter musst be a string or a integer. Your type:{string}")

def brutus(_string: chiffre, shift: int) -> str:
    string = []
    string_clear = ""

    if type(_string) == str:
        for char in _string:
            if type(char) == str:
                char_ascii = ord(char)
                char_string = chr(char_ascii - shift)
                string.append(char_string)

            elif type(char) == int:
                char_string -= shift
                string.append(char_string)

        for char in string:
            string_clear += str(char)

        return string_clear

    elif type(_string) == int:
        for numb in _string:
            if type(numb) == int:
                numb_clear-= shift
                string.append(numb_clear)

            elif type(numb) == str:
                numb_ascii = ord(char)
                numb_caesar = chr(char_ascii + shift)
                string.append(numb_caesar)

        for char in string:
            string_clear += str(char)

        return string_clear

