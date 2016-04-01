Name:           steamos-modeswitch-inhibitor
Version:        1.9.2
Release:        1%{?dist}
Summary:        SteamOS Mode Switch Inhibitor

License:        BSD
URL:            http://store.steampowered.com/steamos/
Source0:        http://repo.steampowered.com/steamos/pool/main/s/%{name}/%{name}_%{version}.tar.gz
 
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libX11-devel
BuildRequires:  libXxf86vm-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXrender-devel
BuildRequires:  libXcomposite-devel
BuildRequires:  libtool
BuildRequires:  mesa-libGL-devel

%description
Shared library which fakes any mode switch attempts to prevent full screen apps
from changing resolution.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and
header files for developing applications that use %{name}.

%prep
%setup -q

%build
autoreconf -vif
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -name "*.la" -delete
rm -fr %{buildroot}%{_docdir}/%{name}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc debian/copyright debian/changelog
%{_libdir}/libmodeswitch_inhibitor.so.*

%files devel
%{_libdir}/libmodeswitch_inhibitor.so

%changelog
* Fri Jul 31 2015 Simone Caronni <negativo17@gmail.com> - 1.9.2-1
- Update to 1.9.2.

* Thu May 21 2015 Simone Caronni <negativo17@gmail.com> - 1.9.1-2
- Add libX11 build requirement for RHEL 7.

* Sun Jun  8 2014 Simone Caronni <negativo17@gmail.com> - 1.9.1-1
- First build.
