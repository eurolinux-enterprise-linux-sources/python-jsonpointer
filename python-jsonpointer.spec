%global pypi_name jsonpointer
%global github_name python-json-pointer
%global commit c1ec3dfd171b242e23b3fe078a99f0e23fb0c6ea
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           python-%{pypi_name}
Version:        1.0
Release:        4%{?dist}
Summary:        Resolve JSON Pointers in Python

License:        BSD
URL:            https://github.com/stefankoegl/%{github_name}
# pypi tarball does not contain COPYING
Source0:        https://github.com/stefankoegl/%{github_name}/archive/%{commit}/%{github_name}-%{version}-%{shortcommit}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel

%description
Library to resolve JSON Pointers according to RFC 6901.

%prep
%setup -qn %{github_name}-%{commit}

%build
%{__python} setup.py build

%install
%{__python} setup.py install --skip-build --root %{buildroot}

%check
%{__python} tests.py

%files
%doc README.md COPYING AUTHORS
%{python_sitelib}/%{pypi_name}.py*
%{python_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Mon Feb 20 2017 Charalampos Stratakis <cstratak@redhat.com> - 1.0-4
- Import to RHEL 6.9
- Increment the release so it will replace the respective EPEL build
Resolves: rhbz#1422977

* Thu Sep 05 2013 Alan Pevec <apevec@gmail.com> - 1.0-2
- add AUTHORS to docs

* Mon Jul 01 2013 Alan Pevec <apevec@gmail.com> - 1.0-1
- Initial package.
