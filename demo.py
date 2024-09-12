#!/usr/bin/python3
import sys
import subprocess
import time
from colorama import Fore, init
import useragent
import os
import sys
import time
import platform
import requests
import re
import json
import urllib
import colorama
import instaloader
from time import sleep
from datetime import datetime
from instaloader import instaloader
from colorama import init, Fore
import webbrowser


import platform
import getpass
import os

def get_username():
    system = platform.system()
    if system == 'Windows':
        return os.getlogin()
    elif system in ['Linux', 'Darwin']:  # Darwin adalah nama sistem untuk macOS
        return getpass.getuser()
    else:
        raise OSError("Unsupported operating system")

username = get_username()



def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()

try: # Import Module
    import requests
    import time
    import random
    import os
    import urllib3
    import json
    import bs4

except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'requests'])
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'urllib3'])
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'bs4'])
finally:
    import requests # Post, Get, & Put URL API
    import urllib3  # HTTP client untuk Python
    from bs4 import BeautifulSoup as bs




clear()

 #warna inisial hit
hijau   =   "\033[1;92m"
putih   =   "\033[1;97m"
abu     =   "\033[1;90m"
kuning  =   "\033[1;93m"
ungu    =   "\033[1;95m"
merah   =   "\033[1;91m"
biru    =   "\033[1;96m"
ungu2   =   "\33[3;47;43m" #Purple
putih2  =   "\033[0;47;90m"
merah2  =   "\033[0;30;91m" 





def help():
    menu()
    print(f"""
[LAYER 7]
-HTTP             - BASIC HTTP DDOS LAYER 7
-BROWSER          - VIP DDOS METHOD LAYER 7
-KILLER           - FOR WEBSITE THAT HAVE MEDIUM PROTECTION
-STRIKE           - STRIKE WEBSITE DDOS HIGH PROTECTION
-NUKE             - 2 METHOD HTTP AND BROWSER IN ONE
-TSAR             - 3 METHOD HTTP BROWSER KILLER IN ONE
-MIX              - POWERFULL DDOS ATTACK LAYER 7
-BYPASS           - FOR BYPASS WEBSITE
-EVIL             - low stresser ddos
-PHONIEX-A        - ALL METHOD IN ONE
-KRAKATOA         - USE STRONG VPS BECHAUSE THIS IS THE MOST DESTRUCTIVE METHODS
          
[LAYER 4]
-UDP FLOOD        - BASIC UDP FLOOD DDOS LAYER 4
-TCP FLOOD        - BASIC TCP FLOOD DDOS LAYER 4
-ICMP FLOOD       - BASIC ICMP FLOOD DDOS LAYER 4
-Fornax A         - ALL METHOD LAYER4 IN ONE
          
[to attack website]
[METHOD] [TARGET] [PORT] [TIME]{putih}""")
    main()


def menu():
		sys.stdout.write(f"\x1b]2;TON BOTNET :: PREMIUM USER :: TON BOTNET 1.1.1 :: 0/1\x07")
		print(f"""{ungu}



		
                           ,MMM8&&&.
                      _...MMMMM88&&&&..._
                   .::'''MMMMM88&&&&&&'''::.
                  ::     MMMMM88&&&&&&     ::
                  '::....MMMMM88&&&&&&....::'
                     `''''MMMMM88&&&&''''`
                           'MMM8&&&' 
            T O N - X  A S I A N  S T R E S S E R 
		    POWERFULL DDOS BOTNET 
                         BY TON618
___________________________________________________________
		type "help" to see all methods{putih}""")

def main():

	while True:
		sys.stdout.write(f"\x1b]2;TON BOTNET :: PREMIUM USER :: TON BOTNET 1.1.1 :: 1/1\x07")
		sin = input(f"root{merah}@Ton:~#{putih} ")
		sinput = sin.split(" ")[0]
		if sinput == "user" or sinput == ".user":
			print(f"""
{ungu}[user details]
{ungu}USER = [{username}{hijau}]
{ungu}VIP  = {hijau}True
{ungu}VVIP = [{hijau}True]
{ungu}expierd = [{hijau}unlimited]
{putih}""")
		if sinput == "clear":
			clear()
			menu()
		if sinput == "cls" or sinput == "CLS":
			os.system ("pkill screen")
			clear()
			menu()
		if sinput == "stop" or sinput == "STOP":
			os.system ("pkill screen")
			menu()			
		if sinput == "help" or sinput == "HELP" or sinput == ".help" or sinput == ".HELP" or sinput == "menu" or sinput == ".menu" or sinput == "MENU" or sinput == ".MENU":
			clear()
			help()
		elif sinput == "":
			main()
		
		elif sinput == "http" or sinput == ".http" or sinput == ".HTTP" or sinput == "HTTP":
			try:
				host = sin.split()[1]
				port = sin.split()[2]
				time = sin.split()[3]
				print(f"""
[DDOS INFORMATION]
{biru}status : [{hijau} attack launched]
{biru}target : [{hijau}{host}]
{biru}port   : [{hijau}{port}]
{biru}time   : [{hijau}{time}]
{biru}method : [{hijau} HTTP]
{biru}vip    : [{hijau} True]
{biru}vvip   : [{hijau} True]
{biru}user   : [{hijau} {username}]
{putih}""")

			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "browser" or sinput == ".browser" or sinput == "BROWSER" or sinput == ".BROWSER":
			try:
				host = sin.split()[1]
				port = sin.split()[2]
				time = sin.split()[3]

				clear()
				print(f"""
[DDOS INFORMATION]
{biru}status : [{hijau} attack launched]
{biru}target : [{hijau}{host}]
{biru}port   : [{hijau}{port}]
{biru}time   : [{hijau}{time}]
{biru}method : [{hijau} browser]
{biru}vip    : [{hijau} True]
{biru}vvip   : [{hijau} True]
{biru}user   : [{hijau} {username}]
{putih}""")

			except ValueError:
				main()
			except IndexError:
				main()

		elif sinput == "KILLER" or sinput == ".KILLER" or sinput == "killer" or sinput == ".killer":
			try:
				host = sin.split()[1]
				port = sin.split()[2]
				time = sin.split()[3]
				clear()
				print(f"""
[DDOS INFORMATION]
{biru}status : [{hijau} attack launched]
{biru}target : [{hijau}{host}]
{biru}port   : [{hijau}{port}]
{biru}time   : [{hijau}{time}]
{biru}method : [{hijau} killer]
{biru}vip    : [{hijau} True]
{biru}vvip   : [{hijau} True]
{biru}user   : [{hijau} {username}]
{putih}""")

			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "strike" or sinput == ".strike" or sinput == "STRIKE" or sinput == ".STRIKE":
			try:
				host = sin.split()[1]
				port = sin.split()[2]
				time = sin.split()[3]
				clear()
				print(f"""
[DDOS INFORMATION]
{biru}status : [{hijau} attack launched]
{biru}target : [{hijau}{host}]
{biru}port   : [{hijau}{port}]
{biru}time   : [{hijau}{time}]
{biru}method : [{hijau} strike]
{biru}vip    : [{hijau} True]
{biru}vvip   : [{hijau} True]
{biru}user   : [{hijau} {username}]
{putih}""")

			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "nuke" or sinput == ".nuke" or sinput == "NUKE" or sinput == ".NUKE":
			try:
				host = sin.split()[1]
				port = sin.split()[2]
				time = sin.split()[3]

				clear()
				print(f"""
[DDOS INFORMATION]
{biru}status : [{hijau} attack launched]
{biru}target : [{hijau}{host}]
{biru}port   : [{hijau}{port}]
{biru}time   : [{hijau}{time}]
{biru}method : [{hijau} nuke]
{biru}vip    : [{hijau} True]
{biru}vvip   : [{hijau} True]
{biru}user   : [{hijau} {username}]
{putih}""")

			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "tsar" or sinput == ".tsar" or sinput == "TSAR" or sinput == ".TSAR":
			try:
				host = sin.split()[1]
				port = sin.split()[2]
				time = sin.split()[3]

				clear()
				print(f"""
[DDOS INFORMATION]
{biru}status : [{hijau} attack launched]
{biru}target : [{hijau}{host}]
{biru}port   : [{hijau}{port}]
{biru}time   : [{hijau}{time}]
{biru}method : [{hijau} tsar]
{biru}vip    : [{hijau} True]
{biru}vvip   : [{hijau} True]
{biru}user   : [{hijau} {username}]
{putih}""")

			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "mix" or sinput == ".mix" or sinput == "MIX" or sinput == ".MIX":
			try:
				host = sin.split()[1]
				port = sin.split()[2]
				time = sin.split()[3]

				clear()
				print(f"""
[DDOS INFORMATION]
{biru}status : [{hijau} attack launched]
{biru}target : [{hijau}{host}]
{biru}port   : [{hijau}{port}]
{biru}time   : [{hijau}{time}]
{biru}method : [{hijau} mix]
{biru}vip    : [{hijau} True]
{biru}vvip   : [{hijau} True]
{biru}user   : [{hijau} {username}]
{putih}""")

			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "evil" or sinput == ".evil" or sinput == "EVIL" or sinput == ".EVIL":
			try:
				host = sin.split()[1]
				port = sin.split()[2]
				time = sin.split()[3]

				clear()
				print(f"""
[DDOS INFORMATION]
{biru}status : [{hijau} attack launched]
{biru}target : [{hijau}{host}]
{biru}port   : [{hijau}{port}]
{biru}time   : [{hijau}{time}]
{biru}method : [{hijau} evil]
{biru}vip    : [{hijau} True]
{biru}vvip   : [{hijau} True]
{biru}user   : [{hijau} {username}]
{putih}""")

			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "phoniex-a" or sinput == ".phoniex-a" or sinput == "PHONIEX-A" or sinput == ".PHONIEX-A":
			try:
				host = sin.split()[1]
				port = sin.split()[2]
				time = sin.split()[3]

				clear()
				print(f"""
[DDOS INFORMATION]
{biru}status : [{hijau} attack launched]
{biru}target : [{hijau}{host}]
{biru}port   : [{hijau}{port}]
{biru}time   : [{hijau}{time}]
{biru}method : [{hijau} phoniex-a]
{biru}vip    : [{hijau} True]
{biru}vvip   : [{hijau} True]
{biru}user   : [{hijau} {username}]
{putih}""")

			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "krakatoa" or sinput == ".krakatoa" or sinput == "KRAKATOA" or sinput == ".KRAKATOA":
			try:
				host = sin.split()[1]
				port = sin.split()[2]
				time = sin.split()[3]

				clear()
				print(f"""
[DDOS INFORMATION]
{biru}status : [{hijau} attack launched]
{biru}target : [{hijau}{host}]
{biru}port   : [{hijau}{port}]
{biru}time   : [{hijau}{time}]
{biru}method : [{hijau} krakatoa]
{biru}vip    : [{hijau} True]
{biru}vvip   : [{hijau} True]
{biru}user   : [{hijau} {username}]
{putih}""")

			except ValueError:
				main()
			except IndexError:
				main()


		elif sinput == "bypass" or sinput == ".bypass" or sinput == "BYPASS" or sinput == ".BYPASS":
			try:
				host = sin.split()[1]
				port = sin.split()[2]
				time = sin.split()[3]

				clear()
				print(f"""
[DDOS INFORMATION]
{biru}status : [{hijau} attack launched]
{biru}target : [{hijau}{host}]
{biru}port   : [{hijau}{port}]
{biru}time   : [{hijau}{time}]
{biru}method : [{hijau} bypass]
{biru}vip    : [{hijau} True]
{biru}vvip   : [{hijau} True]
{biru}user   : [{hijau} {username}]
{putih}""")
			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "TCP-FLOOD" or sinput == ".TCPFLOOD" or sinput == "tcp-flood" or sinput == ".tcpflood":
			try:
				host = sin.split()[1]
				port = sin.split()[2]
				time = sin.split()[3]

				clear()
				print(f"""
[DDOS INFORMATION]
{biru}status : [{hijau} attack launched]
{biru}target : [{hijau}{host}]
{biru}port   : [{hijau}{port}]
{biru}time   : [{hijau}{time}]
{biru}method : [{hijau} tcpflood]
{biru}vip    : [{hijau} True]
{biru}vvip   : [{hijau} True]
{biru}user   : [{hijau} {username}]
{putih}""")
			except ValueError:
				main()
			except IndexError:
				main()
clear()
menu()
main()
