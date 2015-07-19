%define	upstream_name    DBD-mysql
%define upstream_version 4.029
%define Werror_cflags %nil

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

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

perl Makefile.PL INSTALLDIRS=vendor
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
