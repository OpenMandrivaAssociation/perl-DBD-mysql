%define _empty_manifest_terminate_build 0
%define Werror_cflags %{nil}

%define upstream_name    DBD-mysql
%define upstream_version 4.050

%ifarch %{x86_64}
# FIXME workaround for debuginfo gen bug
%global debug_package %{nil}
%endif

Summary:	MySQL-Perl bindings
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	9
License:	GPLv2+
Group:		Development/Perl
Url:		https://metacpan.org/release/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/DBD/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:	make
BuildRequires:	perl(DBI)
BuildRequires:	mysql-devel
BuildRequires:	perl-devel
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	perl(Devel::CheckLib)
Provides:	perl-Mysql = %{EVRD}

%description
DBD::mysql is an interface driver for connecting the DBMS independent Perl API
DBI to the MySQL DBMS. When you want to use MySQL from within perl, DBI and
DBD::mysql are your best choice: Unlike "mysqlperl", another option, this is
based on a common standard, so your sources will easily be portable to other
DBMS's.

%files
%{perl_vendorarch}/*
%{_mandir}/*/*

#----------------------------------------------------------------------------

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%autopatch -p1

%build
%serverbuild

# it does not work with -fPIE and someone added that to the serverbuild macro...
CFLAGS=`echo $CFLAGS|sed -e 's|-fPIE||g'`
CXXFLAGS=`echo $CXXFLAGS|sed -e 's|-fPIE||g'`

perl Makefile.PL INSTALLDIRS=vendor
#--testhost=127.0.0.1 --testport=22222

%make_build OPTIMIZE="$CFLAGS"

%install
%make_install

