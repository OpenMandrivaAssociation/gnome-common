%define _disable_rebuild_configure 1

Summary:	Gnome-common contains useful things common to building gnome packages
Name:		gnome-common
Version:	3.18.0
Release:	1
License:	GPLv3+
Group:		Development/GNOME and GTK+
Url:		http://www.gnome.org/
Source0:	http://download.gnome.org/sources/gnome-common/%{url_version}/%{name}-%{version}.tar.xz
BuildArch:	noarch

BuildRequires:	gawk
Requires:	common-licenses

%description
gnome-common is for building various GNOME modules from CVS. It is not
needed to run GNOME.

%prep
%setup -q

%build
%configure
%make

%install
%makeinstall_std

%files
%doc README ChangeLog 
%{_bindir}/*
%{_datadir}/aclocal/*.m4

