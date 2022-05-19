#!/usr/bin/python3
#pip3 install python-nmap
import nmap
import os
sc = nmap.PortScanner()

print("Bienvenue\n")

def main():
    n = input("1- Network scanner\n2- Vulnerabilites Detection\n3- Exploit\n\nPlease entrer un numero : ")
    if n == '1':
        nmap()

    if n == '2':
         vuln()

    if n == '3':
        os.system('msfconsole')
    else:
         print("please veuillez choisir un nombre entre 1 et 3")

def nmap():
    print("****************welcom to the Network Scanner********************")
    print("*****************************************************************")
    ip = input("\nPlease entrer votre adresse IP: ")
    sc.scan(ip, '1-1024')
    print(sc.scaninfo())
    print(sc[ip]['tcp'].keys())


def vuln():
    print("****************welcom to the vulnirabilites Scanner********************")
    print("*****************************************************************")
    ip = input("\nPlease entrer votre adresse IP: ")
    print(os.system('nmap -sV --script=vulscan.nse' +ip))


if __name__ == "__main__":
    main()
