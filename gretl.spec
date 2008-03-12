Summary:	Econometric analysis
Summary(pl.UTF-8):	Analiza ekonometryczna
Name:		gretl
Version:	1.2.4
Release:	12
License:	GPL
Group:		Applications/Math
Source0:	http://dl.sourceforge.net/gretl/%{name}-%{version}.tar.bz2
# Source0-md5:	31dcf07b52f88cab71f8aa11aec992c0
# files missing from 1.2.4 distribution (taken from CVS)
Source1:	%{name}-doc-commands.tar.bz2
# Source1-md5:	45716104288ad81061697757e6acd1de
Patch0:		%{name}-use_terminfo_not_termcap.patch
Patch1:		%{name}-DESTDIR.patch
Patch2:		%{name}-desktop.patch
Patch3:		%{name}-checks.patch
Patch4:		%{name}-dirs.patch
Patch5:		%{name}-configure_in.patch
Patch6:		%{name}-buffer_overflow.patch
Patch7:		%{name}-libxslt-1.1.15.patch
URL:		http://gretl.sourceforge.net/
BuildRequires:	autoconf >= 2.12
BuildRequires:	automake
BuildRequires:	gcc-g77
BuildRequires:	gettext-devel
BuildRequires:	gmp-devel >= 4.0.1
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	gtksourceview-devel
BuildRequires:	lapack-devel
BuildRequires:	libgnomeprintui-devel >= 2.2
BuildRequires:	libgnomeui-devel >= 2.0
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.5.0
BuildRequires:	libxslt-devel >= 1.0.30
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
BuildRequires:	zlib-devel
Requires(post):	/usr/bin/scrollkeeper-update
Requires(post):	GConf2
Requires:	%{name}-lib = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
It is a software package for econometric analysis, written in the C
programming language. Comprises a shared library, a command-line
client program, and a graphical client built using GTK+. Gretl calls
gnuplot to generate graphs. Contains sample data files, like those
from W. Greene.

%description -l pl.UTF-8
To jest pakiet do analizy ekonometrycznej. Zawiera bibliotekę,
narzędzie działające z linii poleceń i graficznego klienta opartego na
GTK+. Gretl używa gnuplota do generowania wykresów. Zawiera też 
przykładowe pliki z danymi, min. dane z książki W. Greena.

%package lib
Summary:	Gretl Libraries
Summary(pl.UTF-8):	Biblioteki Gretl
Group:		Libraries

%description lib
Libraries for Gretl. See gretl package description.

%description lib -l pl.UTF-8
Biblioteki Gretl.

%package devel
Summary:	Gretl header files
Summary(pl.UTF-8):	Pliki nagłówkowe Gretl
Group:		Development/Libraries
Requires:	%{name}-lib = %{version}-%{release}

%description devel
Package contains header files for building gretl-based software. See
gretl package description.

%description devel -l pl.UTF-8
Pliki nagłówkowe potrzebne do budowania programów bazujących na gretl.

%prep
%setup -q -a1
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
# these seds belong with patch7
sed 's/$hlp/cli/' doc/commands/gretltxt.xsl>doc/commands/gretltxt_cli.xsl
sed 's/$hlp/gui/' doc/commands/gretltxt.xsl>doc/commands/gretltxt_gui.xsl

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I macros
%{__autoconf}
%{__autoheader}
%configure \
	GNUPLOT=/usr/bin/gnuplot \
	GNUPLOT_PNG=yes \
	LATEX=/usr/bin/latex
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# gretl-config is not installed with gtk+2 builds
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/gretl-config.1*

# plugins are dlopened by *.so
rm -f $RPM_BUILD_ROOT%{_libdir}/gretl-gtk2/*.la

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/bin/scrollkeeper-update
%gconf_schema_install

%postun	-p /usr/bin/scrollkeeper-update

%post	lib -p /sbin/ldconfig
%postun	lib -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog EXTENDING NEWS README TODO doc/{figures,manual.html}
%attr(755,root,root) %{_bindir}/gretl
%attr(755,root,root) %{_bindir}/gretlcli
%attr(755,root,root) %{_bindir}/gretl_x11
%dir %{_libdir}/gretl-gtk2
%attr(755,root,root) %{_libdir}/gretl-gtk2/*.so
%{_datadir}/gretl
%{_datadir}/gtksourceview-*/language-specs/*.lang
%{_datadir}/mime-info/gretl.*
%{_omf_dest_dir}/gretl
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
%{_pixmapsdir}/*.xpm
%{_sysconfdir}/gconf/schemas/*.schemas
%{_mandir}/man1/gretl.1*

%files lib
%defattr(644,root,root,755)
%{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/gretl
%{_pkgconfigdir}/*.pc
