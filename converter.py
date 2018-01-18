#Written by Ben Greenberg using Python 3.6.4
#Converter is a handy tool to, eh, convert between commonly encountered formats when working with data and files. It can convert from hex to binary, hex to ascii, ascii to hex, as well as perform both Base64 and URL encoding/decoding. Input can be taken from stdin or from a file. Output is sent to stdout or a file with the extension .out appended to the input file name respectively. Output can also be sent to the clipboard.
#Requires: pyperclip

#Usage: 
#converter.py [-h]
#(-h2b | -h2a | -x2a | -a2h | -a2x | -b64d | -b64e | -urld | -urle)
#(-s <input> | -f <filename>) [-c]

#Usage examples:
#converter.py -a2h -s "ABCDabcd" -> 41 42 43 44 61 62 63 64
#converter.py -x2a -c -s "\x41\x42\x43\x44\x61\x62\x63\x64" -> ABCDabcd (to stdout and clipboard)
#converter.py -b64d -s "R2l2ZSBtZSBiYXNlNjQgb3IgZ2l2ZSBtZSBkZWF0aA==" -> Give me base64 or give me death
#converter.py -urle -f a.txt -> Will produce output file called a.txt.out with URL encoded contents of a.txt

import argparse, base64, binascii, urllib.parse, pyperclip

def Main():
  parser = argparse.ArgumentParser()
  modegroup = parser.add_mutually_exclusive_group(required=True)
  inputgroup = parser.add_mutually_exclusive_group(required=True)
  modegroup.add_argument("-h2b", action="store_true", help="Converts space-separated hex bytes to Binary")
  modegroup.add_argument("-h2a", action="store_true", help="Converts space-separated hex bytes to ASCII")
  modegroup.add_argument("-x2a", action="store_true", help="Converts hex bytes with \\x delimiter to ASCII")
  modegroup.add_argument("-a2h", action="store_true", help="Converts ASCII to space-separated hex bytes")
  modegroup.add_argument("-a2x", action="store_true", help="Converts ASCII to \\x delimited hex bytes")
  modegroup.add_argument("-b64d", action="store_true", help="Base64 decodes input text")
  modegroup.add_argument("-b64e", action="store_true", help="Base64 encodes input text")
  modegroup.add_argument("-urld", action="store_true", help="URL decodes input text")
  modegroup.add_argument("-urle", action="store_true", help="URL encodes input text")
  inputgroup.add_argument("-s", metavar="<input>", help="Takes input from stdin and outputs to stdout")
  inputgroup.add_argument("-f", metavar="<filename>", help="Takes input and outputs to file")
  parser.add_argument("-c", action="store_true", help="Also copies output to the clipboard")
  args = parser.parse_args()
  
  if (args.f is not None):
    with open(args.f, "r") as file:
      input = file.read()
      file.close()
  else:
    input = args.s
    
  if args.h2b is True:
    output = Hex2Binary(input)
  elif args.h2a is True:
    output = Hex2ASCII("h2a", input)
  elif args.x2a is True:
    output = Hex2ASCII("x2a", input)
  elif args.a2h is True:
    output = ASCII2Hex("a2h", input)
  elif args.a2x is True:
    output = ASCII2Hex("a2x", input)
  elif args.b64d is True:
    output = Base64Handler("b64d", input)
  elif args.b64e is True:
    output = Base64Handler("b64e", input)
  elif args.urld is True:
    output = URLHandler("urld", input)
  elif args.urle is True:
    output = URLHandler("urle", input)
    
  if args.f is not None:
    if args.h2b is True:
      OutputFile = open(args.f+".bin","wb")
    else:
      OutputFile = open(args.f+".out","w")
    OutputFile.write(output)
    OutputFile.close()
  else:
    print(output)
    
  if args.c is True:
    pyperclip.copy(output)
    
def Hex2Binary(input):
  return binascii.unhexlify(input.replace(" ", ""))
  
def Hex2ASCII(modetype, input):
  if modetype == "h2a":
    output = input.replace(" ", "").encode("ascii")
  elif modetype == "x2a":  
    output = input.replace("\\x", "").encode("ascii")
    
  return binascii.unhexlify(output).decode("ascii")
  
def ASCII2Hex(modetype, input):
  output = binascii.hexlify(input.encode("ascii")).decode("ascii").upper()
  
  if modetype == "a2h":
    return " ".join([output[x:x+2] for x in range(0,len(output),2)])
  elif modetype == "a2x":
    return "\\x"+"\\x".join([output[x:x+2] for x in range(0,len(output),2)])
  
def Base64Handler(modetype, input):
  if modetype == "b64d":
    return base64.b64decode(input).decode("ascii")
  elif modetype == "b64e":
    return base64.b64encode(input.encode("ascii")).decode("ascii")
    
def URLHandler(modetype, input):
  if modetype == "urld":
    return urllib.parse.unquote(input)
  if modetype == "urle":
    return urllib.parse.quote(input)
    
if __name__ == "__main__":
  Main()