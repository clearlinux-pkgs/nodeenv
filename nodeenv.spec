#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : nodeenv
Version  : 0.13.6
Release  : 16
URL      : https://pypi.python.org/packages/source/n/nodeenv/nodeenv-0.13.6.tar.gz
Source0  : https://pypi.python.org/packages/source/n/nodeenv/nodeenv-0.13.6.tar.gz
Summary  : Node.js virtual environment builder
Group    : Development/Tools
License  : BSD-3-Clause
Requires: nodeenv-bin
Requires: nodeenv-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : setuptools

%description
Node.js virtual environment
===========================
``nodeenv`` (node.js virtual environment) is a tool to create
isolated node.js environments.

%package bin
Summary: bin components for the nodeenv package.
Group: Binaries

%description bin
bin components for the nodeenv package.


%package python
Summary: python components for the nodeenv package.
Group: Default

%description python
python components for the nodeenv package.


%prep
%setup -q -n nodeenv-0.13.6

%build
python2 setup.py build -b py2

%install
rm -rf %{buildroot}
python2 setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/nodeenv

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
