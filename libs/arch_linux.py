# Bibliotecas
from os import system

def arch_linux_menu():
    system('clear')
    print("""
 #     # #     #     #####  ####### ####### ######  ####### 
 ##   ##  #   #     #     #    #    #     # #     # #       
 # # # #   # #      #          #    #     # #     # #       
 #  #  #    #        #####     #    #     # ######  #####   
 #     #    #             #    #    #     # #   #   #       
 #     #    #       #     #    #    #     # #    #  #       
 #     #    #        #####     #    ####### #     # #######

[01] - Internet
[02] - Multimedia
[03] - Development
[04] - Office

    """)
    cmd = str(input('===> '))
    if cmd == '1': 
        system('clear')
        print("""
 #     # #     #     #####  ####### ####### ######  ####### 
 ##   ##  #   #     #     #    #    #     # #     # #       
 # # # #   # #      #          #    #     # #     # #       
 #  #  #    #        #####     #    #     # ######  #####   
 #     #    #             #    #    #     # #   #   #       
 #     #    #       #     #    #    #     # #    #  #       
 #     #    #        #####     #    ####### #     # #######

[01] - Brave
[02] - Tor
[03] - Chromium
[04] - Google Chrome 
[05] - Discord 
[06] - Skype
[07] - Telegram Desktop
[08] - Firefox 

    """)
        cmd = str(input('===> '))
        if cmd == '':
            system('yay -S brave-bin')
        elif cmd == '2':
            system('git clone https://aur.archlinux.org/tor-browser.git ; cd tor-browser ; makepkg -si')
        elif cmd == '3':
            system('sudo snap install chromium')
        elif cmd == '4':
            system('https://aur.archlinux.org/google-chrome.git ; cd google-chrome ; makepkg -s ')
        elif cmd == '5':
            system('sudo snap install discord')
        elif cmd == '6':
            system('sudo snap install skype')
        elif cmd == '7':
            system('sudo snap install telegram-desktop')
        elif cmd == '8':
            system('sudo snap install firefox')
    elif cmd == '2':
        system('clear')
        print("""
 #     # #     #     #####  ####### ####### ######  ####### 
 ##   ##  #   #     #     #    #    #     # #     # #       
 # # # #   # #      #          #    #     # #     # #       
 #  #  #    #        #####     #    #     # ######  #####   
 #     #    #             #    #    #     # #   #   #       
 #     #    #       #     #    #    #     # #    #  #       
 #     #    #        #####     #    ####### #     # #######

[01] - Spotify
[02] - Vlc
[03] - PulseAudio
[04] - Simplescreenrecorder
[05] - OBS Studio
[06] - Gimp
[07] - Vidcutter
[07] - Audacity
    """)
        cmd = str(input('===> '))
        if cmd == '1':
            system('yay -S spotify-bin')
        elif cmd == '2':
            system('sudo snap install vlc')
        elif cmd == '3':
            system('sudo pacman -S pulseaudio')
        elif cmd == '4':
            system('sudo snap install simplescreenrecorder')
        elif cmd == '5':
            system('sudo snap install obs-studio')
        elif cmd == '6':
            system('sudo snap install gimp')
        elif cmd == '7':
            system('sudo snap install vidcutter')
        elif cmd == '8':
            system('sudo snap install audacity')
    elif cmd == '3':
        system('clear')
        print("""
 #     # #     #     #####  ####### ####### ######  ####### 
 ##   ##  #   #     #     #    #    #     # #     # #       
 # # # #   # #      #          #    #     # #     # #       
 #  #  #    #        #####     #    #     # ######  #####   
 #     #    #             #    #    #     # #   #   #       
 #     #    #       #     #    #    #     # #    #  #       
 #     #    #        #####     #    ####### #     # #######

[01] - Vscode
[02] - Geany
[03] - Sublime-text
[04] - Android Studio

    """)
        cmd = str(input('===> '))
        if cmd == '1':
            system('sudo snap install code --classic')
        elif cmd == '2':
            system('sudo snap install geany-gtk --edge')
        elif cmd == '3':
            system('sudo snap install sublime-text --classic')
        elif cmd == '4':
            system('sudo snap install android-studio --classic')
    
    elif cmd == '4':
        system('clear')
        print("""
 #     # #     #     #####  ####### ####### ######  ####### 
 ##   ##  #   #     #     #    #    #     # #     # #       
 # # # #   # #      #          #    #     # #     # #       
 #  #  #    #        #####     #    #     # ######  #####   
 #     #    #             #    #    #     # #   #   #       
 #     #    #       #     #    #    #     # #    #  #       
 #     #    #        #####     #    ####### #     # #######

[01] - Libreoffice
[02] - Onlyoffice
 

    """)
        cmd = str(input('===> '))
        if cmd == '1':
            system('sudo snap install libreoffice')
        elif cmd == '2':
            system('sudo snap install onlyoffice-desktopeditors')