import os
import sys

if __name__=="main":
  if sys.argv[0]=="r":#r :carpeta actual
    ruta = os.getcwd()#
    print(ruta)