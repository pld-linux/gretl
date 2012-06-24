Summary:	Econometric analysis
Summary(pl):	Analiza ekonometryczna
Name:		gretl
Version:	0.96
Release:	1
License:	GPL
Group:		Applications/Math
Group(de):	Applikationen/Mathematik
Group(pl):	Aplikacje/Matematyczne
Source0:	ftp://ricardo.ecn.wfu.edu/pub/gretl/%{name}-%{version}.tar.gz
URL:		http://gretl.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	%{name}-lib = %{version}

%define		_includedir	/usr/include/gretl

%description
It is a software package for econometric analysis, written in the C
programming language. Comprises a shared library, a command-line
client program, and a graphical client built using GTK+. Gretl calls
gnuplot to generate graphs.

%description -l pl
To jest pakiet do analizy ekonometrycznej. Zawiera bibliotek�,
narz�dzie dzia�aj�ce z linii polece� i graficznego klienta opartego na
GTK+. Gretl u�ywa gnuplota do generowania wykres�w.

%package lib
Summary:	Gretl Libraries
Summary(pl):	Biblioteki Gretl
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	����������
Group(uk):	��̦�����

%description lib
Libraries for Gretl. See gretl package description.

%description lib -l pl
Biblioteki Gretl.

%package devel
Summary:	Gretl header files
Summary(pl):	Pliki nag��wkowe Gretl
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	����������/����������
Group(uk):	��������/��̦�����
Requires:	%{name}-lib = %{version}

%description devel
Package contains header files for building gretl-based software. See
gretl package description.

%description devel -l pl
Pliki nag��wkowe potrzebne do budowania program�w bazuj�cych na gretl.

# I will add this package later ;-)
#%package sample_data
#Summary:	Gretl sample data
#Summary(pl):	Przyk�adowe dane do Gretl
#Group:		Applications/Math
#Group(de):	Applikationen/Mathematik
#Group(pl):	Aplikacje/Matematyczne
#
#%description sample_data
#Contains sample data for experiments with gretl econometric software.
#Contains also data set from William Greene book(!).			

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
gzip -9nf README ChangeLog EXTENDING 

%clean
rm -rf $RPM_BUILD_ROOT

%post	lib -p /sbin/ldconfig
%postun	lib -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.gz
%doc doc/gretl-logo.png 
%doc doc/*.pdf
%doc doc/*.tex
%doc doc/*.sty

%attr(755,root,root) %{_bindir}/*
%{_datadir}/gretl
%{_mandir}/*/*

%files lib
%defattr(644,root,root,755)
%{_libdir}/*

%files devel
%defattr(644,root,root,755)
%{_includedir}
