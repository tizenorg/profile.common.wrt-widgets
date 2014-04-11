Name:       wrt-widgets
Summary:    Wrt-widgets Installer
Version:    0.1
Release:    1
Group:      Web Framework/Web Run Time
License:    Apache-2.0
BuildArch:  noarch
Source0:    %{name}-%{version}.tar.gz
BuildRequires: pkgconfig(libtzplatform-config)
Requires:   libtzplatform-config

%description
Wrt-widgets prepare a suitable pc oriented environment to install Web apps
After installing wrt-widgets, launch install_widgets.sh script as root to install them.

%prep
%setup -q

%build

%install

mkdir -p %{buildroot}/%{_bindir}
cp install_widgets.sh %{buildroot}/%{_bindir}
cp prepare_widgets.sh %{buildroot}/%{_bindir}

mkdir -p  %{buildroot}/%{TZ_SYS_SHARE}/widget_demo
cp -r *.wgt %{buildroot}/%{TZ_SYS_SHARE}/widget_demo/

%post

%files
%{TZ_SYS_SHARE}/widget_demo/*.wgt
%attr(755,root,root) %{_bindir}/install_widgets.sh
%attr(755,root,root) %{_bindir}/prepare_widgets.sh
