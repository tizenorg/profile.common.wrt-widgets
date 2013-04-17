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
for d in dbspace home usr; do find /opt/$d -exec chsmack -a '*' {} \; ; done;
find  /usr/lib64/ -exec chsmack -a _ {} \;


echo "Please Reboot and Execute the script install_widgets.sh as user root"

%files
/root/widget_demo/*.wgt
/usr/bin/install_widgets.sh

