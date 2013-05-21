%define upstream_name    HTTP-Server-Simple
%define upstream_version 0.44

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Perl module to write simple standalone http daemons
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/HTTP/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(CGI) 
BuildRequires:	perl(URI::Escape)
Requires:	perl(CGI)
BuildArch:	noarch

%description
This module is a simple standalone http dameon. It doesn't thread. It doesn't
fork. It does, however, act as a simple frontend which can turn a CGI into a
standalone web-based application.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc ex README Changes
%{perl_vendorlib}/HTTP
%{_mandir}/man3/*


%changelog
* Mon May 30 2011 Funda Wang <fwang@mandriva.org> 0.440.0-3mdv2011.0
+ Revision: 681751
- add req
- rebuild

* Tue Apr 05 2011 Sandro Cazzaniga <kharec@mandriva.org> 0.440.0-1
+ Revision: 650619
- new version 0.44

* Tue Jul 13 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.430.0-1mdv2011.0
+ Revision: 552320
- update to 0.43

* Fri Feb 19 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.420.0-1mdv2010.1
+ Revision: 508050
- update to 0.42

* Wed Sep 30 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.410.0-1mdv2010.0
+ Revision: 451155
- update to 0.41

* Wed Aug 19 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.400.0-1mdv2010.0
+ Revision: 418129
- update to 0.40

* Sat Aug 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.380.0-1mdv2010.0
+ Revision: 406063
- rebuild using %%perl_convert_version

* Mon Jan 12 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.38-1mdv2009.1
+ Revision: 328529
- update to new version 0.38

* Sun Jan 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.37-1mdv2009.1
+ Revision: 324504
- update to new version 0.37

* Tue Nov 25 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.36-1mdv2009.1
+ Revision: 306763
- update to new version 0.36

* Sat Oct 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.35-1mdv2009.1
+ Revision: 292167
- update to new version 0.35

* Thu Jun 12 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.34-1mdv2009.0
+ Revision: 218341
- update to new version 0.34
- update to new version 0.33

* Tue Apr 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.31-1mdv2009.0
+ Revision: 193847
- update to new version 0.31

* Sat Feb 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.29-1mdv2008.1
+ Revision: 169259
- update to new version 0.29

* Thu Jan 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.28-1mdv2008.1
+ Revision: 153979
- update to new version 0.28

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue May 01 2007 Michael Scherer <misc@mandriva.org> 0.27-1mdv2008.0
+ Revision: 19960
- fix missing BuildRequires
- update to 0.27


* Fri Jun 16 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.20-1mdv2007.0
- New version 0.20
- cleanup

* Fri Mar 03 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.18-1mdk
- 0.18

* Wed Feb 01 2006 Michael Scherer <misc@mandriva.org> 0.17-1mdk
- New release 0.17

* Wed Dec 28 2005 Michael Scherer <misc@mandriva.org> 0.16-2mdk
- Do not ship empty dir

* Tue Nov 08 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.16-1mdk
- 0.16

* Mon Oct 10 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.15-2mdk
- Fix BuildRequires

* Sat Oct 08 2005 Michael Scherer <misc@mandriva.org> 0.15-1mdk
- New release 0.15

* Sat Oct 01 2005 Michael Scherer <misc@mandriva.org> 0.13-1mdk
- First mandriva package

