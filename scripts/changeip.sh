#!/bin/sh -eu
nmcli connection modify 'Wired connection 1' +ipv4.addresses 192.168.2.1/24
sudo ip addr flush 'enxb827eb76559a'
sudo systemctl restart networking
