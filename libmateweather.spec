Summary:	Library to allow MATE Desktop to display weather information
Summary(pl.UTF-8):	Biblioteka umożliwiająca wyświetlanie informacji pogodowych w środowisku MATE Desktop
Name:		libmateweather
Version:	1.26.3
Release:	1
License:	GPL v2+
Group:		X11/Libraries
Source0:	https://pub.mate-desktop.org/releases/1.26/%{name}-%{version}.tar.xz
# Source0-md5:	891a0161b24f046a75125683a56551b5
URL:		https://wiki.mate-desktop.org/mate-desktop/libraries/libmateweather/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	glib2-devel >= 1:2.56.0
BuildRequires:	gtk+3-devel >= 3.22
BuildRequires:	gtk-doc >= 1.11
BuildRequires:	libsoup-devel >= 2.54.0
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	libxml2-devel >= 1:2.6.0
BuildRequires:	mate-common
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	tar >= 1:1.22
BuildRequires:	tzdata-zoneinfo >= 2016g
BuildRequires:	xz
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	gtk-update-icon-cache
Requires:	glib2 >= 1:2.56.0
Requires:	gsettings-desktop-schemas
Requires:	gtk+3 >= 3.22
Requires:	hicolor-icon-theme
Requires:	libsoup >= 2.54.0
Requires:	libxml2 >= 1:2.6.0
Requires:	tzdata-zoneinfo >= 2016g
Obsoletes:	python-mateweather < 1.18.0
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
Requires:	glib2-devel >= 1:2.56.0
Requires:	gtk+3-devel >= 3.22
Requires:	libsoup-devel >= 2.54.0
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
BuildArch:	noarch

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

# outdated copy of es
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/es_ES
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{frp,ie,jv,ku_IQ}

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
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libmateweather.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmateweather.so.1
%{_datadir}/libmateweather
%{_datadir}/glib-2.0/schemas/org.mate.weather.gschema.xml
%{_iconsdir}/hicolor/*x*/status/weather-*.png
%{_iconsdir}/hicolor/scalable/status/weather-*.svg

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmateweather.so
%{_includedir}/libmateweather
%{_pkgconfigdir}/mateweather.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libmateweather
