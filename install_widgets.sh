#!/bin/sh


#echo "Widget Installation"
#if [ "$(id -u)" != "0" ]; then
#   echo "This script must be run as root" >&2
#   exit 1
#fi

source /etc/tizen-platform.conf

wgtdir=${TZ_SYS_SHARE}/widget_demo
if [ -z "$(ls $wgtdir/*.wgt 2> /dev/null)" ]; then
   echo "$wgtdir doesn't contains any widgets (.wgt)" 1>&2
   exit 1
fi

for wgt in $(grep "^$USER" $wgtdir/install.conf | cut -f2 -d':'); do
do 
    echo "installing $wgt"
	if [ -x /usr/bin/wrt-installer ]; then
		wrt-installer -i $wgtdir/$wgt
	else
		xwalkctl -i $wgtdir/$wgt
	fi
done

# setup desktop icons for xwalk
if [ ! -x /usr/bin/wrt-installer ]; then
	for id in $(sqlite3 ~/.config/xwalk-service/applications.db 'select id from applications'); do
		ln -sf /opt/share/applications/xwalk-service.$id.*.desktop ~/.applications/desktop/
	done
fi

[[ "$(id -u)" == "0" ]] && chmod -R a+rw ${TZ_SYS_DB}/

if [ -x /usr/bin/wrt-launcher ]; then
	repo=${TZ_USER_APP}/

	wrt-launcher --list |
	awk 'NR>2{print $2, $5, $6}' |
	while read name packid appid
	do
		bin=$repo/$packid/bin/$appid
		for x in $repo/$packid/res/wgt/*[iI][cC][oO][nN]*; do
		if [[ -f $x ]]; then
			res=$(file -b $x|cut -d , -f 2|tr -d ' '|egrep '[0-9]+x[0-9]+')
			if [[ -n "$res" ]]; then
			diric=${TZ_SYS_SHARE}/icons/hicolor/$res/apps
			[[ -d $diric ]] || mkdir -p $diric
			cp $x $diric/$name.png
			fi
		fi
	   done
		desk=${TZ_SYS_RO_DESKTOP_APP}/$name.desktop
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
fi

#update-desktop-database
#xdg-icon-resource forceupdate

