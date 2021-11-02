Name:           libpal
Version:        0.9.8
Release:        1%{?dist}
Summary:        Positional Astronomy Library

License:        LGPLv3+ and GPLv3+
URL:            https://github.com/Starlink/pal
Source0:        https://github.com/Starlink/pal/releases/download/v%{version}/pal-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  erfa-devel

%description
The PAL library is a partial re-implementation of Pat Wallace's popular SLALIB
library written in C using a Gnu GPL license and layered on top of the IAU's
SOFA library (or the BSD-licensed ERFA) where appropriate. PAL attempts to
stick to the SLA C API where possible although palObs() has a more C-like API
than the equivalent slaObs() function. In most cases it is enough to simply
change the function prefix of a routine in order to link against PAL rather
than SLALIB. Routines calling SOFA use modern nutation and precession models
so will return slightly different answers than native SLALIB. PAL functions
not available in SOFA were ported from the Fortran version of SLALIB that
ships as part of the Starlink software and uses a GPL licence.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n pal-%{version}


%build
%configure --disable-static --with-external_cminpack --with-external_pal
%make_build


%install
%make_install
find %{buildroot} -name '*.la' -delete
# Docs and licenses copied to strange places
rm -r %{buildroot}%{_prefix}/{manifests,news,share/pal}


%check
make check


%files
%license COPYING*
%doc README.md pal.news sun267.pdf
%{_libdir}/*.so.0*

%files devel
%{_includedir}/*
%{_libdir}/*.so


%changelog
* Fri Oct 29 2021 Orion Poplawski <orion@nwra.com> - 0.9.8-1
- Initial package
