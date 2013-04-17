#! /bin/sh

repo=/opt/usr/apps/
chmod -R a+rw /opt/dbspace/

dbwdgt() {
cat << EOC
33CFo0eFJe  Annex
yKrWwxz1KX  Mancala
ewqPdCunAO  BubbleWrap
SM31mV8fq9  Go
EOC
}

dbwdgt |
while read id name
do
    bin=$(ls /opt/usr/apps/$id/bin/$id.*)
    for x in /opt/usr/apps/$id/res/wgt/*[iI][cC][oO][nN]*; do
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

