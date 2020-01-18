%global pypi_name jsonpointer
%global github_name python-json-pointer
%global commit cfff4f4dd456c085cd0f5edfe88f074372204ede
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%if 0%{?fedora} > 12
    %global with_python3 1
%endif

Name: python-%{pypi_name}
Version: 1.9
Release: 2%{?dist}
Summary: Resolve JSON Pointers in Python

License: BSD
URL: https://github.com/stefankoegl/%{github_name}
# pypi tarball does not contain COPYING
Source0: https://github.com/stefankoegl/%{github_name}/archive/%{commit}/%{github_name}-%{version}-%{shortcommit}.tar.gz

BuildArch: noarch
BuildRequires: python2-devel
BuildRequires: python-setuptools
%if 0%{?with_python3}
BuildRequires: python3-devel
%endif

%description
Library to resolve JSON Pointers according to RFC 6901.

%if 0%{?with_python3}
%package -n python3-%{pypi_name}
Summary: Resolve JSON Pointers in Python
%description -n python3-%{pypi_name}
Library to resolve JSON Pointers according to RFC 6901.
%endif

%prep
%setup -qn %{github_name}-%{commit}
%if 0%{?with_python3}
rm -rf %{py3dir}
cp -ar . %{py3dir}
%endif

%build
%{__python} setup.py build
%if 0%{?with_python3}
pushd %{py3dir}
LC_ALL=en_US.UTF-8 \
    %{__python3} setup.py build
popd
%endif

%install
%if 0%{?with_python3}
pushd %{py3dir}
LC_ALL=en_US.UTF-8 \
    %{__python3} setup.py install --skip-build --root %{buildroot}
popd
%endif
%{__python} setup.py install --skip-build --root %{buildroot}

%check
%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} tests.py
popd
%endif
%{__python} tests.py

%files
%doc README.md COPYING AUTHORS
%{_bindir}/%{pypi_name}
%{python_sitelib}/%{pypi_name}.py*
%{python_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%doc README.md COPYING AUTHORS
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py*
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%endif

%changelog
* Wed Aug 05 2015 Lokesh Mandvekar <lsm5@redhat.com> - 1.9-2
- Resolves: rhbz#1243067 - add to rhel-7.2
- br: python-setuptools

* Wed Aug 05 2015 Lokesh Mandvekar <lsm5@redhat.com> - 1.9-1
- rebase to 1.9

* Thu Apr 17 2014 Lokesh Mandvekar <lsm5@redhat.com> - 1.0-4
- Rebuilt for RHEL-7

* Wed Feb  5 2014 Thomas Spura <tomspur@fedoraproject.org> - 1.0-3
- add python3 subpackage (#1061622)

* Thu Sep 05 2013 Alan Pevec <apevec@gmail.com> - 1.0-2
- add AUTHORS to docs

* Mon Jul 01 2013 Alan Pevec <apevec@gmail.com> - 1.0-1
- Initial package.
