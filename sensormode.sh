#!/bin/sh

sudo systemctl stop partytime
sudo systemctl disable partytime

sudo systemctl start sensors
sudo systemctl enable sensors
