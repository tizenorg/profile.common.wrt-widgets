#!/bin/sh

##### vconf create table from settings package #########################
# Set vconf values with -g/-u options

source /etc/tizen-platform.conf

rm -rf ${TZ_SYS_DATA}/setting/set_info

#### Bluetotth API ####################################################
vconftool set -t string db/menu_widget/regionformat "en_GB.UTF-8"
vconftool set -t int db/menu_widget/regionformat_time1224 "1"
vconftool set -t string db/setting/accessibility/font_name "HelveticaNeue"

########################################################################
#  PC Specific Environment settings


mkdir -p ${TZ_SYS_RW_PACKAGES}
rm -f ${TZ_SYS_DB}/.wrt*

if [ -x /usr/bin/wrt-client ]; then
	wrt_commons_create_clean_db.sh
	wrt_reset_db.sh
fi
pkg_initdb
ail_initdb

##### WA : To allow multi-user launch  ##########
chmod -R a+rw ${TZ_SYS_DB}/

