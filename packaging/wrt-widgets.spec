Name:       wrt-widgets
Summary:    Wrt-widgets Installer
Version:    0.1
Release:    1
Group:      Web Framework/Web Run Time
License:    Apache-2.0
BuildArch:  noarch
Source0:    %{name}-%{version}.tar.gz
Source1001: wrt-widgets.manifest
BuildRequires: pkgconfig(libtzplatform-config)
Requires:   libtzplatform-config
Requires:   desktop-skin

%description
Wrt-widgets prepare a suitable pc oriented environment to install Web apps
After installing wrt-widgets, widgets will be installed at first boot.

%prep
%setup -q
cp %{SOURCE1001} .

%build

%install

mkdir -p %{buildroot}/%{_bindir}
cp install_widgets.sh %{buildroot}/%{_bindir}

mkdir -p  %{buildroot}/%{TZ_SYS_SHARE}/widget_demo
cp -r apps/*.wgt %{buildroot}/%{TZ_SYS_SHARE}/widget_demo/
#cp -r apps/*.png %{buildroot}/%{TZ_SYS_SHARE}/widget_demo/
#cp -r apps/*.desktop %{buildroot}/%{TZ_SYS_SHARE}/widget_demo/
cp install.conf %{buildroot}/%{TZ_SYS_SHARE}/widget_demo/

# install xwalk preinstall service in user session
mkdir -p %{buildroot}%{_unitdir_user}
install -m 644 xwalk_widgets_preinstall.service %{buildroot}%{_unitdir_user}/

%post
# setup xwalk preinstall service (inside user session)
mkdir -p %{_unitdir_user}/default.target.wants/
ln -sf ../xwalk_widgets_preinstall.service %{_unitdir_user}/default.target.wants/

%postun
rm -f %{_unitdir_user}/default.target.wants/xwalk_widgets_preinstall.service

%files
%manifest %{name}.manifest
%defattr(-,root,root)
%{TZ_SYS_SHARE}/widget_demo/*
%attr(755,root,root) %{_bindir}/install_widgets.sh
%{_unitdir_user}/xwalk_widgets_preinstall.service

