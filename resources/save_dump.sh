#!/bin/bash
python2.7 manage.py dumpdata portal municipios blog zinnia publicador auth.User | python -m json.tool > /home/photosite/webapps/photoplay2/photoplay/photoplay/fixtures/initial_data.json
