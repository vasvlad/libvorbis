%define keepstatic 1
Name:       libvorbis
Summary:    The Vorbis General Audio Compression Codec
Version:    1.3.7
Release:    1
License:    BSD
URL:        https://www.xiph.org/
Source0:    %{name}-%{version}.tar.bz2
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(ogg)
BuildRequires:  libtool

%description
%{summary}.


%package devel
Summary:    Development tools for Vorbis applications
Requires:   %{name} = %{version}-%{release}

%description devel
%{summary}.


%package devel-static
Summary:    Development tools for Vorbis applications

%description devel-static
%{summary}.


%package doc
Summary:   Documentation for %{name}
BuildArch: noarch
Requires:  %{name} = %{version}-%{release}

%description doc
%{summary}.


%prep
%autosetup -n %{name}-%{version}/upstream

%build
export CFLAGS="$RPM_OPT_FLAGS -fPIC"
%reconfigure --enable-static --disable-shared
%make_build

%install
%make_install

%check
make check

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license COPYING
#%{_libdir}/libvorbis.so.*
#%{_libdir}/libvorbisfile.so.*
#%{_libdir}/libvorbisenc.so.*

%files devel-static
%defattr(-,root,root,-)
%{_libdir}/*.a

%files devel
#%defattr(-,root,root,-)
%{_includedir}/vorbis
#%{_libdir}/libvorbis.so
#%{_libdir}/libvorbisfile.so
#%{_libdir}/libvorbisenc.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/aclocal/vorbis.m4

%files doc
%defattr(-, root, root)
%doc AUTHORS README.md
%{_docdir}/%{name}-*/
