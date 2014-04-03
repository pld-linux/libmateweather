Summary:	Library to allow MATE Desktop to display weather information
Summary(pl.UTF-8):	Biblioteka umożliwiająca wyświetlanie informacji pogodowych w środowisku MATE Desktop
Name:		libmateweather
Version:	1.8.0
Release:	2
License:	GPL v2+
Group:		X11/Libraries
Source0:	http://pub.mate-desktop.org/releases/1.8/%{name}-%{version}.tar.xz
# Source0-md5:	f11f7f3c6ae72e58b54931cb09bb76a7
URL:		http://wiki.mate-desktop.org/libmateweather
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.26.0
BuildRequires:	gtk+2-devel >= 2:2.11.0
BuildRequires:	gtk-doc >= 1.9
BuildRequires:	intltool >= 0.40.3
BuildRequires:	libsoup-devel >= 2.34.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.0
BuildRequires:	mate-common
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	python-devel >= 2
BuildRequires:	python-pygobject-devel >= 2.0
BuildRequires:	python-pygtk-devel >= 2:2.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	/sbin/ldconfig
Requires:	glib2 >= 1:2.26.0
Requires:	gsettings-desktop-schemas
Requires:	gtk+2 >= 2:2.11.0
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Requires:	libxml2 >= 1:2.6.0
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
Requires:	glib2-devel >= 1:2.26.0
Requires:	gtk+2-devel >= 2:2.11.0
Requires:	libsoup-devel >= 2.4.0
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

%package -n python-mateweather
Summary:	Python binding for libmateweather library
Summary(pl.UTF-8):	Wiązanie Pythona do biblioteki libmateweather
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python-pygobject >= 2.0
Requires:	python-pygtk-gtk >= 2:2.0

%description -n python-mateweather
Python binding for libmateweather library.

%description -n python-mateweather -l pl.UTF-8
Wiązanie Pythona do biblioteki libmateweather.

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
	--enable-python \
	--disable-silent-rules \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libmateweather.la
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/mateweather/*/mateweather.la
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/cmn

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

# outdated copy of es
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

%files -n python-mateweather
%defattr(644,root,root,755)
%dir %{py_sitedir}/mateweather
%{py_sitedir}/mateweather/*.py[co]
%dir %{py_sitedir}/mateweather/I_KNOW_THIS_IS_UNSTABLE
%{py_sitedir}/mateweather/I_KNOW_THIS_IS_UNSTABLE/*.py[co]
%attr(755,root,root) %{py_sitedir}/mateweather/I_KNOW_THIS_IS_UNSTABLE/mateweather.so
