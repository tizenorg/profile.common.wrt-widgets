Name:       wrt_widgets
Summary:    Wrt_widgets
Version:    0.1
Release:    1
Group:      Framework/system
License:    Apache License, Version 2.0
Source0:    %{name}-%{version}.tar.gz
Requires:  wrt
Requires:  wrt-common
Requires:  wrt-installer 
Requires:  wrt-plugins-tizen
Requires:  wrt-security

%description
Description: Wrt_Widget DEMO


%prep
%setup -q


%build

%install

chmod a+x install_widgets.sh
chmod a+x  load_widget.sh
mkdir -p %{buildroot}/usr/bin/
cp install_widgets.sh %{buildroot}/usr/bin/
cp load_widget.sh %{buildroot}/usr/bin/

if [ ! -d %{buildroot}/root/widget_demo ]
then
	mkdir -p  %{buildroot}/root/widget_demo
fi

cp *.wgt %{buildroot}/root/widget_demo/

%post
mkdir -p /opt/usr/apps
mkdir -p /opt/share/applications
rm /opt/dbspace/.wrt*
wrt_commons_create_clean_db.sh
wrt_reset_all.sh
pkg_initdb
mkdir -p /usr/share/applications_tmp
mv /usr/share/applications/* /usr/share/applications_tmp/
ail_initdb
mv /usr/share/applications_tmp/* /usr/share/applications/
for d in dbspace home usr; do find /opt/$d -exec chsmack -a _ {} \; ; done;


echo "Please Reboot and Execute the scripts install_widgets.sh & load_widget.sh in root mode "

%files
/root/widget_demo/*.wgt
/usr/bin/install_widgets.sh
/usr/bin/load_widget.sh
