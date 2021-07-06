#!/usr/bin/python3
# This Programm write by Mr.nope
# Except-Python 1.2.0

import os, sys, time, platform
try:
    from colorama import Fore,init
except ImportError:
    os.system("pip3 install colorama")

opt = Fore.LIGHTGREEN_EX + "\nPyEx" + Fore.YELLOW + " ~# " + Fore.WHITE
system = platform.uname()[0]

banner = """
MMMMMMMMMMMMMMMMMNOo:'.         .':oONMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMNOl,.                 .,lONMMMMMMMMMMMMMM
MMMMMMMMMMMMW0;  .coc.                  ;0WMMMMMMMMMMMM
MMMMMMMMMMMMN:  .kMMWx.                  :NMMMMMMMMMMMM
MMMMMMMMMMMMX;   :O0k:                   ;XMMMMMMMMMMMM
MMMMMMMMMMMMX;     .                     ;XMMMMMMMMMMMM
MMMMWWNNNNNNKxcccccccccccc;..            ;XWNNNNNWWMMMM
MMNkc,'....'''''.''''.''''..             ;Ol..'.',ckNMM  """ + Fore.RED + "Version: " + Fore.YELLOW + "1.2.0" + Fore.WHITE + """
MK:                                      :k'        :KM
K;                                       lx.         ;K
l                                       .do.          l
.                                       :k,           .
                                      .cx;             
                 .',;;;::;;;::::::cccllc.              
              .cllcc::::::::;;;;;;,'..                 
             :xc.                                      
.           ;k;                                       .
l          .dd.                                       l
K;         .xl                                       ;K
MK:        'k:                                      :KM
MMNkc,''..'lO;             ..''''''.'..''.......',ckNMM
MMMMWWNNNNNWX;            ..;ccccccccccccxKNNNNNNWMMMMM
MMMMMMMMMMMMX;                     .     ;XMMMMMMMMMMMM
MMMMMMMMMMMMX;                   ;k0O:   ;XMMMMMMMMMMMM
MMMMMMMMMMMMN:                  .xWMMk.  :NMMMMMMMMMMMM
MMMMMMMMMMMMW0;                  .coc.  ;0MMMMMMMMMMMMM
MMMMMMMMMMMMMMNOl,.                 .,lONMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMNOo:'.         .':oONWMMMMMMMMMMMMMMMM
"""
def cls():
    if system == 'Linux':
        os.system("clear")
    elif system == 'Windows':
        os.system("cls")
    else:
        print("\nSorry, Please Run This Programm on Linux, Windows\n")
        sys.exit()
def main():
    os.system("printf '\033]2;PyEx\a'")
    cls()
    print(banner)
    print("\n{1}.Start Except Python")
    print("{2}.Exit")
    choose = input(opt)
    if choose == '1':
        pyexp()
    elif choose == '2':
        ext()
    elif choose == '' or choose == ' ':
        return main()
    else:
        cls()
        print(choose + Fore.RED + " Not Found!" + Fore.WHITE)
        try1()
def try1():
    try_to_menu = input("\npress Enter...")
    if try_to_menu == '':
        main()
    else:
        main()
def ext():
    cls()
    print(Fore.GREEN + "Exiting..." + Fore.WHITE)
    sys.exit()
def pyexp():
    cls()
    print("Usage: Ctrl + D To Stop Work And back To Main Menu!\n")
    time.sleep(0.80)
    file_name = input("\nEnter File Name: ")
    time.sleep(1)
    excp = input("\nEnter Except Name: ")
    time.sleep(1)
    print("\nCreating...")
    time.sleep(2)
    f = open(file_name + ".py","w")
    f.write("""
class """ + excp + """ (Exception):
      # code
      pass""")
    f.close()
    print(f"\nFile: {file_name} Created!\n")
    time.sleep(0.50)
    try1()
if __name__ == '__main__':
    try:
        try:
            main()
        except EOFError:
            main()
    except KeyboardInterrupt:
        print("\nCtrl + C")
        print("\nExiting...")
        sys.exit()