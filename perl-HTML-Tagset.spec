%define	upstream_name	 HTML-Tagset
%define	upstream_version 3.20

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 4

Summary: 	This module contains data tables useful in dealing with HTML
License: 	GPL
Group: 		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:    http://www.cpan.org/modules/by-module/HTML/%{upstream_name}-%{upstream_version}.tar.gz

BuildArch:	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}

%description
This module contains data tables useful in dealing with HTML.
It provides no functions or methods.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%clean 
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/*/*
%{perl_vendorlib}/HTML
