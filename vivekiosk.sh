#!/bin/sh -eu
ip_addr="$(nmap -n -sn 192.168.2.1/24 -oG - | awk '/Up$/{print $2}' | tail -n+2)"
pre='https://'
url="$pre$ip_addr"
script='Exec=/home/joel/vivekiosk.sh'
echo '[Desktop Entry]' > ~/Desktop/ViveKiosk.desktop
echo 'Encoding=UTF-8' >> ~/Desktop/ViveKiosk.desktop
echo 'Name=ViveKiosk' >> ~/Desktop/ViveKiosk.desktop
echo 'Type=Application' >> ~/Desktop/ViveKiosk.desktop
echo 'Terminal=False' >> ~/Desktop/ViveKiosk.desktop
echo $script >> ~/Desktop/ViveKiosk.desktop
echo 'Icon=text-html' >> ~/Desktop/ViveKiosk.desktop
#chromium-browser --password-store=basic --chrome-frame --window-size=425,692 --window-position=0,80 --app="($url)"
chromium-browser --password-store=basic --kiosk --chrome-frame --app=$url
