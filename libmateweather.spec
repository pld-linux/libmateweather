Summary:	Library to allow MATE Desktop to display weather information
Summary(pl.UTF-8):	Biblioteka umożliwiająca wyświetlanie informacji pogodowych w środowisku MATE Desktop
Name:		libmateweather
Version:	1.22.1
Release:	1
License:	GPL v2+
Group:		X11/Libraries
Source0:	http://pub.mate-desktop.org/releases/1.22/%{name}-%{version}.tar.xz
# Source0-md5:	614d7b06bcbc42e3a93f56abd589398d
URL:		http://wiki.mate-desktop.org/libmateweather
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.50.0
BuildRequires:	gtk+3-devel >= 3.22
BuildRequires:	gtk-doc >= 1.11
BuildRequires:	intltool >= 0.50.1
BuildRequires:	libsoup-devel >= 2.34.0
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	libxml2-devel >= 1:2.6.0
BuildRequires:	mate-common
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	tar >= 1:1.22
BuildRequires:	tzdata-zoneinfo >= 2016g
BuildRequires:	xz
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	gtk-update-icon-cache
Requires:	glib2 >= 1:2.50.0
Requires:	gsettings-desktop-schemas
Requires:	gtk+3 >= 3.22
Requires:	libsoup >= 2.34.0
Requires:	libxml2 >= 1:2.6.0
Requires:	mate-icon-theme
Requires:	tzdata-zoneinfo >= 2016g
Obsoletes:	python-mateweather
Conflicts:	mate-applet-gweather < 1.6.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libmateweather is a library to allow MATE Desktop to display weather
information. It's a fork of libgweather.

%description -l pl.UTF-8
libmateweather to biblioteka umożliwiająca wyświetlanie informacji
pogodowych w środowisku MATE Desktop. Jest odgałęzieniem libgweather.

%package devel
Summary:	Development files for libmateweather
Summary(pl.UTF-8):	Pliki programistyczne biblioteki libmateweather
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.50.0
Requires:	gtk+3-devel >= 3.22
Requires:	libsoup-devel >= 2.34.0
Requires:	libxml2-devel >= 1:2.6.0

%description devel
Development files for libmateweather.

%description devel -l pl.UTF-8
Pliki programistyczne biblioteki libmateweather.

%package apidocs
Summary:	libmateweather API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki libmateweather
Group:		Documentation
Requires:	gtk-doc-common
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
libmateweather API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libmateweather.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-html-dir=%{_gtkdocdir} \
	--with-zoneinfo-dir=%{_datadir}/zoneinfo \
	--disable-silent-rules \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libmateweather.la

%if %{with python}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean
%endif

# outdated copy of es
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/es_ES
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{frp,ie,jv,ku_IQ}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%update_icon_cache mate
%glib_compile_schemas

%postun
/sbin/ldconfig
%update_icon_cache mate
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libmateweather.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmateweather.so.1
%{_datadir}/libmateweather
%{_datadir}/glib-2.0/schemas/org.mate.weather.gschema.xml
%{_iconsdir}/mate/*x*/status/weather-*.png
%{_iconsdir}/mate/scalable/status/weather-*.svg

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmateweather.so
%{_includedir}/libmateweather
%{_pkgconfigdir}/mateweather.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libmateweather
