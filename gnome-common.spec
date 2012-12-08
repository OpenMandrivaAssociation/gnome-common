Name:		gnome-common
Summary:	Gnome-common contains useful things common to building gnome packages
Version:	3.6.0
Release:	%mkrel 1
License: 	GPLv3+
Group:		Development/GNOME and GTK+
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/3.6/%{name}-%{version}.tar.xz
URL: 		http://www.gnome.org/
Requires:	common-licenses
BuildRequires:	pkgconfig gawk
BuildArch:	noarch

%description
gnome-common is for building various GNOME modules from CVS. It is not
needed to run GNOME.

%prep
%setup -q

%build
%configure2_5x
%make

%install
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

%makeinstall_std

%files
%defattr(-, root, root)
%doc README ChangeLog 
%{_bindir}/*
%{_datadir}/aclocal/*.m4
%{_datadir}/gnome-common


%changelog
* Tue Oct 16 2012 Arkady L. Shane <ashejn@rosalab.ru> 3.6.0-1
- update to 3.6.0

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 2.34.0-2mdv2011.0
+ Revision: 664859
- mass rebuild

* Mon Apr 04 2011 Funda Wang <fwang@mandriva.org> 2.34.0-1
+ Revision: 650124
- new version 2.34.0

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 2.28.0-3mdv2011.0
+ Revision: 605469
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 2.28.0-2mdv2010.1
+ Revision: 521485
- rebuilt for 2010.1

* Mon Sep 21 2009 Götz Waschk <waschk@mandriva.org> 2.28.0-1mdv2010.0
+ Revision: 446588
- update to new version 2.28.0

* Thu Mar 19 2009 Götz Waschk <waschk@mandriva.org> 2.26.0-1mdv2009.1
+ Revision: 358073
- update to new version 2.26.0

* Mon Sep 22 2008 Götz Waschk <waschk@mandriva.org> 2.24.0-1mdv2009.1
+ Revision: 286845
- new version

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 2.20.0-3mdv2009.0
+ Revision: 221084
- rebuild

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 2.20.0-2mdv2008.1
+ Revision: 150122
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Sep 17 2007 Götz Waschk <waschk@mandriva.org> 2.20.0-1mdv2008.0
+ Revision: 89331
- new version

* Tue Apr 17 2007 Götz Waschk <waschk@mandriva.org> 2.18.0-1mdv2008.0
+ Revision: 13996
- new version


* Sun Jan 14 2007 Götz Waschk <waschk@mandriva.org> 2.12.0-3mdv2007.0
+ Revision: 108666
- Import gnome-common

* Sun Jan 14 2007 Götz Waschk <waschk@mandriva.org> 2.12.0-3mdv2007.1
- Rebuild

* Wed Feb 22 2006 Frederic Crozat <fcrozat@mandriva.com> 2.12.0-2mdk
- use mkrel

* Wed Oct 05 2005 Frederic Crozat <fcrozat@mandriva.com> 2.12.0-1mdk
- Release 2.12.0

* Wed Nov 10 2004 G�tz Waschk <waschk@linux-mandrake.com> 2.8.0-1mdk
- fix source URL
- New release 2.8.0

