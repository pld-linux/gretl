Summary:	Econometric analysis
Name:		gretl
Version:	0.96
Release:	1
License:	GPL
Group:		Applications/Math
Group(de):	Applikationen/Mathematik
Group(pl):	Aplikacje/Matematyczne
Source0:	ftp://ricardo.ecn.wfu.edu/pub/gretl/%{name}-%{version}.tar.gz
Source1:	gretl-scripts.tar.gz
URL:		http://gretl.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root
Requires:	%{name}-lib=%{version}

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

%description -n gretl-lib
Libraries for Gretl. See gretl package description.


%package -n gretl-devel
Summary:	Gretl header files
License:	GPL
Group:		Development
Group(de):	Entwicklung
Group(es):	Desarrollo
Group(pl):	Programowanie

%description -n gretl-devel
Package contains header files for building gretl-based software. 
See gretl package description.

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
rm -rf $RPM_BUILD_ROOT

%setup -a 1 -q
# Have to move them because ./configure would replace them
# FIX This lameriade by writing proper %install section
# instead of make install
mkdir -p gretl-scripts
mv gretl gretl-config gretl-scripts

%build
./configure --prefix=${RPM_BUILD_ROOT}/usr \
    --exec-prefix=${RPM_BUILD_ROOT}/usr \
    --mandir="/usr/man" --disable-gtktest \
    --disable-gtkextratest --with-readline=yes
#make

%install
rm -rf $RPM_BUILD_ROOT
make install
# Configure script seems to have bug, and makes
# no use of --mandir= 
mkdir -p $RPM_BUILD_ROOT/usr/man/man1
mv $RPM_BUILD_ROOT/usr/share/man/man1/* $RPM_BUILD_ROOT/usr/man/man1/

# make install seems to forget about those
# manuals:
mkdir -p $RPM_BUILD_ROOT/usr/share/doc/
cp doc/*.pdf $RPM_BUILD_ROOT/usr/share/doc/
cp doc/*.tex $RPM_BUILD_ROOT/usr/share/doc/
cp doc/*.sty $RPM_BUILD_ROOT/usr/share/doc/
rm -f $RPM_BUILD_ROOT/usr/bin/gretl
rm -f $RPM_BUILD_ROOT/usr/bin/gretl-config

# This is nasty and lame solution.
# FIX make install scripts to do this better way
# SOURCE1 contains gretl and gretl-config scripts
# with correct paths to execs.
cp gretl-scripts/* $RPM_BUILD_ROOT/usr/bin/


%post -n gretl-lib
/sbin/ldconfig

%postun -n gretl-lib
/sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README COPYING ChangeLog INSTALL EXTENDING 
%doc doc/gretl-logo.png
%attr(755,root,root) /usr/bin/*
/usr/share/gretl/*
/usr/man/*

%files -n gretl-lib
%defattr(755,root,root,755)
/usr/lib/*

%files -n gretl-devel
%defattr(644,root,root,755)
/usr/include/gretl/*
