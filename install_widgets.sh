#!/bin/sh


echo "Widget Installation"
if [ "$(id -u)" != "0" ]; then
   echo "This script must be run as root" >&2
   exit 1
fi

wgtdir=/root/widget_demo
if [ -z "$(ls $wgtdir/*.wgt 2> /dev/null)" ]; then
   echo "$wgtdir doesn't contains any widgets (.wgt)" 1>&2
   exit 1
fi

for wgt in $wgtdir/*.wgt
do 
    echo "installing $wgt"
    wrt-installer -i $wgt
done


repo=/opt/usr/apps/
chmod -R a+rw /opt/dbspace/

wrt-launcher --list |
awk 'NR>2{print $2, $5, $6}' |
while read name packid appid
do
    bin=$repo/$packid/bin/$appid
    for x in $repo/$packid/res/wgt/*[iI][cC][oO][nN]*; do
	if [[ -f $x ]]; then
	    res=$(file -b $x|cut -d , -f 2|tr -d ' '|egrep '[0-9]+x[0-9]+')
	    if [[ -n "$res" ]]; then
		diric=/usr/share/icons/hicolor/$res/apps
		[[ -d $diric ]] || mkdir -p $diric
		cp $x $diric/$name.png
	    fi
	fi
    done
    desk=/usr/share/applications/$name.desktop
    cat << EOC > $desk
[Desktop Entry]
Type=Application
Name=$name
Exec=$bin
Icon=$name
Terminal=false
Categories=WRT;Game
EOC
done

update-desktop-database
xdg-icon-resource forceupdate

