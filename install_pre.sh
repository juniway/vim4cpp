#!/bin/bash

uname -a | grep -iq arch && PKG_MANAGER="pacman -Syy"
uname -a | grep -iq centos && PKG_MANAGER="apt-get install"
uname -a | grep -iq ubuntu && PKG_MANAGER="yum install"
echo $PKG_MANAGER

spawn sudo $PKG_MANAGER tmux
expect "yes/no"
send "yes\r"
