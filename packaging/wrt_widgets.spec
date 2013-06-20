Name:       wrt_widgets
Summary:    Wrt_widgets
Version:    0.1
Release:    1
Group:      Framework/system
License:    Apache License, Version 2.0
Source0:    %{name}-%{version}.tar.gz
Requires:  wrt
Requires:  wrt-commons
Requires:  wrt-installer 
Requires:  wrt-plugins-tizen
Requires:  wrt-security
Requires:  aul-1-configPC
Requires:  dbus-configPC

%description
Description: Wrt_Widget DEMO


%prep
%setup -q


%build

%install

mkdir -p %{buildroot}/usr/bin/
cp install_widgets.sh %{buildroot}/usr/bin/

if [ ! -d %{buildroot}/root/widget_demo ]
then
	mkdir -p  %{buildroot}/root/widget_demo
fi

cp *.wgt %{buildroot}/root/widget_demo/

%post
##### vconf create table from settings package #########################
# Set vconf values with -g/-u options
GOPTION="-g 6514"

#resetMenuscreen
	# menuscreen app will take this vconf
	#vconftool $GOPTION set -t string db/setting/menuscreen/package_name "com.samsung.cluster-home"


#resetFlightmode
	vconftool $GOPTION set -t bool db/telephony/flight_mode "0" -f

#resetNetwork
	vconftool $GOPTION set -t int db/setting/select_network "0"
	vconftool $GOPTION set -t int db/setting/select_network_act "0"
	vconftool $GOPTION set -t int db/setting/network_mode "0"
	vconftool $GOPTION set -t bool db/setting/3gEnabled "1"
	vconftool $GOPTION set -t bool db/setting/data_roaming "0"

#resetUsbConnectivity
	vconftool $GOPTION set -t int memory/setting/usb_mode "-1" -i -f
	vconftool $GOPTION set -t int memory/setting/usb_sel_mode "0" -i -f
	vconftool $GOPTION set -t int memory/setting/usb_in_mode_change "0" -i -f
	vconftool $GOPTION set -t bool db/setting/debug_mode "1" -f
	vconftool $GOPTION set -t int db/setting/default_rendering_engine "1" -i

#resetSound
	DEFAULT_CALL_TONE="/opt/share/settings/Ringtones/ringtone_sdk.mp3"
	DEFAULT_NOTI_TONE="/opt/share/settings/Alerts/General notification_sdk.wav"

	vconftool $GOPTION set -t bool db/setting/sound/sound_on "1"
	vconftool $GOPTION set -t bool db/setting/sound/vibration_on "0"

	vconftool $GOPTION set -t int db/setting/sound/call/ringtone_sound_volume "13"
	vconftool $GOPTION set -t int db/setting/sound/noti/sound_volume "7"
	vconftool $GOPTION set -t int db/setting/sound/media/sound_volume "7"
	vconftool $GOPTION set -t int db/setting/sound/touch_feedback/sound_volume "5"

	vconftool $GOPTION set -t int db/setting/sound/noti/vibration_level "5"
	vconftool $GOPTION set -t int db/setting/sound/touch_feedback/vibration_level "3"
	vconftool $GOPTION set -t int db/setting/sound/touch_feedback/vibration_level_bak "3" ##private key

	vconftool $GOPTION set -t string db/setting/sound/call/ringtone_path "${DEFAULT_CALL_TONE}"
	vconftool $GOPTION set -t string db/setting/sound/call/ringtone_default_path "${DEFAULT_CALL_TONE}"
	vconftool $GOPTION set -t int db/setting/sound/call/vibration_type "2"

	vconftool $GOPTION set -t string db/setting/sound/noti/msg_ringtone_path	"${DEFAULT_NOTI_TONE}"
	vconftool $GOPTION set -t string db/setting/sound/noti/ringtone_default_path    "${DEFAULT_NOTI_TONE}"
	vconftool $GOPTION set -t int db/setting/sound/noti/msg_alert_rep_type		"0"

	vconftool $GOPTION set -t string db/setting/sound/noti/email_ringtone_path	"${DEFAULT_NOTI_TONE}"
	vconftool $GOPTION set -t int db/setting/sound/noti/email_alert_rep_type		"0"
	vconftool $GOPTION set -t bool db/setting/sound/touch_sounds "1"
	vconftool $GOPTION set -t bool db/setting/sound/sound_lock "1"

#resetWallpaper
	vconftool $GOPTION set -t string db/menu_widget/bgset "/opt/share/settings/Wallpapers/Home_default.jpg"
	vconftool $GOPTION set -t string db/idle_lock/bgset "/opt/share/settings/Wallpapers/Home_default.jpg"

#resetMotions
	vconftool $GOPTION set -t bool db/setting/motion_active "1"

#resetDisplay
	#backlight
# Set backlight timeout to dim display on all platforms except emulator
# 0 sec : unlimited time
# 600 sec : 10 min
%if 0%{?simulator}
	vconftool $GOPTION set -t int db/setting/lcd_backlight_normal "600"
%else
	vconftool $GOPTION set -t int db/setting/lcd_backlight_normal "30"
%endif

	vconftool $GOPTION set -t int db/setting/lcd_timeout_normal_backup "30"

	#brightness
	vconftool $GOPTION set -t int db/setting/Brightness "-1"
	vconftool $GOPTION set -t int db/setting/brightness_automatic "0"

	#battery
	vconftool $GOPTION set -t bool db/setting/battery_percentage "0"
	#launch
	#vconftool $GOPTION set -t string db/menu_widget/launch_effect "0"

#resetPowersaving
	vconftool $GOPTION set -t bool db/setting/pwrsv/system_mode/status "0"
	vconftool $GOPTION set -t bool db/setting/pwrsv/system_mode/reminder "1"

#resetFont
	vconftool $GOPTION set -t int db/setting/font_size "1"
	vconftool $GOPTION set -t int db/setting/font_type "0"

#resetRotationLock
	vconftool $GOPTION set -t bool db/setting/rotate_lock "1"
	vconftool $GOPTION set -t bool db/setting/auto_rotate_screen "0"
	#vconftool $GOPTION set -t bool memory/setting/rotate_hold "0" -i -f
#resetTimeAndData
%ifarch %{arm}
	vconftool $GOPTION set -t bool db/setting/automatic_time_update "1"
%else
	vconftool $GOPTION set -t bool db/setting/automatic_time_update "0"
%endif

	vconftool $GOPTION set -t int db/menu_widget/regionformat_time1224 "1"
	vconftool $GOPTION set -t int db/setting/date_format "0"
	vconftool $GOPTION set -t int db/setting/weekofday_format  "0"

	#-----------------------------------------------------------------
	# MOCK FUNCTION
	# MOCK IMPLEMENTATION FOR API COMPATIBILITY
	# NEED TO CHECK THE KEY WITH THE CALENDAR APP
	#-----------------------------------------------------------------
	vconftool $GOPTION set -t int db/setting/weekofday_format  "0"

	vconftool $GOPTION set -t string db/setting/timezone "+9"
	# to be removed
	vconftool $GOPTION set -t string db/setting/cityname_id "IDS_WCL_BODY_CITYNAME_SEOUL"

	vconftool $GOPTION set -t string db/setting/timezone_id "Asia/Seoul"

	#if [ -f /opt/etc/localtime ]
	#then
	rm -f /opt/etc/localtime
	ln -s /usr/share/zoneinfo/Asia/Seoul /opt/etc/localtime
	#fi


#resetAccessibility
	vconftool $GOPTION set -t bool db/setting/accessibility/accessibility "0"
	vconftool $GOPTION set -t bool db/setting/accessibility/high_contrast "0"
	vconftool $GOPTION set -t bool db/setting/accessibility/screen_zoom "1"
	vconftool $GOPTION set -t int db/setting/accessibility/font_size "1"
	#vconftool $GOPTION set -t int db/setting/accessibility/font_style "0"
	vconftool $GOPTION set -t string db/setting/accessibility/font_name "HelveticaNeue"
	vconftool $GOPTION set -t bool db/setting/accessibility/tts "0"
	vconftool $GOPTION set -t int db/setting/accessibility/speech_rate "2"

	#-----------------------------------------------------------------
	# MOCK FUNCTION
	# NOT SUPPORTED BUT ADDED FOR API COMPATIBILITY
	# temp key for screen reader & speech rate
	#-----------------------------------------------------------------
	vconftool $GOPTION set -t bool db/setting/accessibility/tts "0"
	vconftool $GOPTION set -t int db/setting/accessibility/speech_rate "2"

#resetLanguageAndRegion
	vconftool $GOPTION set -t int db/setting/lang "9"
	vconftool $GOPTION set -t string db/menu_widget/language "en_GB.UTF-8"
	vconftool $GOPTION set -t string db/menu_widget/regionformat "en_GB.UTF-8"

#resetViewtype
	#vconftool $GOPTION set -t int db/menuscreen/viewtype "0"
	#vconftool $GOPTION set -t int db/taskswitcher/viewtype "0"

#resetTouch
	#vconftool $GOPTION set -t int db/setting/vib_feedback "3"
	#vconftool $GOPTION set -t bool db/setting/touch_panel_autolock "0"

#resetLicense
	vconftool $GOPTION set -t bool db/setting/transaction_tracking "0"
	vconftool $GOPTION set -t bool db/setting/expiry_reminder "0"
	vconftool $GOPTION set -t int db/setting/roaming_network "0"

#resetSecurity
	rm -rf /opt/data/setting/set_info
	#vconftool $GOPTION set -t string db/setting/privacy_passwd ""
	vconftool $GOPTION set -t int db/setting/screen_lock_type "5" -f
	vconftool $GOPTION set -t string db/setting/3rd_lock_pkg_name "org.tizen.lockscreen"

	# NOT USED NOW.
	#vconftool $GOPTION set -t bool db/setting/rcs "0"

#resetMemory
	vconftool $GOPTION set -t int db/setting/default_memory/wap "0"
	vconftool $GOPTION set -t int db/setting/default_memory/bluetooth "0"
	vconftool $GOPTION set -t int db/setting/default_memory/camera "0"
	vconftool $GOPTION set -t int db/setting/default_memory/voice_recorder "0"
	vconftool $GOPTION set -t int db/setting/default_memory/fm_radio "0"
	vconftool $GOPTION set -t int db/setting/default_memory/all_share "0"
	vconftool $GOPTION set -t int db/setting/default_memory/adobe_air "0"
	vconftool $GOPTION set -t int db/setting/default_memory/dvb_h "0"

	# format - system server
	#vconftool $GOPTION -i set -t int memory/mmc/format "0"

#resetAbout
	vconftool $GOPTION set -t string db/setting/device_name "Tizen"
	vconftool $GOPTION set -t string db/setting/selected_num ""
#resetMenuWidgets
	vconftool $GOPTION -i set -t int memory/setting/font_changed "0"
	#vconftool $GOPTION -i set -t int memory/mobile_hotspot/skin_changed "0"

#resetDevoptions
	vconftool $GOPTION -i set -t int db/setting/devoption/bgprocess "0"

#resetDisplay
	vconftool $GOPTION set -t string db/setting/screenmode/selected_name "Dynamic"

########################################################################
mkdir -p /opt/usr/apps
mkdir -p /opt/share/applications
mkdir -p /opt/share/packages
rm /opt/dbspace/.wrt*
wrt_commons_create_clean_db.sh
wrt_reset_all.sh
pkg_initdb
mkdir -p /usr/share/applications_tmp
mv /usr/share/applications/* /usr/share/applications_tmp/
mv /usr/share/applications_tmp/*tizen*.desktop /usr/share/applications/
ail_initdb
mv /usr/share/applications_tmp/* /usr/share/applications/
for d in dbspace home usr; do find /opt/$d -exec chsmack -a '*' {} \; ; done;
find  /usr/lib64/ -exec chsmack -a _ {} \;
chmod -R a+rw /opt/dbspace/

echo "Please Reboot and Execute the script install_widgets.sh as user root"

%files
/root/widget_demo/*.wgt
/usr/bin/install_widgets.sh

