#!/bin/bash
python manage.py dumpdata portal municipios | python -m json.tool > /home/photo/apps/photoplay/photoplay/fixtures/initial_data.json
