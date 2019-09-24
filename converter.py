#!/usr/bin/python2.7

import sys
from time import sleep
import os

W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[36m' # blue
P  = '\033[35m' # purple
C  = '\033[34m' # cyan
GR = '\033[37m' # gray
T  = '\033[93m' # tan

def hexdec():
    os.system("clear")
    hexval = raw_input(B+"Enter the hex number you would like to convert to decimal: ")
    conv = int(hexval, 16)
    conv = str(conv)
    print ""
    print B+"The Decimal value of "+hexval+" is -- "+R+conv
    print ""
    sleep(1)
    menu()

def hexbi():
    os.system("clear")
    hexval = raw_input(B+"Enter the hex number you would like to convert to binary: ")
    conv = int(hexval, 16)
    conv = bin(conv).lstrip('0b')
    print ""
    print B+"The binary value of "+hexval+" is -- "+R+conv
    print ""
    sleep(1)
    menu()

def hexoct():
    os.system("clear")
    hexval = raw_input(B+"Enter the hex number you would like to convert to octal: ")
    conv = int(hexval, 16)
    conv = oct(conv)
    print ""
    print B+"The octal value of "+hexval+" is -- "+R+conv
    print ""
    sleep(1)
    menu()

def decbi():
    os.system("clear")
    decval = raw_input(B+"Enter the decimal number you would like to convert to binary: ")
    conv = int(decval)
    conv = bin(conv).lstrip('0b')
    print ""
    print "The binary value of "+decval+"is -- "+R+conv
    print ""
    sleep(1)
    menu()

def dechex():
    os.system("clear")
    decval = raw_input(B+"Enter the decimal number you would like to convert to hex: ")
    conv = int(decval)
    conv = hex(conv)
    print ""
    print B+"The hex value of "+decval+" is -- "+G+conv
    print ""
    sleep(1)
    menu()

def decoct():
    os.system("clear")
    decval = raw_input(B+"Enter the decimal number you would like to convert to octal: ")
    conv = int(decval)
    conv = oct(conv)
    print ""
    print "The octal value of "+decval+" is -- "+R+conv
    print ""
    sleep(1)
    menu()

def bidec():
    os.system("clear")
    bival = raw_input(B+"Enter the binary number you would like to convert to decimal: ")
    conv = int(bival, 2)
    conv = str(conv)
    print ""
    print "The decimal value of "+bival+" is -- "+R+conv
    print ""
    sleep(1)
    menu()

def bihex():
    os.system("clear")
    bival = raw_input(B+"Enter the binary number you would like to convert to hex: ")
    conv = int(bival, 2)
    conv = hex(conv)
    print ""
    print "The hex value of "+bival+" is --"+R+conv
    print ""
    sleep(1)
    menu()

def bioct():
    os.system("clear")
    bival = raw_input(B+"Enter the binary number you would like to convert to octal: ")
    conv = int(bival, 2)
    conv = oct(conv)
    print ""
    print "The octal value of "+bival+" is -- "+R+conv
    print ""
    sleep(1)
    menu()

def octdec():
    os.system("clear")
    octval = raw_input(B+"Enter the octal number you would like to convert to decimal: ")
    conv = int(octval, 8)
    conv = str(conv)
    print ""
    print "The decimal value of "+octval+" is -- "+R+conv
    print ""
    sleep(1)
    menu()

def octhex():
    os.system("clear")
    octval = raw_input(B+"Enter the octal number you would like to convert to hex: ")
    conv = int(octval, 8)
    conv = hex(conv)
    print ""
    print "The hex value of "+octval+" is -- "+R+conv
    print ""
    sleep(1)
    menu()

def octbi():
    os.system("clear")
    octval = raw_input(B+"Enter the octal value you would like to convert to binary: ")
    conv = int(octval, 8)
    conv = bin(conv).lstrip('0b')
    print ""
    print "The binary value of "+octval+" is -- "+R+conv
    print ""
    sleep(1)
    menu()

def menu():
    print ""
    print "-----------------------------------------"
    print ""
    print T+"This is the Python converter.\n"
    print T+"1. Convert Hex to Decimal"
    print T+"2. Convert Hex to Binary"
    print T+"3. Convert Hex to Octal"
    print T+"4. Convert Decimal to Binary"
    print T+"5. Convert Decimal to Hex"
    print T+"6. Convert Decimal to Octal"
    print T+"7. Convert Binary to Decimal"
    print T+"8. Convert Binary to Hex"
    print T+"9. Convert Binary to Octal"
    print T+"10. Convert Octal to Decimal"
    print T+"11. Convert Octal to Hex"
    print T+"12. Convert Octal to Binary"
    print R+"99. Exit"
    print ""
    choice = raw_input(G+"What conversion would you like to do: ")

    if choice == "1":
        hexdec()
    elif choice == "2":
        hexbi()
    elif choice == "3":
        hexoct()
    elif choice == "4":
        decbi()
    elif choice == "5":
        dechex()
    elif choice == "6":
        decoct()
    elif choice == "7":
        bidec()
    elif choice == "8":
        bihex()
    elif choice == "9":
        bioct()
    elif choice == "10":
        octdec()
    elif choice == "11":
        octhex()
    elif choice == "12":
        octbi()
    elif choice == "99":
        print R+"Now exiting Python converter."
        sleep(2)
        os.system("clear")
        sys.exit()
    else:
        print R+"Please select a valid choice from the menu"
        menu()

menu()

