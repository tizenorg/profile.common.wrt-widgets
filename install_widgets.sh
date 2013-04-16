#!/bin/sh
PWD_I=`pwd`
echo "Widget Installation"
if [ "$(id -u)" != "0" ]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi
FILE=`ls *.wgt` 
if [ -z "$FILE" ]; then
   echo "$PWD_I doesn't contains any widgets (.wgt)" 1>&2
   exit 1
fi
for i in $FILE
do 
wrt-installer -i $PWD_I/$i
done

