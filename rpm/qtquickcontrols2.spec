#
# spec file for package libqt5-qtquickcontrols2
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define qt5_snapshot 1

Name:           libqt5-qtquickcontrols2
Version:        5.6.2
Release:        0
Summary:        Qt 5 Quick Controls Addon
License:        SUSE-LGPL-2.1-with-digia-exception-1.1 or GPL-3.0
Group:          Development/Libraries/X11
Url:            http://qt.digia.com
%define base_name libqt5
%define real_version 5.6.2
%define so_version 5.6.2
%define tar_version qtquickcontrols2-opensource-src-%{real_version}
Source:         %{tar_version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  libQt5Core-private-headers-devel >= %{version}
BuildRequires:  libQt5Gui-private-headers-devel >= %{version}
BuildRequires:  libqt5-qtbase-devel >= %{version}
BuildRequires:  libqt5-qtdeclarative-private-headers-devel >= %{version}
BuildRequires:  pkgconfig(Qt5Qml) >= %{version}
BuildRequires:  pkgconfig(Qt5Quick) >= %{version}
%if %qt5_snapshot
#to create the forwarding headers
BuildRequires:  perl
%endif
BuildRequires:  xz
%requires_ge libQt5Widgets5
%requires_ge libQtQuick5
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The Qt Quick Controls2 module provides a set of controls that
can be used to build complete interfaces in Qt Quick.

%package -n libQt5QuickControls2-5
Summary:        Qt 5 QuickControl2 Library
Group:          Development/Libraries/X11

%description -n libQt5QuickControls2-5
Qt is a set of libraries for developing applications.

This package contains base tools, like string, xml, and network
handling.

%package -n libQt5QuickTemplates2-5
Summary:        Qt5 QuickTemplates2 Library
Group:          Development/Libraries/X11

%description -n libQt5QuickTemplates2-5
You need this package, if you want to compile programs with qtwebkit.

%package -n libQt5QuickControls2-devel
Summary:        Qt Development Kit
Group:          Development/Libraries/X11
Requires:       libQt5QuickControls2-5 = %{version}

%description -n libQt5QuickControls2-devel
You need this package, if you want to compile programs with qtwebkit.

%package -n libQt5QuickTemplates2-devel
Summary:        Qt Development Kit
Group:          Development/Libraries/X11
Requires:       libQt5QuickTemplates2-5 = %version

%description -n libQt5QuickTemplates2-devel
You need this package, if you want to compile programs with qtwebkit.

%package examples
Summary:        Qt5 quickcontrols2 examples
Group:          Development/Libraries/X11

%description examples
Examples for libqt5-qtquickcontrols2 module.

%prep
%setup -q -n qtquickcontrols2-opensource-src-%{real_version}

%build
%if %qt5_snapshot
#force the configure script to generate the forwarding headers (it checks whether .git directory exists)
mkdir .git
%endif
%qmake5
%make_jobs

%install
%qmake5_install
find %{buildroot}/%{_libqt5_libdir} -type f -name '*la' -print -exec perl -pi -e 's,-L%{_builddir}/\S+,,g' {} \;
find %{buildroot}/%{_libqt5_libdir} -type f -name '*pc' -print -exec perl -pi -e "s, -L$RPM_BUILD_DIR/?\S+,,g" {} \; -exec sed -i -e "s,^moc_location=.*,moc_location=%{_lib}qt5_bindir/moc," -e "s,uic_location=.*,uic_location=%{_lib}qt5_bindir/uic," {} \;
find %{buildroot}/%{_libqt5_libdir} -type f -name '*prl' -exec sed -i -e "/^QMAKE_PRL_BUILD_DIR/d" {} \;

# kill .la files
rm -f %{buildroot}%{_libqt5_libdir}/lib*.la

%post -n libQt5QuickControls2-5 -p /sbin/ldconfig

%postun -n libQt5QuickControls2-5 -p /sbin/ldconfig

%post -n libQt5QuickTemplates2-5 -p /sbin/ldconfig

%postun -n libQt5QuickTemplates2-5 -p /sbin/ldconfig

%files -n libQt5QuickControls2-5
%defattr(-,root,root,755)
%doc LICENSE.*
%{_libqt5_libdir}/libQt5QuickControls2.so.*

%files -n libQt5QuickTemplates2-5
%defattr(-,root,root,755)
%doc LICENSE.*
%{_libqt5_libdir}/libQt5QuickTemplates2.so.*

%files
%defattr(-,root,root,755)
%doc LICENSE.*
%{_libqt5_archdatadir}/qml/QtQuick
%{_libqt5_archdatadir}/qml/Qt

%files -n libQt5QuickControls2-devel
%defattr(-,root,root,755)
%doc LICENSE.*
%exclude %{_libqt5_includedir}/QtQuickControls2/%{so_version}
%{_libqt5_includedir}/QtQuickControls2
%{_libqt5_libdir}/cmake/Qt5QuickControls2
%{_libqt5_libdir}/libQt5QuickControls2.prl
%{_libqt5_libdir}/libQt5QuickControls2.so
%{_libqt5_libdir}/pkgconfig/Qt5QuickControls2.pc
%{_libqt5_archdatadir}/mkspecs/modules/qt_lib_quickcontrols2.pri
%{_libqt5_archdatadir}/mkspecs/modules/qt_lib_quickcontrols2_private.pri

%files -n libQt5QuickTemplates2-devel
%defattr(-,root,root,755)
%doc LICENSE.*
%exclude %{_libqt5_includedir}/QtQuickTemplates2/%{so_version}
%{_libqt5_includedir}/QtQuickTemplates2
%{_libqt5_libdir}/libQt5QuickTemplates2.prl
%{_libqt5_libdir}/libQt5QuickTemplates2.so
%{_libqt5_archdatadir}/mkspecs/modules/qt_lib_quicktemplates2_private.pri

%files examples
%defattr(-,root,root,755)
%doc LICENSE.*
%{_libqt5_examplesdir}/

%changelog
