%define Werror_cflags %{nil}

%define upstream_name    DBD-mysql
%define upstream_version 4.043

Summary:	MySQL-Perl bindings
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3
License:	GPLv2+
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/DBD/%{upstream_name}-%{upstream_version}.tar.gz
Patch0:		DBD-mysql-4.043-Fix-use-after-free-after-calling-mysql_stmt_close.patch
Patch1:		DBD-mysql-4.043-Fix-build-failures-for-MariaDB-10.2.patch
Patch2:		DBD-mysql-4.043-Describe-all-SSL-related-attributes-in-POD.patch
Patch3:		DBD-mysql-4.043-Enforce-SSL-encryption.patch
Patch4:		DBD-mysql-4.043-Add-new-connection-attribute-mysql_ssl_optional.patch
Patch5:		DBD-mysql-4.043-Add-new-database-handle-attribute-mysql_ssl_cipher.patch
BuildRequires:	perl(DBI)
BuildRequires:	mysql-devel
BuildRequires:	perl-devel
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(zlib)
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

%make OPTIMIZE="$CFLAGS"

%install
%makeinstall_std

