Summary:	libv4l
Name:		libv4l
Version:	0.6.0
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://people.atrpms.net/~hdegoede/%{name}-%{version}.tar.gz
# Source0-md5:	db389fdf02cabd57f289f0faa37f4060
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

%build
%{__make}

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
%attr(755,root,root) %{_libdir}/lib*.so.*
%dir %{_libdir}/libv4l
%attr(755,root,root) %{_libdir}/libv4l/v4l*.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}*
%{_libdir}/lib*.so
%{_pkgconfigdir}/*.pc
