# Converter

Written by Ben Greenberg using Python 3.6.4

Converter is a handy tool to, eh, convert between commonly encountered formats when working with data and files. It can convert from hex to binary, hex to ascii, ascii to hex, as well as perform both Base64 and URL encoding/decoding. Input can be taken from stdin or from a file. Output is sent to stdout or a file with the extension .out appended to the input file name respectively. Output can also be sent to the clipboard.

Usage: converter.py [-h]
                    (-h2b | -h2a | -x2a | -a2h | -a2x | -b64d | -b64e | -urld | -urle)
                    (-s <input> | -f <filename>) [-c]
                    
Usage examples:
#converter.py -a2h -s "ABCDabcd" -> 41 42 43 44 61 62 63 64
#converter.py -x2a -c -s "\x41\x42\x43\x44\x61\x62\x63\x64" -> ABCDabcd (to stdout and clipboard)
#converter.py -b64d -s "R2l2ZSBtZSBiYXNlNjQgb3IgZ2l2ZSBtZSBkZWF0aA==" -> Give me base64 or give me death
#converter.py -urle -f a.txt -> Will produce output file called a.txt.out with URL encoded contents of a.txt
