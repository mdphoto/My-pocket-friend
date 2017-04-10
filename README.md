# My-pocket-friend
Easy drop your photocard in your pocket

If you want to start your MFP on boot, prefer a crontab at rc.local.
MFP need a root access.
-sudo or su crontab -e
Paste the line to file end
@reboot python3 /home/michel/biloute.py > /home/michel/biloute.log 2>&1
