%define module  HTTP-Server-Simple
%define name	perl-%{module}
%define version 0.37
%define rel 1

Name: 		%{name}
Version: 	%{version}
Release:	%mkrel %{rel} 
License:	GPL or Artistic
Group:		Development/Perl
Summary:	Perl module to write simple standalone http daemons
URL:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/HTTP/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(CGI) perl(URI::Escape)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This module is a simple standalone http dameon. It doesn't thread. It doesn't
fork. It does, however, act as a simple frontend which can turn a CGI into a
standalone web-based application.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ex README Changes
%{perl_vendorlib}/HTTP
%{_mandir}/man3/*

