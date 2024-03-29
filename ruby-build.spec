Name:          ruby-build
Version:       20220726
Release:       1%{?dist}
Group:         Applications/System
Summary:       The ruby-build program for building Ruby instances.
BuildArch:     noarch
License:       MIT
URL:           https://github.com/rbenv/ruby-build
Source0:       %{url}/archive/v%{version}.tar.gz

BuildRequires: redhat-rpm-config

# For compiling rubies
Requires: openssl-devel readline-devel zlib-devel readline libyaml libyaml-devel readline-devel ncurses ncurses-devel gdbm gdbm-devel glibc-devel tcl-devel gcc unzip openssl-devel byacc make libffi-devel

%if 0%{?el7}
Requires: compat-db47
%else
Requires: db4-devel
%endif

# For running rubies
Requires: openssl libyaml

%description
Installs %{name}.

%prep
%setup

%build

%install
PREFIX=%{buildroot}/%{_prefix} \
  ./install.sh
%{__mkdir} -p %{buildroot}/%{_pkgdocdir}
%{__mv} README.md LICENSE %{buildroot}/%{_pkgdocdir}

%files
%doc %{_pkgdocdir}
%{_bindir}/*
%{_datarootdir}/%{name}
%license %{_pkgdocdir}/LICENSE

%changelog
* Mon Aug  8 2022 Jeffrey Lau <jeffrey.lau@ribose.com> - 20220726
- Bump version

* Fri Mar  5 2021 Jeffrey Lau <jeffrey.lau@ribose.com> - 20210119
- Bump version

* Fri Jul  3 2020 Jeffrey Lau <jeffrey.lau@ribose.com> - 20200520
- Bump version

* Tue Apr 30 2019 Jeffrey Lau <jeffrey.lau@ribose.com> - 20190423
- Bump version

* Wed Mar 27 2019 Jeffrey Lau <jeffrey.lau@ribose.com> - 20190320
- Bump version

* Sun Jun 18 2018 Ronald Tse <ronald.tse@ribose.com> - 20180618
- Bump version

* Mon Jan 22 2018 Jeffrey Lau <jeffrey.lau@ribose.com> - 20171215
- Bump version

* Fri Jun 23 2017 Ronald Tse <ronald.tse@ribose.com> - 20170523
- Initial commit
