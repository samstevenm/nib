#!/bin/sh -eu
ip_addr="$(nmap -n -sn 192.168.2.1/24 -oG - | awk '/Up$/{print $2}' | tail -n+2)"
pre='https://'
url="$pre$ip_addr"
script='Exec=/home/joel/vivesmall.sh'
echo '[Desktop Entry]' > ~/Desktop/ViveSmall.desktop
echo 'Encoding=UTF-8' >> ~/Desktop/ViveSmall.desktop
echo 'Name=ViveSmall' >> ~/Desktop/ViveSmall.desktop
echo 'Type=Application' >> ~/Desktop/ViveSmall.desktop
echo 'Terminal=False' >> ~/Desktop/ViveSmall.desktop
echo $script >> ~/Desktop/ViveSmall.desktop
echo 'Icon=text-html' >> ~/Desktop/ViveSmall.desktop
chromium-browser --password-store=basic --chrome-frame --window-size=425,692 --window-position=0,80 --app=$url
#chromium-browser --password-store=basic --kiosk --chrome-frame --app="($url)"
