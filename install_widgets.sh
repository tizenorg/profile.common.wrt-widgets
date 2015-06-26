#!/bin/sh

. /etc/tizen-platform.conf

function info() {
	local ts=$(date +%Y%m%d.%H%M%S)
	echo $ts "$@" >&2
}

function do_install() {
	info "------------- wrt_widgets install start --------------"

	local wgtdir=${TZ_SYS_SHARE}/widget_demo
	if [ -n "$(ls $wgtdir/*.wgt 2> /dev/null)" ]; then
		local nbinstall=0
		for wgt in $(grep "^$USER" $wgtdir/install.conf | cut -f2 -d':'); do
			info "installing $wgt" 
			local try=1
			local ok=0
			while [ $try -le 3 ]; do
				flock -w 30 -e /tmp/pkgcmd_lock pkgcmd -i -q -t wgt -p $wgtdir/$wgt && { ok=1; break; }
				try=$((try+1))
				sleep 1
			done
			[ $ok -eq 1 ] && {
				info "$wgt installed successfully" 
				nbinstall=$((nbinstall+1))
			} || info "failed to install $wgt" 
		done

		# signal tz-launcher that new apps were installed
		info "$nbinstall applications installed" 
		if [ $nbinstall -gt 0 ]; then
			info "sending restart signal to tz-launcher"
			pkill -USR1 -U $UID tz-launcher
		fi
	else
		info "$wgtdir hasn't installed widget (.wgt), init the bases..."
		pkgcmd -l
		info "init done"
	fi

	info "------------- wrt_widgets install end --------------"
}

do_install >>~/.applications/install.log 2>&1 

touch ~/.applications/install_done

# never fail
exit 0

