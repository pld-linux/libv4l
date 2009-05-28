Summary:	libv4l
Name:		libv4l
Version:	0.1
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://people.atrpms.net/~hdegoede/%{name}-%{version}.tar.gz
# Source0-md5:	3965a3bd8568e9c349e6ae89521db84d
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
install -d $RPM_BUILD_ROOT%{_includedir}/%{name}
install -d $RPM_BUILD_ROOT%{_libdir}
install include/* $RPM_BUILD_ROOT%{_includedir}/%{name}
install lib/lib*.so* $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%attr(755,root,root) %{_libdir}/lib*.so.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}
%{_libdir}/lib*.so
