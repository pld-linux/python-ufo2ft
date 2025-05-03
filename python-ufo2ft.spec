#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	A bridge between UFOs and FontTools
Summary(pl.UTF-8):	Pomost między UFO a FontTools
Name:		python-ufo2ft
# keep 2.10.x for python2 support
Version:	2.10.0
Release:	2
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/ufo2ft/
Source0:	https://files.pythonhosted.org/packages/source/u/ufo2ft/ufo2ft-%{version}.zip
# Source0-md5:	8678156f5bcb25374ab567f674086cf7
URL:		https://pypi.org/project/ufo2ft/
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
BuildRequires:	python-setuptools_scm
%if %{with tests}
BuildRequires:	python-booleanOperations >= 0.8.2
BuildRequires:	python-compreffor >= 0.4.6
BuildRequires:	python-cu2qu >= 1.6.5
BuildRequires:	python-enum34 >= 1.1.6
# fonttools[ufo]
BuildRequires:	python-fonttools >= 3.43.0
BuildRequires:	python-fs >= 2.2.0
BuildRequires:	python-pytest >= 2.8
BuildRequires:	python-skia-pathops >= 0.2.0
BuildRequires:	python-ufoLib2 >= 0.3.2.post2
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	unzip
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ufo2ft ("UFO to FontTools") is a fork of ufo2fdk whose goal is to
generate OpenType font binaries from UFOs without the FDK dependency.

%description -l pl.UTF-8
ufo2ft ("UFO to FontTools") to odgałęzienie projektu ufo2fdk. Celem
odgałęzienia jest generowanie z UFO binariów fontów OpenType bez
zależności od FDK.

%prep
%setup -q -n ufo2ft-%{version}

%build
%py_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTHONPATH=$(pwd)/Lib \
%{__python} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py_sitescriptdir}/ufo2ft
%{py_sitescriptdir}/ufo2ft-%{version}-py*.egg-info
