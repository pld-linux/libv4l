Summary:	Abstraction layer on top of video4linux2 devices
Summary(pl.UTF-8):	Warstwa abstrakcji dla urządzeń video4linux2
Name:		libv4l
%define	pkgname	v4l-utils
Version:	0.8.5
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://linuxtv.org/downloads/v4l-utils/%{pkgname}-%{version}.tar.bz2
# Source0-md5:	037bec9f68cfb0b84bcccb00d30e429b
URL:		http://hansdegoede.livejournal.com/
BuildRequires:	QtGui-devel
BuildRequires:	libstdc++-devel
BuildRequires:	sysfsutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Collection of libraries which adds a thin abstraction layer on top of
video4linux2 devices. The purpose of this (thin) layer is to make it
easy for application writers to support a wide variety of devices
without having to write seperate code for different devices in the
same class.

%description -l pl.UTF-8
libv4l to zestaw bibliotek dodający niewielką warstwę abstrakcji dla
urządzeń video4linux2. Celem tej warstwy jest ułatwienie autorom
aplikacji obsługi szerokiej gamy urządzeń bez pisania osobnego kodu
dla różnych urządzeń tej samej klasy.

%package devel
Summary:	Header files for libv4l libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek libv4l
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libv4l libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek libv4l.

%package -n ir-keytable
Summary:	Alter keymaps of Remote Controller devices
License:	GPL v2+
Group:		Applications/Console

%description -n ir-keytable
Dump, Load or Modify IR receiver input tables.

%package -n %{pkgname}
Summary:	Collection of command line video4linux utilities
License:	GPL v2+
Group:		Applications/Console

%description -n %{pkgname}
A series of utilities for media devices, allowing to handle the
proprietary formats available at most webcams (libv4l), and providing
tools to test V4L devices. 

%package -n %{pkgname}-qt
Summary:	Qt V4L2 test Utility
License:	GPL v2+
Group:		X11/Applications

%description -n %{pkgname}-qt
Graphical Qt v4l2 control panel.

%prep
%setup -q -n %{pkgname}-%{version}
%if "%{pld_release}" == "ac"
%{__sed} -i 's/-fvisibility=hidden//' */Makefile
%endif

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcppflags} %{rpmcflags} -Wall" \
	LDFLAGS="%{rpmcflags} %{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=%{_prefix} \
	LIBDIR=%{_libdir} \
	DESTDIR=$RPM_BUILD_ROOT

install utils/rds/rds-saa6588 $RPM_BUILD_ROOT%{_bindir}
install utils/xc3028-firmware/firmware-tool $RPM_BUILD_ROOT%{_bindir}/xc3028-firmware

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libv4l*.so.0
%attr(755,root,root) %{_libdir}/libv4l

%files devel
%defattr(644,root,root,755)
%doc README.lib*
%attr(755,root,root) %{_libdir}/libv4l*.so
%{_includedir}/libv4l*.h
%{_pkgconfigdir}/libv4l*.pc

%files -n ir-keytable
%config(noreplace) %{_sysconfdir}/rc_*
/lib/udev/rules.d/70-infrared.rules
%attr(755,root,root) %{_bindir}/ir-keytable
%{_mandir}/man1/ir-keytable.1*

%files -n %{pkgname}
%doc ChangeLog README TODO contrib
%attr(755,root,root) %{_bindir}/*-ctl
%attr(755,root,root) %{_bindir}/decode_tm6000
%attr(755,root,root) %{_bindir}/rds-saa6588
%attr(755,root,root) %{_bindir}/v4l2-*
%attr(755,root,root) %{_bindir}/xc3028-firmware
%attr(755,root,root) %{_sbindir}/v4l2-dbg

%files -n %{pkgname}-qt
%attr(755,root,root) %{_bindir}/qv4l2
%{_desktopdir}/qv4l2.desktop
%{_iconsdir}/hicolor/*/apps/qv4l2.*
