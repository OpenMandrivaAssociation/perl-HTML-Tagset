%define	upstream_name	 HTML-Tagset
%define	upstream_version 3.20

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	8

Summary:	This module contains data tables useful in dealing with HTML
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/HTML/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module contains data tables useful in dealing with HTML.
It provides no functions or methods.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{_mandir}/*/*
%{perl_vendorlib}/HTML


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 3.200.0-5mdv2012.0
+ Revision: 765306
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 3.200.0-4
+ Revision: 763856
- rebuilt for perl-5.14.x

* Fri Jan 20 2012 Oden Eriksson <oeriksson@mandriva.com> 3.200.0-3
+ Revision: 763069
- rebuild

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 3.200.0-2
+ Revision: 667196
- mass rebuild

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 3.200.0-1mdv2010.1
+ Revision: 406187
- rebuild using %%perl_convert_version

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 3.20-3mdv2009.1
+ Revision: 351963
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 3.20-2mdv2009.0
+ Revision: 223790
- rebuild

* Mon Mar 03 2008 Guillaume Rousse <guillomovitch@mandriva.org> 3.20-1mdv2008.1
+ Revision: 177900
- new version

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sun Jan 14 2007 Olivier Thauvin <nanardon@mandriva.org> 3.10-2mdv2007.0
+ Revision: 108497
- rebuild

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - Import perl-HTML-Tagset

* Thu Nov 10 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 3.10-1mdk
- 3.10
- Don't require perl

* Tue Jan 04 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 3.04-1mdk
- 3.04

