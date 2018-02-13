# nib
Network in a box

## RPI-
1. Username: joel, Password: joelspira
2. Notes
  + Sharing WiFi to Ethernet, used `changeip.sh` to set to 192.168.2.1/24 (default is 10.42.0.1/24)
  + Auto-launches Chrome in Kiosk Mode on Boot.  Use ALT-F4 to kill, if desired.
  + `dpkg -i /path/to/VNC-ServerXXX.deb` to install REALVNC, since this is Mate not Raspian
  + `startvncviewer.sh` used to start/ enable start at boot
  + Other scripts are attempts to simplify launching Chrome/Connecting to Hub

## REALVNC- 
1. EMAIL: viveqts@gmail.com
2. Password: joelspira

## Vive Hub- 
1. Password: joelspira
2. Static IP: 192.168.2.102

## Verizon Hotspot- 
1. SSID: Lutron Hotspot
2. Password: joelspira
3. Admin Password: joelspira
4. IP: 192.168.1.1

# Setup
1. Ensure Hotspot is on/ plugged in
2. Connect Hub to RasPi with CAT5
3. Plug in Hub Power (24Vdc Phoenix)
4. Plug in RasPI power (5Vdc USB)
5. Open REALVNCViewer on any device and log in with REALVNC credentials
6. Connect to joel-desktop, log in with RPI credentials
7. You can always check the Ethernet Settings on Hub WiFi to verify
8. Might be useful to find Hub: `nmap -n -sn 192.168.2.1/24 -oG - | awk '/Up$/{print $2}'`
