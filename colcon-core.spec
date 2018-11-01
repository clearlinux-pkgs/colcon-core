#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : colcon-core
Version  : 0.3.12
Release  : 10
URL      : https://files.pythonhosted.org/packages/37/dd/ebb44097dd8f9c57bfa17bc202bce9a3a1a5e44a3d911c050002cae0dbf6/colcon-core-0.3.12.tar.gz
Source0  : https://files.pythonhosted.org/packages/37/dd/ebb44097dd8f9c57bfa17bc202bce9a3a1a5e44a3d911c050002cae0dbf6/colcon-core-0.3.12.tar.gz
Summary  : Command line tool to build sets of software packages.
Group    : Development/Tools
License  : Apache-2.0
Requires: colcon-core-bin = %{version}-%{release}
Requires: colcon-core-python = %{version}-%{release}
Requires: colcon-core-python3 = %{version}-%{release}
Requires: pytest
Requires: pytest-cov
Requires: pytest-repeat
Requires: pytest-rerunfailures
Requires: pytest-runner
Requires: setuptools
BuildRequires : buildreq-distutils3

%description
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
%setup -q -n colcon-core-0.3.12

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1541038345
python3 setup.py build

%install
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
