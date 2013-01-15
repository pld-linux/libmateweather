Summary:	Libraries to allow MATE Desktop to display weather information
Name:		libmateweather
Version:	1.5.0
Release:	1
License:	GPL v2+
Group:		X11/Libraries
Source0:	http://pub.mate-desktop.org/releases/1.5/%{name}-%{version}.tar.xz
# Source0-md5:	f4b3e63cd2865c33d1e9cc319c30210f
URL:		http://wiki.mate-desktop.org/libmateweather
BuildRequires:	gsettings-desktop-schemas-devel
BuildRequires:	gtk+2-devel >= 2:2.11.0
BuildRequires:	intltool >= 0.40.3
BuildRequires:	libsoup-devel >= 2.4.0
BuildRequires:	mate-common
# XXX what's pld package?
#BuildRequires:	python-gudev
BuildRequires:	python-pygobject-devel
BuildRequires:	python-pygtk-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	glib2 >= 1:2.26.0
Requires:	gsettings-desktop-schemas
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libraries to allow MATE Desktop to display weather information

%package devel
Summary:	Development files for libmateweather
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development files for libmateweather

%package apidocs
Summary:	libmateweather API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki libmateweather
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libmateweather API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libmateweather.

%prep
%setup -q

%build
NOCONFIGURE=1 ./autogen.sh
%configure \
	--with-html-dir=%{_gtkdocdir} \
	--enable-python \
	--disable-static

%{__make} \
	V=1

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libmateweather.la
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/mateweather/*/mateweather.la

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/es_ES
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%update_icon_cache hicolor
%glib_compile_schemas

%postun
/sbin/ldconfig
%update_icon_cache hicolor
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING README
%{_datadir}/libmateweather
%{_iconsdir}/mate/*/status/*
%{_datadir}/glib-2.0/schemas/org.mate.weather.gschema.xml
%attr(755,root,root) %{_libdir}/libmateweather.so.*.*.*
%ghost %{_libdir}/libmateweather.so.1

# python
%dir %{py_sitedir}/mateweather
%{py_sitedir}/mateweather/*.py[co]
%dir %{py_sitedir}/mateweather/I_KNOW_THIS_IS_UNSTABLE/
%{py_sitedir}/mateweather/*/*.py[co]
%attr(755,root,root) %{py_sitedir}/mateweather/*/mateweather.so

%files devel
%defattr(644,root,root,755)
%{_libdir}/libmateweather.so
%{_includedir}/libmateweather
%{_pkgconfigdir}/mateweather.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libmateweather
