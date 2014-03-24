%define	upstream_name    DBD-mysql
%define upstream_version 4.027
%define Werror_cflags %nil

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	MySQL-Perl bindings
License:	GPL
Group:		Development/Databases
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/DBD/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(DBI)
BuildRequires:	mysql-devel
BuildRequires:	openssl-devel
BuildRequires:	perl-devel
BuildRequires:	zlib-devel
Provides:	perl-Mysql
Obsoletes:	perl-Mysql

%description
DBD::mysql is an interface driver for connecting the DBMS independent Perl API
DBI to the MySQL DBMS. When you want to use MySQL from within perl, DBI and
DBD::mysql are your best choice: Unlike "mysqlperl", another option, this is
based on a common standard, so your sources will easily be portable to other
DBMS's.

%prep

%setup -q -n %{upstream_name}-%{upstream_version}

%build
%serverbuild

# it does not work with -fPIE and someone added that to the serverbuild macro...
CFLAGS=`echo $CFLAGS|sed -e 's|-fPIE||g'`
CXXFLAGS=`echo $CXXFLAGS|sed -e 's|-fPIE||g'`

%{__perl} Makefile.PL INSTALLDIRS=vendor
#--testhost=127.0.0.1 --testport=22222

%make OPTIMIZE="$CFLAGS"

# make test requires a running mysql server
#make test

%clean 

%install

%makeinstall_std

%files
%doc ChangeLog
%{perl_vendorarch}/*
%{_mandir}/*/*


%changelog
* Tue Jan 24 2012 Oden Eriksson <oeriksson@mandriva.com> 4.20.0-1mdv2012.0
+ Revision: 767782
- fix build
- 4.020
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Sun May 15 2011 Guillaume Rousse <guillomovitch@mandriva.org> 4.19.0-1
+ Revision: 674797
- update to new version 4.019

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 4.18.0-2
+ Revision: 667067
- mass rebuild

* Thu Mar 17 2011 Oden Eriksson <oeriksson@mandriva.com> 4.18.0-1
+ Revision: 645738
- 4.018
- relink against libmysqlclient.so.18

* Sat Jan 01 2011 Oden Eriksson <oeriksson@mandriva.com> 4.17.0-3mdv2011.0
+ Revision: 627002
- rebuilt against mysql-5.5.8 libs, again

* Mon Dec 27 2010 Oden Eriksson <oeriksson@mandriva.com> 4.17.0-2mdv2011.0
+ Revision: 625423
- rebuilt against mysql-5.5.8 libs

* Sun Aug 15 2010 Jérôme Quelin <jquelin@mandriva.org> 4.17.0-1mdv2011.0
+ Revision: 569934
- update to 4.017

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 4.16.0-4mdv2011.0
+ Revision: 564403
- rebuild for perl 5.12.1

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 4.16.0-3mdv2011.0
+ Revision: 555787
- rebuild for perl 5.12

  + Sandro Cazzaniga <kharec@mandriva.org>
    - rebuild

* Wed Jul 14 2010 Jérôme Quelin <jquelin@mandriva.org> 4.16.0-1mdv2011.0
+ Revision: 553080
- update to 4.016

* Sun Apr 18 2010 Jérôme Quelin <jquelin@mandriva.org> 4.14.0-4mdv2010.1
+ Revision: 536132
- update to 4.014

* Thu Apr 08 2010 Funda Wang <fwang@mandriva.org> 4.13.0-4mdv2010.1
+ Revision: 532895
- rebuild

* Fri Feb 26 2010 Oden Eriksson <oeriksson@mandriva.com> 4.13.0-3mdv2010.1
+ Revision: 511615
- rebuilt against openssl-0.9.8m

* Wed Feb 17 2010 Oden Eriksson <oeriksson@mandriva.com> 4.13.0-2mdv2010.1
+ Revision: 507034
- rebuild

* Fri Sep 18 2009 Jérôme Quelin <jquelin@mandriva.org> 4.13.0-1mdv2010.0
+ Revision: 444261
- update to 4.013

* Wed Jul 08 2009 Jérôme Quelin <jquelin@mandriva.org> 4.12.0-1mdv2010.0
+ Revision: 393660
- update to 4.012
- using %%perl_convert_version

* Mon Jun 08 2009 Guillaume Rousse <guillomovitch@mandriva.org> 4.011-1mdv2010.0
+ Revision: 383959
- update to new version 4.011
- new version
- disable format errors checking, due to strange results

* Sat Dec 06 2008 Oden Eriksson <oeriksson@mandriva.com> 4.008-2mdv2009.1
+ Revision: 311202
- rebuilt against mysql-5.1.30 libs

* Sun Aug 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 4.008-1mdv2009.0
+ Revision: 277947
- update to new version 4.008

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 4.007-2mdv2009.0
+ Revision: 265354
- rebuild early 2009.0 package (before pixel changes)

* Tue May 20 2008 Guillaume Rousse <guillomovitch@mandriva.org> 4.007-1mdv2009.0
+ Revision: 209324
- update to new version 4.007

* Wed Jan 23 2008 Thierry Vignaud <tv@mandriva.org> 4.006-2mdv2008.1
+ Revision: 157263
- rebuild with fixed %%serverbuild macro

* Thu Jan 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 4.006-1mdv2008.1
+ Revision: 153975
- update to new version 4.006

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 4.005-2mdv2008.1
+ Revision: 152054
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Thu Jul 19 2007 Oden Eriksson <oeriksson@mandriva.com> 4.005-1mdv2008.0
+ Revision: 53561
- 4.005

* Tue May 01 2007 Olivier Thauvin <nanardon@mandriva.org> 4.004-1mdv2008.0
+ Revision: 19857
- 4.004


* Tue Mar 06 2007 Oden Eriksson <oeriksson@mandriva.com> 4.003-1mdv2007.0
+ Revision: 133623
- 4.003

* Thu Jan 11 2007 Oden Eriksson <oeriksson@mandriva.com> 4.001-1mdv2007.1
+ Revision: 107382
- 4.001

* Thu Nov 02 2006 Oden Eriksson <oeriksson@mandriva.com> 3.0008-1mdv2007.1
+ Revision: 75669
- Import perl-DBD-mysql

* Thu Nov 02 2006 Oden Eriksson <oeriksson@mandriva.com> 3.0008-1mdv2007.1
- 3.0008 (fixes #26932)
- fix deps

* Tue Sep 05 2006 Oden Eriksson <oeriksson@mandriva.com> 3.0006-1mdv2007.0
- rebuilt against MySQL-5.0.24a-1mdv2007.0 due to ABI changes

* Thu Jun 22 2006 Guillaume Rousse <guillomovitch@mandriva.org> 3.0006-1mdv2007.0
- New version 3.0006

* Wed Jun 07 2006 Guillaume Rousse <guillomovitch@mandriva.org> 3.0004-1mdv2007.0
- New release 3.0004
- spec cleanup

* Wed Jan 04 2006 Emmanuel Blindauer <blindauer@mandriva.org> 3.0002-4mdk
- rebuild against openssl-0.9.8a, sync with ppc

* Sun Nov 13 2005 Oden Eriksson <oeriksson@mandriva.com> 3.0002-3mdk
- rebuilt against openssl-0.9.8a

* Sun Oct 30 2005 Oden Eriksson <oeriksson@mandriva.com> 3.0002-2mdk
- rebuilt against MySQL-5.0.15

* Sat Jul 16 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 3.0002-1mdk
- 3.0002

* Sat Jul 02 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 3.0000-1mdk
- 3.0000

* Thu Jun 09 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 2.9008-1mdk
- 2.9008
- Change innacurate summary

* Fri Apr 29 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 2.9007-1mdk
- 2.9007

* Wed Jan 26 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 2.9004-6mdk
- Add perl-DBI in the BuildRequires (Marc Koschewski)

* Mon Jan 24 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 2.9004-5mdk
- rebuild

* Sat Jan 22 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 2.9004-4mdk
- rebuilt against MySQL-4.1.x system libs

* Fri Jan 21 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 2.9004-3mdk
- Fix URL and source
- Replaces perl-Mysql

* Mon Nov 15 2004 Michael Scherer <misc@mandrake.org> 2.9004-2mdk
- Rebuild for new perl

* Sun Jul 18 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 2.9004-1mdk
- 2.9004

* Thu Jun 03 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 2.9003-1mdk
- 2.9003
- drop distribution tag
- cosmetics



