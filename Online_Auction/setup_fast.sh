#!/bin/bash
cd /workspaces/xjankaj/Online_Auction
pkill -9 python
python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py runserver 8000 &
echo "Server starting on port 8000..."
