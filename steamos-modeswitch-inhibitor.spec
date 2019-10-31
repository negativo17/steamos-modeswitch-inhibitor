Name:           steamos-modeswitch-inhibitor
Version:        1.10
Release:        2%{?dist}
Summary:        SteamOS Mode Switch Inhibitor

License:        BSD
URL:            http://store.steampowered.com/steamos/
Source0:        http://repo.steampowered.com/steamos/pool/main/s/%{name}/%{name}_%{version}.tar.xz
 
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  libXcomposite-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xxf86vm)

%description
Shared library which fakes any mode switch attempts to prevent full screen apps
from changing resolution.

%prep
%setup -q

%build
autoreconf -vif
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot} -name "*.la" -delete
find %{buildroot} -name "*.so" -delete
rm -fr %{buildroot}%{_docdir}/%{name}

%ldconfig_scriptlets

%files
%doc debian/copyright debian/changelog
%{_libdir}/libmodeswitch_inhibitor.so.*

%changelog
* Sun Jan 27 2019 Simone Caronni <negativo17@gmail.com> - 1.10-2
- Update SPEC file.
- Remove devel subpackage.

* Fri Apr 01 2016 Simone Caronni <negativo17@gmail.com> - 1.10-1
- Update to 1.10.

* Fri Jul 31 2015 Simone Caronni <negativo17@gmail.com> - 1.9.2-1
- Update to 1.9.2.

* Thu May 21 2015 Simone Caronni <negativo17@gmail.com> - 1.9.1-2
- Add libX11 build requirement for RHEL 7.

* Sun Jun  8 2014 Simone Caronni <negativo17@gmail.com> - 1.9.1-1
- First build.
