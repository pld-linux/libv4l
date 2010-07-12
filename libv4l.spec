Summary:	libv4l
Name:		libv4l
Version:	0.6.4
Release:	1
License:	GPL v2
Group:		Applications
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

%package devel
Summary:	Header files for libv4l library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libv4l library.

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
%attr(755,root,root) %{_libdir}/libv4l1.so.?
%attr(755,root,root) %{_libdir}/libv4l2.so.?
%attr(755,root,root) %{_libdir}/libv4lconvert.so.?
%dir %{_libdir}/libv4l
%attr(755,root,root) %{_libdir}/libv4l/v4l*.so
%attr(755,root,root) %{_libdir}/libv4l/ov511-decomp
%attr(755,root,root) %{_libdir}/libv4l/ov518-decomp

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libv4l1.so
%attr(755,root,root) %{_libdir}/libv4l2.so
%attr(755,root,root) %{_libdir}/libv4lconvert.so
%{_includedir}/libv4l1.h
%{_includedir}/libv4l2.h
%{_includedir}/libv4lconvert.h
%{_pkgconfigdir}/libv4l1.pc
%{_pkgconfigdir}/libv4l2.pc
%{_pkgconfigdir}/libv4lconvert.pc
