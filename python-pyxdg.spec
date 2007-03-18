%define		module	pyxdg
Summary:	Python library to access freedesktop.org standards
Summary(pl.UTF-8):	Biblioteka pythona do u¿ywania standardów freedesktop.org
Name:		python-%{module}
Version:	0.15
Release:	0.1
License:	LGPL
Group:		Development/Libraries
Source0:	http://www.freedesktop.org/~lanius/%{module}-%{version}.tar.gz
# Source0-md5:	86a5441285fc908145414b63348d11a3
URL:		http://freedesktop.org/Software/pyxdg
BuildRequires:	python-devel
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PyXDG is a python library to access freedesktop.org standards.

%description -l pl.UTF-8
PyXDG jest bibliotek± pythona do u¿ywania standardów freedesktop.org.

%prep
%setup -q -n %{module}-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --skip-build --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README TODO
%{py_sitescriptdir}/pyxdg-%{version}-py2.5.egg-info
%dir %{py_sitescriptdir}/xdg
%{py_sitescriptdir}/xdg/*.pyc
