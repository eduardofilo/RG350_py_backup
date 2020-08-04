#!/bin/sh

export HOME=`cat /etc/passwd |head -1 |cut -d':' -f 6`

# Restore the framebuffer to a working state
/usr/sbin/unlockvt > /dev/null

# Reset the console
/usr/bin/reset

# Disactivate the console on framebuffer
echo 0 > /sys/devices/virtual/vtconsole/vtcon1/bind

# Disable downscaling for future apps
if [ -f /sys/devices/platform/jz-lcd.0/allow_downscaling ] ; then
        echo 0 > /sys/devices/platform/jz-lcd.0/allow_downscaling
fi

# Restore the regular key map
if [ -f /sys/devices/platform/linkdev/alt_key_map ] ; then
        echo 0 > /sys/devices/platform/linkdev/alt_key_map
fi

# Stop the gravity sensor if it's loaded
/usr/sbin/gsensor --stop

# Source /etc/profile to set the environment variables
. /etc/profile

# Creating home directory for config
if [ ! -f /media/data/local/home/.pystatesbackup ] ; then
    mkdir /media/data/local/home/.pystatesbackup
    cp config.txt /media/data/local/home/.pystatesbackup
fi

python main.py
