#!/bin/sh

##### vconf create table from settings package #########################
# Set vconf values with -g/-u options
GOPTION="-g 6514"

rm -rf /opt/data/setting/set_info

#### Bluetotth API ####################################################
vconftool $GOPTION set -t string db/menu_widget/regionformat "en_GB.UTF-8"
vconftool $GOPTION set -t int db/menu_widget/regionformat_time1224 "1"
vconftool $GOPTION set -t string db/setting/accessibility/font_name "HelveticaNeue"

########################################################################
#  PC Specific Environment settings


mkdir -p /opt/share/packages
rm /opt/dbspace/.wrt*
wrt_commons_create_clean_db.sh
wrt_reset_db.sh
pkg_initdb

##### WA : To reduce database creation duration : https://review.tizen.org/gerrit/5452/
mkdir -p /usr/share/applications_tmp
mv /usr/share/applications/* /usr/share/applications_tmp/
mv /usr/share/applications_tmp/*tizen*.desktop /usr/share/applications/
ail_initdb
mv /usr/share/applications_tmp/* /usr/share/applications/

##### WA : To allow multi-user launch  ##########
chmod -R a+rw /opt/dbspace/

