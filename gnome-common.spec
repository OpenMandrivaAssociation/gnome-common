Name:		gnome-common
Summary:	Gnome-common contains useful things common to building gnome packages
Version: 2.28.0
Release:	%mkrel 3
License: 	GPL
Group:		Development/GNOME and GTK+
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
URL: 		http://www.gnome.org/
Requires:	common-licenses
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	pkgconfig gawk
BuildArch:	noarch

%description
gnome-common is for building various GNOME modules from CVS. It is not
needed to run GNOME.

%prep
%setup -q

%build

# don't use macro, it will confuse configure
./configure --prefix=%{_prefix} --libdir=%{_libdir}

%make

%install
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

%makeinstall

%clean
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc README ChangeLog 
%{_bindir}/*
%{_datadir}/aclocal/*.m4
%{_datadir}/gnome-common
