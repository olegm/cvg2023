#!/bin/sh

sudo systemctl stop sensors
sudo systemctl disable sensors

sudo systemctl start partytime
sudo systemctl enable partytime
