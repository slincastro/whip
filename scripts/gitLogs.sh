#!/bin/bash
echo 'Repository Path:' $1
echo 'Json storage Path:' $2

rm $2
cd $1 && git log --pretty=format:'{ "name": "%aN",    "email": "%aE",    "date": "%aD"},' >> $2