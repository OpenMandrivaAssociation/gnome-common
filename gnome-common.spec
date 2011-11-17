Name:		gnome-common
Summary:	Gnome-common contains useful things common to building gnome packages
Version:	3.1.0
Release:	1
License: 	GPLv3+
Group:		Development/GNOME and GTK+
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz
URL: 		http://www.gnome.org/
Requires:	common-licenses

BuildRequires:	gawk
BuildArch:	noarch

%description
A module that is required only when building GNOME from the repository. 
It is not needed to run GNOME.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}

%makeinstall_std

%files
%doc README ChangeLog 
%{_bindir}/*
%{_datadir}/aclocal/*.m4
%{_datadir}/gnome-common

