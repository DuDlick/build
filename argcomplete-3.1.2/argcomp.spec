Name: argcomplete
Version: 3.1.2
Release: 1%{?dist}
Summary: Argcomplete provides easy, extensible command line tab completion of arguments for your Python application.

License: BSD
URL: https://pypi.org/project/argcomplete/#files:~:text=argcomplete%2D3.1.2.tar.gz
Source: %{name}-%{version}.tar.gz

BuildArch: noarch
BuildRequires: python3-devel
Requires: python3

%prep
%autosetup -n %{name}-%{version}.tar.gz

%build
%py3_build

%install
%py_install

%files
%license LICENSE
%{python3_sitelib}/argcomplete*
%{python3_sitelib}/argcomplete-%{version}-py%{python3_version}.egg-info

