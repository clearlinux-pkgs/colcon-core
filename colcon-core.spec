#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : colcon-core
Version  : 0.4.4
Release  : 29
URL      : https://files.pythonhosted.org/packages/a3/f9/059a61ddea19f19daec379ab28ac9c266f5beb1674ac606b7fc1bee39ac0/colcon-core-0.4.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/a3/f9/059a61ddea19f19daec379ab28ac9c266f5beb1674ac606b7fc1bee39ac0/colcon-core-0.4.4.tar.gz
Summary  : Command line tool to build sets of software packages.
Group    : Development/Tools
License  : Apache-2.0
Requires: colcon-core-bin = %{version}-%{release}
Requires: colcon-core-python = %{version}-%{release}
Requires: colcon-core-python3 = %{version}-%{release}
Requires: distlib
Requires: setuptools
BuildRequires : buildreq-distutils3
BuildRequires : distlib
BuildRequires : setuptools

%description
colcon - collective construction
================================
``colcon`` is a command line tool to improve the workflow of building, testing and using multiple software packages.
It automates the process, handles the ordering and sets up the environment to use the packages.

%package bin
Summary: bin components for the colcon-core package.
Group: Binaries

%description bin
bin components for the colcon-core package.


%package python
Summary: python components for the colcon-core package.
Group: Default
Requires: colcon-core-python3 = %{version}-%{release}

%description python
python components for the colcon-core package.


%package python3
Summary: python3 components for the colcon-core package.
Group: Default
Requires: python3-core

%description python3
python3 components for the colcon-core package.


%prep
%setup -q -n colcon-core-0.4.4
cd %{_builddir}/colcon-core-0.4.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1574467563
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/colcon

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
