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


Name:           qt5-qtquickcontrols2
Version:        5.6.2
Release:        0
Summary:        Qt 5 Quick Controls Addon
License:        SUSE-LGPL-2.1-with-digia-exception-1.1 or GPL-3.0
Group:          Development/Libraries/X11
Url:            http://qt.digia.com
Source:         %{name}-%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  qt5-qtcore-devel
BuildRequires:  qt5-qtgui-devel
BuildRequires:  qt5-qtdeclarative
BuildRequires:  qt5-qtdeclarative-qtquick-devel
BuildRequires:  qt5-qmake

%description
The Qt Quick Controls2 module provides a set of controls that
can be used to build complete interfaces in Qt Quick.


%prep
%setup -q -n %{name}-%{version}/qtquickcontrols2

%build
export QTDIR=/usr/share/qt5
touch .git

%qmake5
make %{?_smp_flags}

%install
rm -rf %{buildroot}
%qmake5_install

%post 
/sbin/ldconfig

%postun 
/sbin/ldconfig

%files
%defattr(-,root,root,755)
%{_libdir}/libQt5QuickControls2.so.*


%changelog
