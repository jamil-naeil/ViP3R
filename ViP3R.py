import os
import getpass
import argparse
from time import sleep

def menu():
    sleep(2)
    while True:
        os.system('clear && date')
        print("0--------------------0")
        print(" ▒█░░▒█ ░▀░ ▒█▀▀█ █▀▀█ ▒█▀▀█  ")
        print(" ░▒█▒█░ ▀█▀ ▒█▄▄█ ░░▀▄ ▒█▄▄▀  ")
        print(" ░░▀▄▀░ ▀▀▀ ▒█░░░ █▄▄█ ▒█░▒█  ")
        print("0--------------------0")
        print(" [C] Creator t.me/ERR0Rxx ")
        inject = input(
            '\n  >>  [  Menu ]  <<  \n\n [1] Less Recoil \n [2] AimB0t \n [3] Small Crosshair \n [4] Magic Bullet \n [5] Exit Menu \n\n Enter Input: ')
        if inject == '1':
            os.system("su -c ./module/index.pyc 1")
            sleep(1)
            print('\n Less Recoil Value Injected in Memory Addr = 0x1 \n')
        elif inject == '2':
            os.system("su -c ./module/index.pyc 2")
            sleep(1)
            print('\n Aimb0t Injected in Memory Addr = 0xf \n')
        elif inject == '3':
            os.system("su -c ./module/index.pyc 3")
            sleep(1)
            print('\n Magic Bullet Injected in Memory Addr = 0x3 \n')
        elif inject == '4':
            os.system("su -c ./module/index.pyc 4")
            sleep(1)
            print('\n Small Croshair Injected in Memory Addr = 0x1 \n')
        elif inject == '5':
            sleep(1)
            print('\n #root@1337XCode : Thank You For Using This Program\n\n')
            sleep(1)
            print(" Subscribe To t.me/T34M3RR0Rz & @TeamAvenger For More Updates \n\n")
            sleep(1)
            os.system(
                'am start -n org.telegram.messenger/org.telegram.ui.LaunchActivity https://t.me/T34M3RR0Rz 2> /dev/null')
            os.system(
                'sleep 10 && am start -n org.telegram.messenger/org.telegram.ui.LaunchActivity https://t.me/TeamAvenger 2> /dev/null')
            raise SystemExit
        else:
            print('\n [!] You Have Selected An Invalid Input\n     Please Enter A Valid Input To Continue.')
            sleep(2)
            os.system("clear")
        menu()


def intro():
    os.system('clear && date')
    print("0--------------------0")
    print(" ▒█░░▒█ ░▀░ ▒█▀▀█ █▀▀█ ▒█▀▀█  ")
    print(" ░▒█▒█░ ▀█▀ ▒█▄▄█ ░░▀▄ ▒█▄▄▀  ")
    print(' ░░▀▄▀░ ▀▀▀ ▒█░░░ █▄▄█ ▒█░▒█  ')
    print("0--------------------0")
    sleep(1)
    print("\n Welcome Back To ViP3R ")
    sleep(1)
    print("\n Creator : t.me/ERR0Rxx / XCode \n")
    sleep(1)
    print(" Subscribe To t.me/T34M3RR0Rz & @TeamAvenger For More Updates Regarding ViP3R ")
    sleep(1)
    os.system("clear")
    os.system('su -c chmod 777 *')  # RWX To All Current Directory Files
    os.system('su -c chmod 777 /module/*')  # RWX To All Module Directory Files
    menu()


def security():
    print('\x1b[1;32;40m')
    os.system('clear && date')
    print("\n\n0--------------------0")
    print(" ▒█░░▒█ ░▀░ ▒█▀▀█ █▀▀█ ▒█▀▀█  ")
    print(" ░▒█▒█░ ▀█▀ ▒█▄▄█ ░░▀▄ ▒█▄▄▀  ")
    print(' ░░▀▄▀░ ▀▀▀ ▒█░░░ █▄▄█ ▒█░▒█  ')
    print("0--------------------0\n\n")
    x = getpass.getpass(prompt='Emter Password : ')
    if x.lower() == 'thor':
        print("\n [#] Access Granted \n")
        intro()
    else:
        print(" [!] Password Incorrect. Recheck Your Password. ")
        sleep(2)
        os.system('clear')
        security()

parser = argparse.ArgumentParser(description='\n Command : sudo python3 ViP3R.py ')
args = parser.parse_args()
security()
