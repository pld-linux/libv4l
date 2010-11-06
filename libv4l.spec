Summary:	libv4l - abstraction layer on top of video4linux2 devices
Summary(pl.UTF-8):	libv4l - warstwa abstrakcji dla urządzeń video4linux2
Name:		libv4l
Version:	0.6.4
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://people.fedoraproject.org/~jwrdegoede/%{name}-%{version}.tar.gz
# Source0-md5:	7ef58595dc36252be7f83f69b379a715
URL:		http://hansdegoede.livejournal.com/3636.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libv4l is a collection of libraries which adds a thin abstraction
layer on top of video4linux2 devices. The purpose of this (thin) layer
is to make it easy for application writers to support a wide variety
of devices without having to write seperate code for different devices
in the same class.

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

%prep
%setup -q
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

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%attr(755,root,root) %{_libdir}/libv4l1.so.0
%attr(755,root,root) %{_libdir}/libv4l2.so.0
%attr(755,root,root) %{_libdir}/libv4lconvert.so.0
%dir %{_libdir}/libv4l
%attr(755,root,root) %{_libdir}/libv4l/v4l1compat.so
%attr(755,root,root) %{_libdir}/libv4l/v4l2convert.so
%attr(755,root,root) %{_libdir}/libv4l/ov511-decomp
%attr(755,root,root) %{_libdir}/libv4l/ov518-decomp

%files devel
%defattr(644,root,root,755)
%doc README.multi-threading
%attr(755,root,root) %{_libdir}/libv4l1.so
%attr(755,root,root) %{_libdir}/libv4l2.so
%attr(755,root,root) %{_libdir}/libv4lconvert.so
%{_includedir}/libv4l1.h
%{_includedir}/libv4l2.h
%{_includedir}/libv4lconvert.h
%{_pkgconfigdir}/libv4l1.pc
%{_pkgconfigdir}/libv4l2.pc
%{_pkgconfigdir}/libv4lconvert.pc
