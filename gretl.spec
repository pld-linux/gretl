Summary:	Econometric analysis
Summary(pl):	Analiza ekonometryczna
Name:		gretl
Version:	0.96
Release:	2
License:	GPL
Group:		Applications/Math
Source0:	ftp://ricardo.ecn.wfu.edu/pub/gretl/%{name}-%{version}.tar.gz
# Source0-md5:	61db4e49fc3a78f97987f2b31dbc6863
Source1:	%{name}.desktop
Source2:	%{name}.xpm
Patch0:		%{name}-override_readline_tests.patch
Patch1:		%{name}-use_terminfo_not_termcap.patch
Patch2:		%{name}-move_x11_binary.patch
Patch3:		%{name}-DESTDIR.patch
Patch4:		%{name}-DESTDIR2.patch
URL:		http://gretl.sourceforge.net/
BuildRequires:	automake
BuildRequires:	gtk+-devel >= 1.2.3
BuildRequires:	readline-devel
BuildRequires:	zlib-devel
Requires:	%{name}-lib = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_includedir	/usr/include/gretl

%description
It is a software package for econometric analysis, written in the C
programming language. Comprises a shared library, a command-line
client program, and a graphical client built using GTK+. Gretl calls
gnuplot to generate graphs. Contains sample data files, like those
from W. Greene.

%description -l pl
To jest pakiet do analizy ekonometrycznej. Zawiera bibliotekê,
narzêdzie dzia³aj±ce z linii poleceñ i graficznego klienta opartego na
GTK+. Gretl u¿ywa gnuplota do generowania wykresów. Zawiera te¿ przy-
k³adowe pliki z danymi, min. dane z ksi±¿ki W. Green'a

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
Summary(pl):	Pliki nag³ówkowe Gretl
Group:		Development/Libraries
Requires:	%{name}-lib = %{version}-%{release}

%description devel
Package contains header files for building gretl-based software. See
gretl package description.

%description devel -l pl
Pliki nag³ówkowe potrzebne do budowania programów bazuj±cych na gretl.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
cp -f /usr/share/automake/config.* tools
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/gretl/db,%{_desktopdir},%{_pixmapsdir}}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.xpm

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	lib -p /sbin/ldconfig
%postun	lib -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README ChangeLog EXTENDING doc/{gretl-logo.png,*.{pdf,tex,sty}}
%attr(755,root,root) %{_bindir}/gretl
%attr(755,root,root) %{_bindir}/gretlcli
%attr(755,root,root) %{_bindir}/gretl_x11
%{_datadir}/gretl
%{_mandir}/*/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*

%files lib
%defattr(644,root,root,755)
%{_libdir}/*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gretl-config
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}
