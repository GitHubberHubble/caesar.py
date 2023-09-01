### Caesar chiffre
### Free to use
import sys
import random
import secrets
from typing import TypeVar

__always_supported = (
    "caesar",
    "brutus",
)

if sys.version_info >= (3, 6):
    chiffre = TypeVar("chiffre", bound = str | int)
    shift = TypeVar("shift", bound = int)
    __all__ = (
        "caesar",
        "brutus",
        "gaius",
        "marcus",
    )
else:
    chiffre = type(str) | type(int)
    __all__ = __always_supported

if sys.version_info >= (3, 6):
    def caesar_shift(custom: shift = ...) -> shift: ...  ### Generate shift for caesar
    def gaius_shift(custom: shift = ...) -> shift: ...  ### Generate shift for gaius

    def caesar(_string: str | int, shift: int, __secure: bool = False) -> chiffre: ...  ### Basic caesar encryption
    def gaius(_string: str | int, shift: int, __secure: bool = ...) -> chiffre: ...  ### advanced caesar chiffre

    def brutus(_string: str | int, shift: int | str) -> str: ...  ### Brutus decrypt caesar
    def marcus(_string: chiffre, shift: int | str) -> str: ...  ### Marcus decrypt gaius
else:
    ...
