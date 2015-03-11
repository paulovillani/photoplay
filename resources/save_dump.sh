#!/bin/bash
python manage.py dumpdata portal municipios blog zinnia  | python -m json.tool > /home/photo/apps/photoplay/photoplay/fixtures/initial_data.json
