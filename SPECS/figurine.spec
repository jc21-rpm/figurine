%define debug_package %{nil}

%global gh_user arsham

Name:           figurine
Version:        2.1.1
Release:        1%{?dist}
Summary:        Print your name in style
Group:          Applications/System
License:        Apache-2.0
URL:            https://github.com/%{gh_user}/%{name}
BuildRequires:  git golang

%description
Print your name in style

%prep
git clone --branch v2.1.1 --depth 1 'https://github.com/arsham/figurine.git' %{_builddir}/%{name}-%{version}

%build
cd "%{_builddir}/%{name}-%{version}"
make linux-amd64
tar -xzf "deploy/%{name}_linux_amd64_v%{version}.tar.gz"

%install
install -Dm0755 %{_builddir}/%{name}-%{version}/deploy/%{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
* Mon Jun 1 2026 Jamie Curnow <jc@jc21.com> 2.1.1-1
- https://github.com/arsham/figurine/releases/tag/v2.1.1
