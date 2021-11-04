# Generated by rust2rpm 18
%global debug_package %{nil}

Name:       pop-launcher
Version:    1.0.3
Release:    %autorelease
Summary:    Modular IPC-based desktop launcher service

License:    GPLv3 and ASL 2.0 and MIT

ExclusiveArch:  %{rust_arches}

%global gituser pop-os
%global gitrepo launcher
%global commit  170c6bbfb25c0683c4e70701a1da88613968cf2a

URL:        https://github.com/%{gituser}/%{gitrepo}
Source0:    %{url}/archive/%{commit}/%{gitrepo}-%{commit}.tar.gz

BuildRequires:  cargo gtk3-devel openssl-devel
Requires:       gnome-shell-extension-pop-shell

Recommends: libqalculate qalc fd-find

Provides:   pop-launcher
Provides:   qalc
Provides:   find

%description
Modular IPC-based desktop launcher service, written in Rust. Desktop launchers
may interface with this service via spawning the pop-launcher process and
communicating to it via JSON IPC over the stdin and stdout pipes. The launcher
service will also spawn plugins found in plugin directories on demand, based on
the queries sent to the service.

%prep
%autosetup -n %{gitrepo}-%{commit} -p1

%build
%make_build

%install
%make_install


%files
%license    COPYING
%doc        README.md debian/changelog
%dir        %{_prefix}/lib/%{name}/plugins/calc/
%dir        %{_prefix}/lib/%{name}/plugins/desktop_entries/
%dir        %{_prefix}/lib/%{name}/plugins/files/
%dir        %{_prefix}/lib/%{name}/plugins/find/
%dir        %{_prefix}/lib/%{name}/plugins/pop_shell/
%dir        %{_prefix}/lib/%{name}/plugins/pulse/
%dir        %{_prefix}/lib/%{name}/plugins/recent/
%dir        %{_prefix}/lib/%{name}/plugins/scripts/
%dir        %{_prefix}/lib/%{name}/plugins/terminal/
%dir        %{_prefix}/lib/%{name}/plugins/web/
%dir        %{_prefix}/lib/%{name}/scripts/session/
%dir        %{_prefix}/lib/%{name}/scripts/system76-power/
%{_bindir}/pop-launcher

%changelog
* Thu Nov 04 2021 Aiden Langley <me@aidenlangley.com> - 1.0.3
- Initial package
