# Bibliotecas
from os import system
from time import sleep
from libs import arch_linux, banners
from libs import ubuntu
from libs import debian
from libs import arch_linux
#Menu
def menu():
    while True:
        system('clear')
        print("""
    #     # #     #     #####  ####### ####### ######  ####### 
    ##   ##  #   #     #     #    #    #     # #     # #       
    # # # #   # #      #          #    #     # #     # #       
    #  #  #    #        #####     #    #     # ######  #####   
    #     #    #             #    #    #     # #   #   #       
    #     #    #       #     #    #    #     # #    #  #       
    #     #    #        #####     #    ####### #     # #######

    - What is your operating system base?

    [01] - Ubuntu
    [02] - Debian
    [03] - Arch Linux
    """)
        cmd = str(input('===> '))
        if cmd == '1':
            ubuntu.ubuntu_menu()
        elif cmd  == '2':
            debian.debian_menu()
        elif cmd  == '3':
            arch_linux.arch_linux_menu()

banners.fun_welcome()   
menu()