Summary:	Econometric analysis
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
Requires:	%{name}-lib

%define		_includedir	/usr/include/gretl

%description
Is a software package for econometric analysis, written in the C
programming language. Comprises a shared library, a command-line
client program, and a graphical client built using GTK+. Gretl calls
gnuplot to generate graphs.

%package -n gretl-lib
Summary:	Gretl Libraries
License:	GPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	Библиотеки
Group(uk):	Б╕бл╕отеки

%description -n gretl-lib
Libraries for Gretl. See gretl package description.

%package -n gretl-devel
Summary:	Gretl header files
License:	GPL
Group:		Development
Group(de):	Entwicklung
Group(es):	Desarrollo
Group(pl):	Programowanie
Group(pt_BR):	Desenvolvimento
Group(ru):	Разработка
Group(uk):	Розробка

%description -n gretl-devel
Package contains header files for building gretl-based software. See
gretl package description.

# I will add this package later ;-)
#%package -n gretl-sampe_data
#Summary:	Gretl sample data
#License:	GPL
#Group:		Applications/Math
#Group(de):	Applikationen/Mathematik
#Group(pl):	Aplikacje/Matematyczne
#
#%description -n gretl-sample_data
#Contains sample data for experiments with gretl econometric software.
#Contains also data set from William Greene book(!).			

%prep
%setup -q

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
gzip -9nf README ChangeLog EXTENDING 

%post -n gretl-lib
/sbin/ldconfig

%postun -n gretl-lib
/sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%doc doc/gretl-logo.png 
%doc doc/*.pdf
%doc doc/*.tex
%doc doc/*.sty

%attr(755,root,root) %{_bindir}/*
%{_datadir}/gretl/*
%{_mandir}/*/*

%files -n gretl-lib
%defattr(644,root,root,755)
%{_libdir}/*

%files -n gretl-devel
%defattr(644,root,root,755)
%{_includedir}/*
