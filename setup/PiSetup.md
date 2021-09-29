## RasPi Initial Setup
1. Copy the wpa_supplicant.conf to the RasPi
1. Connect to raspi over ssh
1. Run Raspi-config to set WI-Fi to US
1. `sudo apt update && sudo apt upgrade`

Install Tailscale
Place `wifi-to-eth-route.sh` in `/opt`
Place `wifiroute.service` in `/etc/systemd/system`

Raspi comes up (reachable over Tailscale) in about 35 to 45 seconds < 1min
WiFi route starts working almost immediately
WiFi bridge starts working in about 1 minute 30 seconds <2min

TODO: IF no internet for ahwile, kill the autohotspot and run the autohotspot script
Testing AutoHotspot- change wpa_supplicant.conf to contain bad info (just make the password or SSID wrong), reboot. hotspot should turn on for "recovery mode"