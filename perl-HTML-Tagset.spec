%define	modname	HTML-Tagset
%define	modver	3.20

Summary:	This module contains data tables useful in dealing with HTML
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	22
License:	GPLv2
Group:		Development/Perl
Url:		http://metacpan.org/pod/HTML::Tagset
Source0:	http://www.cpan.org/modules/by-module/HTML/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test)
BuildRequires:	perl-devel

%description
This module contains data tables useful in dealing with HTML.
It provides no functions or methods.

%prep
%autosetup -p1 -n %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/HTML
%{_mandir}/man3/*
