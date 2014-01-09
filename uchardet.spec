Name:       uchardet
Version:    0.0.1
Release:    1%{?dist}
Summary:    Universal charset detection

License:    MPLv1.1
URL:        http://code.google.com/p/uchardet/
Source0:    http://uchardet.googlecode.com/files/%{name}-%{version}.tar.gz

BuildRequires: cmake

%description
uchardet is a C language binding of the original C++ implementation of the
universal charset detection library by Mozilla. uchardet is an encoding
detector library, which takes a sequence of bytes in an unknown character
encoding without any additional information, and attempts to determine the
encoding of the text.

%package devel
Summary: Development files for uchardet
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and Libraries for the package uchardet.

%prep
%setup -q

%build
%cmake
make %{?_smp_mflags}

%install
%make_install
%ifarch x86_64
mv %{buildroot}/usr/lib %{buildroot}%{_libdir}
%endif

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc COPYING AUTHORS
%{_bindir}/%{name}
%{_libdir}/lib%{name}.so.*
%{_mandir}/man1/%{name}.1.*

%files devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}.a
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Sun May 12 2013 Huaren Zhong <huaren.zhong@gmail.com> - 0.0.1
- Rebuild for Fedora