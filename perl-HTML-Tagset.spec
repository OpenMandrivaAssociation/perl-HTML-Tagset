%define	module	HTML-Tagset
%define name	perl-%{module}
%define	version	3.20
%define	release	%mkrel 1

Summary: 	This module contains data tables useful in dealing with HTML
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	GPL
Group: 		Development/Perl
URL:		http://search.cpan.org/dist/%{module}/
Source:     http://www.cpan.org/modules/by-module/HTML/%{module}-%{version}.tar.gz
BuildArch:	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}

%description
This module contains data tables useful in dealing with HTML.
It provides no functions or methods.

%prep
%setup -q -n %{module}-%{version}

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


