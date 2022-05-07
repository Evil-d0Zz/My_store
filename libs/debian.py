# Bibliotecas
from os import system

def debian_menu():
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

    [01] - Internet
    [02] - Multimedia
    [03] - Development
    [04] - Office
    [05] - Hacking Tools

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
            if cmd == '1':
                system('sudo snap install brave ')
            elif cmd == '2':
                system('sudo apt update && sudo apt upgrade ; sudo apt install apt-transport-https ; wget -q -O - https://deb.torproject.org/torproject.org/A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89.asc | sudo apt-key add - ; echo "deb [arch=amd64] https://deb.torproject.org/torproject.org $(lsb_release -cs) main" | sudo tee -a /etc/apt/sources.list ; echo "deb [arch=amd64] https://deb.torproject.org/torproject.org tor-experimental-0.4.6.x-focal main" | sudo tee -a /etc/apt/sources.list ; echo "deb [arch=amd64] https://deb.torproject.org/torproject.org tor-nightly-master-$(lsb_release -cs) main" | sudo tee -a /etc/apt/sources.list ; sudo apt update ; sudo apt install tor deb.torproject.org-keyring torbrowser-launcher')
            elif cmd == '3':
                system('sudo snap install chromium')
            elif cmd == '4':
                system('wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb ; sudo dpkg -i google-chrome-stable_current_amd64.deb ; sudo apt -f install')
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
                system('sudo apt update ;curl -sS https://download.spotify.com/debian/pubkey_5E3C45D7B312C643.gpg | sudo apt-key add - echo "deb http://repository.spotify.com stable non-free" | sudo tee /etc/apt/sources.list.d/spotify.list ; sudo apt-get update && sudo apt-get install spotify-client')
            elif cmd == '2':
                system('sudo snap install vlc')
            elif cmd == '3':
                system('sudo add-apt-repository ppa:ubuntu-audio-dev/Pulse-testing ; sudo apt-get update ; sudo apt-get install pulseaudio')
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
        elif cmd == '5':
            system('clear')
            print("""
#     # #     #     #####  ####### ####### ######  ####### 
##   ##  #   #     #     #    #    #     # #     # #       
# # # #   # #      #          #    #     # #     # #       
#  #  #    #        #####     #    #     # ######  #####   
#     #    #             #    #    #     # #   #   #       
#     #    #       #     #    #    #     # #    #  #       
#     #    #        #####     #    ####### #     # #######

[01] - Information Gathering
[02] - Vulnerability Assessment
[03] - Exploitation
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

[01] - Arp-Scan
[02] - Masscan
[03] - Nmap
[04] - Dirb 
""")
                cmd = str(input('===> '))
                if cmd == '1':
                    system('git clone https://github.com/royhills/arp-scan.git ; cd arp-scan ; autoreconf --install ; ./configure ; make ; make check ; make install')
                elif cmd == '2':
                    system('sudo apt-get --assume-yes install git make gcc ; git clone https://github.com/robertdavidgraham/masscan ; cd masscan ; make ; make install')
                elif cmd == '3':
                    system('git clone https://github.com/nmap/nmap.git ; cd nmap ; ./configure ; make ; make install')
                elif cmd == '4':
                    system('git clone https://github.com/Seabreg/dirb.git ; cd dirb ; ./configure ; make ; make install')
