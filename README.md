# My-pocket-friend
Easy drop your photocard in your pocket

Install Dietpi on RPI3<br>



Git My-pocket-friend<br>

Make dir /media<br>

mv 100-automountusb.rules to /etc/udev/rules.d/100-automountusb.rules<br>

udevadm control --reload-rules

diet-software / optimised software / Install Nextcloud

If you want to start your MFP on boot, prefer a crontab at rc.local.

crontab -e

Past the line to file end

@reboot python3 /root/mpf.py &
