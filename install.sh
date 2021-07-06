#!/usr/bin/env bash
# This Programm write by Mr.nope
# PyEx 1.2.0

if [[ "$(id -u)" -ne 0 ]]; then
  echo "Please, Run This Programm as Root!"
  echo ""
  exit 1
fi
clear
echo "Installing..."
sleep 2
chmod +x run.py
apt update
apt upgrade
apt install python
apt install python3
echo ""
echo "Installing..., Finish...!"
echo ""
exit 1