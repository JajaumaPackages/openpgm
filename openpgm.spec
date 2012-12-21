Name:          openpgm
Version:       5.1.118
Release:       1%{?dist}
Summary:       An implementation of the PGM reliable multicast protocol

Group:         System Environment/Libraries
# The license is LGPLv2.1
License:       LGPLv2
URL:           http://openpgm.googlecode.com/
Source0:       http://openpgm.googlecode.com/files/libpgm-%{version}%7Edfsg.tar.gz

BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


%description
OpenPGM is an open source implementation of the Pragmatic General
Multicast (PGM) specification in RFC 3208.


%package devel
Summary:       Development files for openpgm
Group:         Development/Libraries
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains OpenPGM related development libraries and header files.


%prep
%setup -q -n libpgm-%{version}~dfsg/openpgm/pgm

%build
%configure
make %{_smp_mflags}

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

rm %{buildroot}%{_libdir}/libpgm.{a,la}

%clean
rm -rf %{buildroot}


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc COPYING LICENSE
%{_libdir}/*.so.*


%files devel
%defattr(-,root,root,-)
%doc examples/
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/openpgm-5.1.pc


%changelog
* Wed Dec 19 2012 Jose Pedro Oliveira <jpo at di.uminho.pt> - 5.1.118-1
- Change license from LGPLv2.1 to LGPLv2 (867182#c13)

* Tue Dec 18 2012 Jose Pedro Oliveira <jpo at di.uminho.pt> - 5.1.118-0
- First Fedora specfile

# vim:set ai ts=4 sw=4 sts=4 et:
