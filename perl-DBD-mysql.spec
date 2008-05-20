%define	module DBD-mysql

Summary:	MySQL-Perl bindings
Name:		perl-%{module}
Version:	4.007
Release:	%mkrel 1
License:	GPL
Group:		Development/Databases
URL:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/DBD/%{module}-%{version}.tar.gz
BuildRequires:	perl-DBI
BuildRequires:	mysql-devel
BuildRequires:	perl-devel
BuildRequires:	zlib-devel
BuildRequires:	openssl-devel
Provides:	perl-Mysql
Obsoletes:	perl-Mysql
Buildroot:	%{_tmppath}/%{name}-%{version}

%description
DBD::mysql is an interface driver for connecting the DBMS independent Perl API
DBI to the MySQL DBMS. When you want to use MySQL from within perl, DBI and
DBD::mysql are your best choice: Unlike "mysqlperl", another option, this is
based on a common standard, so your sources will easily be portable to other
DBMS's.

%prep

%setup -q -n %{module}-%{version}

%build
%serverbuild

%{__perl} Makefile.PL INSTALLDIRS=vendor
#--testhost=127.0.0.1 --testport=22222

%make OPTIMIZE="$CFLAGS"

# make test requires a running mysql server
#make test

%clean 
rm -rf %{buildroot}

%install
rm -rf %{buildroot}

%makeinstall_std

%files
%defattr(-,root,root)
%doc README ChangeLog
%{perl_vendorarch}/*
%{_mandir}/*/*
