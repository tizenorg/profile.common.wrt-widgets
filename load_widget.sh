#! /bin/sh

repo=/opt/usr/apps/

load_widget()
{
    chmod -R a+rw /opt/dbspace/
    for args in `ls $repo` ; do
        if [ $args != "tmp" ]
        then
            echo "    - loading $args"
            echo "---------------------------------------------"
	    chmod a+x $repo/$args/bin/*
            if [ $args == "33CFo0eFJe" ] ; then 
		annex
	    fi
	    if [ $args == "yKrWwxz1KX" ] ; then 
		mancala
	    fi
	    if [ $args == "ewqPdCunAO" ] ; then 
		bubble
	    fi
	    if [ $args == "SM31mV8fq9" ] ; then 
		go
	    fi
	    echo ""
        fi
    done
}

annex()
{
    cp /opt/usr/apps/33CFo0eFJe/res/wgt/annex-icon.png /usr/share/icons/hicolor/128x128/apps/annex.png
cat<<EOF | tee /usr/share/applications/annex.desktop
[Desktop Entry]
Type=Application
Name=Annex
Exec=/opt/usr/apps/33CFo0eFJe/bin/33CFo0eFJe.annex
Icon=/usr/share/icons/hicolor/128x128/apps/annex.png
EOF
}

mancala()
{
    cp /opt/usr/apps/yKrWwxz1KX/res/wgt/icon_128.png /usr/share/icons/hicolor/128x128/apps/mancala.png
cat<<EOF | tee /usr/share/applications/mancala.desktop
[Desktop Entry]
Type=Application
Name=Mancala
Exec=/opt/usr/apps/yKrWwxz1KX/bin/yKrWwxz1KX.mancala
Icon=/usr/share/icons/hicolor/128x128/apps/mancala.png
EOF
}

bubble()
{
    cp /opt/usr/apps/ewqPdCunAO/res/wgt/icon_128.png /usr/share/icons/hicolor/128x128/apps/bubble.png
cat<<EOF | tee /usr/share/applications/bubble.desktop
[Desktop Entry]
Type=Application
Name=BubbleWrap
Exec=/opt/usr/apps/ewqPdCunAO/bin/ewqPdCunAO.bubblewrap
Icon=/usr/share/icons/hicolor/128x128/apps/bubble.png
EOF
}

go()
{
    cp /opt/usr/apps/SM31mV8fq9/res/wgt/Go_Icon_128.png /usr/share/icons/hicolor/128x128/apps/go.png
cat<<EOF | tee /usr/share/applications/go.desktop
[Desktop Entry]
Type=Application
Name=Go
Exec=/opt/usr/apps/SM31mV8fq9/bin/SM31mV8fq9.Go
Icon=/usr/share/icons/hicolor/128x128/apps/go.png
EOF
}


load_widget
