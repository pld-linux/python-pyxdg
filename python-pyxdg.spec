%define		module	pyxdg
Summary:	Python implementations of freedesktop.org standards
Summary(pl.UTF-8):	Implementacje standardów freedesktop.org w języku Python
Name:		python-%{module}
Version:	0.17
Release:	2
License:	LGPL
Group:		Libraries/Python
Source0:	http://www.freedesktop.org/~lanius/%{module}-%{version}.tar.gz
# Source0-md5:	a086de99cc536095684d87f15594e4db
URL:		http://freedesktop.org/Software/pyxdg
BuildRequires:	python-devel >= 1:2.4
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PyXDG is a python module to access freedesktop.org standards. The
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

%prep
%setup -q -n %{module}-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --optimize=2 --root=$RPM_BUILD_ROOT
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README TODO
%dir %{py_sitescriptdir}/xdg
%{py_sitescriptdir}/xdg/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/pyxdg-%{version}-py*.egg-info
%endif
