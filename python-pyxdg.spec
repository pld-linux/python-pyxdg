#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module	pyxdg
Summary:	Python 2 implementations of freedesktop.org standards
Summary(pl.UTF-8):	Implementacje standardów freedesktop.org w języku Python 2
Name:		python-%{module}
Version:	0.25
Release:	2
License:	LGPL v2
Group:		Libraries/Python
Source0:	http://people.freedesktop.org/~takluyver/%{module}-%{version}.tar.gz
# Source0-md5:	bedcdb3a0ed85986d40044c87f23477c
URL:		http://freedesktop.org/Software/pyxdg
%{?with_python2:BuildRequires:	python-devel >= 1:2.6}
%{?with_python3:BuildRequires:	python3-devel >= 1:3.2}
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PyXDG is a Python module to access freedesktop.org standards. The
package contains:

 - Implementation of the XDG-Base-Directory Standard
 - Implementation of the XDG-Desktop Standard
 - Implementation of the XDG-Menu Standard
 - Implementation of the XDG-Icon-Theme Standard
 - Implementation of the XDG-Shared MIME-info Database
 - Implementation of the XDG-Recent File Storage Specification

%description -l pl.UTF-8
PyXDG jest modułem języka Python, pozwalającym na wykorzystywanie
standardów freedesktop.org. Pakiet zawiera:

 - Implementację standardu XDG-Base-Directory
 - Implementację standardu XDG-Desktop
 - Implementację standardu XDG-Menu
 - Implementację standardu XDG-Icon-Theme
 - Implementację bazy XDG-Shared MIME-info
 - Implementację specyfikacji XDG-Recent File Storage

%package -n python3-pyxdg
Summary:	Python 3 implementations of freedesktop.org standards
Summary(pl.UTF-8):	Implementacje standardów freedesktop.org w języku Python 3
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-pyxdg
PyXDG is a Python module to access freedesktop.org standards. The
package contains:

 - Implementation of the XDG-Base-Directory Standard
 - Implementation of the XDG-Desktop Standard
 - Implementation of the XDG-Menu Standard
 - Implementation of the XDG-Icon-Theme Standard
 - Implementation of the XDG-Shared MIME-info Database
 - Implementation of the XDG-Recent File Storage Specification

%description -n python3-pyxdg -l pl.UTF-8
PyXDG jest modułem języka Python, pozwalającym na wykorzystywanie
standardów freedesktop.org. Pakiet zawiera:

 - Implementację standardu XDG-Base-Directory
 - Implementację standardu XDG-Desktop
 - Implementację standardu XDG-Menu
 - Implementację standardu XDG-Icon-Theme
 - Implementację bazy XDG-Shared MIME-info
 - Implementację specyfikacji XDG-Recent File Storage

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%{__python} setup.py build \
	--build-base build-2
%endif

%if %{with python3}
%{__python3} setup.py build \
	--build-base build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%{__python} setup.py \
	build \
		--build-base build-2 \
	install \
		--optimize=2 \
		--root=$RPM_BUILD_ROOT
%py_postclean
%endif

%if %{with python3}
%{__python3} setup.py \
	build \
		--build-base build-3 \
	install \
		--optimize=2 \
		--root=$RPM_BUILD_ROOT
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%dir %{py_sitescriptdir}/xdg
%{py_sitescriptdir}/xdg/*.py[co]
%{py_sitescriptdir}/pyxdg-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-pyxdg
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%dir %{py3_sitescriptdir}/xdg
%{py3_sitescriptdir}/xdg/*.py
%{py3_sitescriptdir}/xdg/__pycache__
%{py3_sitescriptdir}/pyxdg-%{version}-py*.egg-info
%endif
