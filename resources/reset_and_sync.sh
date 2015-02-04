#!/bin/bash
cd resources
./cleardb.sh
cd ..
python manage.py syncdb --noinput
