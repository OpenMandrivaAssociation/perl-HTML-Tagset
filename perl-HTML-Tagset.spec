%define	modname	HTML-Tagset

Summary:	This module contains data tables useful in dealing with HTML
Name:		perl-%{modname}
Version:	3.24
Release:	1
License:	GPLv2
Group:		Development/Perl
Url:		https://metacpan.org/pod/HTML::Tagset
Source0:	http://www.cpan.org/modules/by-module/HTML/%{modname}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test)
BuildRequires:	perl-devel
# FIXME why doesn't the dependency generator notice this?
Provides:	perl(HTML::Tagset) = %{version}

%description
This module contains data tables useful in dealing with HTML.
It provides no functions or methods.

%prep
%autosetup -p1 -n %{modname}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%make_install

%files
%doc Changes
%{perl_vendorlib}/HTML
%{_mandir}/man3/*
