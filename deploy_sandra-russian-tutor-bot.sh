#!/bin/sh
cd ~/sandra-russian-tutor-bot
git fetch --all
git reset --hard origin/main
git pull origin main
kill $(pgrep -f bot.py)
nohup python3 bot.py &
echo "Bot script updated and restarted successfully."