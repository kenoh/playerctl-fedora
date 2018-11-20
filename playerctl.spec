Name:		playerctl
Version:	2.0.1
Release:	1%{?dist}
Summary:	mpris command-line controller and library for spotify, vlc, audacious, bmp, cmus, and others.

License:	GPL
URL:		https://github.com/acrisci/playerctl
Source0:	https://github.com/acrisci/playerctl/archive/v%{version}.tar.gz

BuildRequires:	redhat-rpm-config, gobject-introspection-devel, gtk-doc, libtool
BuildRequires:  meson >= 0.46

%description


%package devel
Summary: playerctl development files
Requires: playerctl%{?_isa} = %{version}-%{release}

%description devel


%prep
%setup -q


%build
meson --prefix="%{_prefix}" --libdir="%{_libdir}" mesonbuild


%install
export DESTDIR=%{buildroot}
ninja -C mesonbuild install

rm %{buildroot}%{_libdir}/libplayerctl.a


%files
%doc
%{_bindir}/playerctl
%{_libdir}/*
%{_mandir}/*
%{_datarootdir}/*

%files devel
%{_includedir}/*



%changelog
* Tue Nov 20 2018 Matus Honek <kenoh@bubbablue> - 2.0.1-1
- Initial spec
