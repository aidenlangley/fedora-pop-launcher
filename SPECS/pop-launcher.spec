%global gituser     pop-os
%global gitrepo     launcher

Name:       pop-launcher
Version:    1.0.2
Release:    1%{?dist}
Summary:    Modular IPC-based desktop launcher service

# GPL-3.0 License
License:    GPLv3 and ASL 2.0 and MIT
URL:        https://github.com/%{gituser}/%{gitrepo}.git
Source0:    https://github.com/%{gituser}/%{gitrepo}/archive/refs/tags/%{version}.tar.gz

BuildRequires:  make cargo openssl-devel gtk3-devel
# xdg-open qalc locale pactl fdfind
Requires:       gnome-shell-extension-pop-shell
Requires:       libqulculate
Requires:       xdg-utils
Requires:       glibc-common

# TODO: Remove pulse plugin folder
# dnf repoquery --provides libqalculate
# dnf repoquery --whatrequires 'libqalculate.so.21()(64bit)'

%description
Pop Shell provides an integrated launcher which interfaces directly with our
pop-launcher service. JSON IPC is used to communicate between the shell and the
launcher in an asynchronous fashion. This functionality was separated from the
shell due to performance and maintainability issues. The new launcher is written
in Rust and fully async. The launcher has extensive features that would be
useful for implementing desktop launchers beyond a shell extension.

%prep
%autosetup -n %{gitrepo}-%{version}

%build
%make_build

%install
%make_install

%files
%license LICENSE
%doc README.md
%{_prefix}/lib/%{name}

%changelog
* Thu Oct 28 2021 Aiden Langley <me@aidenlangley.com> - 1.0.2
- Initial package
