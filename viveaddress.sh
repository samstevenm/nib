#!/bin/sh -eu
ip_addr="$(nmap -n -sn 192.168.2.1/24 -oG - | awk '/Up$/{print $2}' | tail -n+2)"
pre='URL=https://'
url=$pre$ip_addr
echo '[Desktop Entry]' > ~/Desktop/Vive.desktop
echo 'Encoding=UTF-8' >> ~/Desktop/Vive.desktop
echo 'Name=Vive' >> ~/Desktop/Vive.desktop
echo 'Type=Link' >> ~/Desktop/Vive.desktop
echo $url >> ~/Desktop/Vive.desktop
echo 'Icon=text-html' >> ~/Desktop/Vive.desktop
#chromium-browser --password-store=basic --chrome-frame --window-size=425,692 --window-position=0,80 --app="($url)"
chromium-browser --password-store=basic --kiosk --chrome-frame --app="($url)"
