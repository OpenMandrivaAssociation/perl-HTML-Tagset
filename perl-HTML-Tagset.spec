%define	module	HTML-Tagset
%define name	perl-%{module}
%define	version	3.10
%define	release	%mkrel 2

Summary: 	This module contains data tables useful in dealing with HTML
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	GPL
Group: 		Development/Perl
Source:		http://www.cpan.org/authors/id/S/SB/SBURKE/%{module}-%{version}.tar.bz2
URL:		http://search.cpan.org/dist/%{module}/
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRoot: 	%{_tmppath}/%{name}-buildroot/

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
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/*/*
%{perl_vendorlib}/HTML


