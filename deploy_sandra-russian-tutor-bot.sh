#!/bin/sh
cd ~/sandra-russian-tutor-bot
git fetch --all
git reset --hard origin/main
git pull origin main
kill $(pgrep -f bot.py)
/usr/bin/nohup python3 bot.py >mylogfile.log 2>&1 &
echo "Bot script updated and restarted successfully."