Name:       wrt-widgets
Summary:    Wrt-widgets Installer
Version:    0.1
Release:    1
Group:      Web Framework/Web Run Time
License:    Apache-2.0
Source0:    %{name}-%{version}.tar.gz
Requires:   wrt
Requires:   wrt-commons
Requires:   wrt-installer 
Requires:   wrt-plugins-tizen
Requires:   wrt-security
Requires:   daemon-launch-config-pc
Requires:   dbus-config-pc
Requires:   nodejs
Requires:   web-ui-fw
Requires:   web-ui-fw-demo-tizen-winsets
Requires:   web-ui-fw-theme-default
Requires:   web-ui-fw-theme-tizen-black
Requires:   web-ui-fw-theme-tizen-white
Requires:   web-ui-fw-devel

%description
Wrt-widgets prepare a suitable pc oriented environment to install WRT widgets
After installing wrt-widgets, launch install_widgets.sh script as root to install them.

%prep
%setup -q

%build

%install

mkdir -p %{buildroot}/%{_bindir}
cp install_widgets.sh %{buildroot}/%{_bindir}
cp prepare_widgets.sh %{buildroot}/%{_bindir}

if [ ! -d %{buildroot}/%{_datadir}/widget_demo ]
then
    mkdir -p  %{buildroot}/%{_datadir}/widget_demo
fi

cp -r *.wgt %{buildroot}/%{_datadir}/widget_demo/

%post
%{_bindir}/prepare_widgets.sh

%files
%{_datadir}/widget_demo/*.wgt
%attr(755,root,root) %{_bindir}/install_widgets.sh
%attr(755,root,root) %{_bindir}/prepare_widgets.sh
