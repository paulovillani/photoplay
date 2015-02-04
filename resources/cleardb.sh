#!/bin/sh

PROJNAME='photoplay';
SETTINGSFILE='settings.py';
`perl -n -e"s/^[ ]+'([A-Z]+)':[ ]+'([^']+)'.*$/export \1=\2/ && /NAME|USER|PASSWORD|HOST/ && print $1" ../$PROJNAME/$SETTINGSFILE`

CLEARSQL=`mktemp`

echo SET AUTOCOMMIT=0\; >> $CLEARSQL
echo SET FOREIGN_KEY_CHECKS=0\; >> $CLEARSQL
mysqldump -h $HOST -u $USER --password=$PASSWORD --add-drop-table --no-data $NAME | grep ^DROP >> $CLEARSQL
echo SET FOREIGN_KEY_CHECKS=1\; >> $CLEARSQL
echo COMMIT\; >> $CLEARSQL
echo SET AUTOCOMMIT=1\; >> $CLEARSQL

cat $CLEARSQL | mysql -h $HOST -u $USER --password=$PASSWORD $NAME
rm $CLEARSQL
