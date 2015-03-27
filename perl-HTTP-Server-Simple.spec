%define modname	HTTP-Server-Simple
%define modver 0.50

Summary:	Perl module to write simple standalone http daemons
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/HTTP/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl(CGI) 
BuildRequires:	perl(URI::Escape)
Requires:	perl(CGI)

%description
This module is a simple standalone http dameon. It doesn't thread. It doesn't
fork. It does, however, act as a simple frontend which can turn a CGI into a
standalone web-based application.

%prep
%setup -qn %{modname}-%{modver}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc ex README Changes
%{perl_vendorlib}/HTTP
%{_mandir}/man3/*
