## RasPi Initial Setup
1. Copy the wpa_supplicant.conf to the RasPi
1. Connect to raspi over ssh
1. Run Raspi-config to set WI-Fi to US
1. `sudo apt update && sudo apt upgrade`
1. Install and connect Tailscale - https://tailscale.com/download
1. Place `wifi-to-eth-route.sh` in `/opt`

### WACnet
1. Download WACnet
    1. Put latest version of wacnet into `/opt/wacnet`
    1. Get the last version from https://hvac.io/docs/wacnet
    1. `sudo mkdir -p /opt/wacnet`
    1. `sudo wget -P /opt/wacnet https://hvac.io/wacnet/wacnet-2.1.7-standalone.jar`
1. Make WACnet a service
    1. Place `wacnet.service` into `/etc/systemd/system`
    1. `sudo wget -P /etc/system/systemd https://raw.githubusercontent.com/samstevenm/nib/master/systemd/wacnet.service`
    1. `sudo systemctl enable wacnet.service`


Raspi comes up (reachable over Tailscale) in about 35 to 45 seconds < 1min
WiFi route starts working almost immediately
WiFi bridge starts working in about 1 minute 30 seconds <2min

TODO: IF no internet for ahwile, kill the autohotspot and run the autohotspot script
Testing AutoHotspot- change wpa_supplicant.conf to contain bad info (just make the password or SSID wrong), reboot. hotspot should turn on for "recovery mode"