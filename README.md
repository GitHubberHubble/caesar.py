# caesar.py
A simple python module that provides functions to "encrypt" and "decrypt" strings and numbers using the basic caesar chiffre or a selfmade advanced chiffre based on the caesar chiffre. More information in the caesar_README.md.

### author: Dr.med.Denrasen
### version: 0.1
###
### functions:
###     - caesar_shift(custom: shift = ...) -> shift: ...
###         useage:
###             - generates shift/key for the caesar() function
###             - use the "custom" parameter to use a custom shift/key
###
###     - gaius_shift(custom = ...) -> shift: ...
###         useage:
###             - generates shift/key for the gaius() function
###             - use the "custom" parameter to use a custom shift/key
###
###     - caesar(_string, shift, __secure = False)
###         useage:
###             - basic caesar chiffre
###             - _string = string to encrypt
###             - shift = explains itself
###             - __secure = indicates if the encryption is secure
###
###     - gaius(_string, shift, __secure = ...)
###         useage:
###
###     - brutus(_string, shift)
###         useage:
###
###     - marcus(_string, shift)
###         useage:
###
### note:
###     - neither gaius(), marcus() nor gaius_shift() are implemented yet
