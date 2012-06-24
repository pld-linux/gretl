Summary:	Econometric analysis
Summary(pl):	Analiza ekonometryczna
Name:		gretl
Version:	0.96
Release:	1
License:	GPL
Group:		Applications/Math
Source0:	ftp://ricardo.ecn.wfu.edu/pub/gretl/%{name}-%{version}.tar.gz
Patch0:		%{name}-override_readline_tests.patch
Patch1:		%{name}-use_terminfo_not_termcap.patch
Patch2:		%{name}-move_x11_binary.patch
Patch3:		%{name}-DESTDIR.patch
Patch4:		%{name}-DESTDIR2.patch
URL:		http://gretl.sourceforge.net/
BuildRequires:	gtk+-devel >= 1.2.3
BuildRequires:	readline-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	%{name}-lib = %{version}

%define		_includedir	/usr/include/gretl

%description
It is a software package for econometric analysis, written in the C
programming language. Comprises a shared library, a command-line
client program, and a graphical client built using GTK+. Gretl calls
gnuplot to generate graphs. Contains sample data files, like those
from W. Greene.

%description -l pl
To jest pakiet do analizy ekonometrycznej. Zawiera bibliotek�,
narz�dzie dzia�aj�ce z linii polece� i graficznego klienta opartego na
GTK+. Gretl u�ywa gnuplota do generowania wykres�w. Zawiera te� przy-
k�adowe pliki z danymi, min. dane z ksi��ki W. Green'a

%package lib
Summary:	Gretl Libraries
Summary(pl):	Biblioteki Gretl
Group:		Libraries

%description lib
Libraries for Gretl. See gretl package description.

%description lib -l pl
Biblioteki Gretl.

%package devel
Summary:	Gretl header files
Summary(pl):	Pliki nag��wkowe Gretl
Group:		Development/Libraries
Requires:	%{name}-lib = %{version}

%description devel
Package contains header files for building gretl-based software. See
gretl package description.

%description devel -l pl
Pliki nag��wkowe potrzebne do budowania program�w bazuj�cych na gretl.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/gretl/db,%{_prefix}/X11R6/bin}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_bindir}/gretl_x11 $RPM_BUILD_ROOT%{_prefix}/X11R6/bin/

gzip -9nf README ChangeLog EXTENDING 

%clean
rm -rf $RPM_BUILD_ROOT

%post	lib -p /sbin/ldconfig
%postun	lib -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.gz doc/{gretl-logo.png,*.{pdf,tex,sty}}
%attr(755,root,root) %{_bindir}/gretl
%attr(755,root,root) %{_bindir}/gretlcli
%attr(755,root,root) %{_prefix}/X11R6/bin/gretl_x11
%{_datadir}/gretl
%{_mandir}/*/*

%files lib
%defattr(644,root,root,755)
%{_libdir}/*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gretl-config
%attr(755,root,root) %{_libdir}/*.so
%attr(755,root,root) %{_libdir}/*.la
%{_includedir}
