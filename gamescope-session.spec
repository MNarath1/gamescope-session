Name:           gamescope-session
Version:        1.0
Release:        1%{?dist}
Summary:        Gamescope session plus based on Valve's gamescope

License:        MIT
URL:            https://github.com/MNarath1/gamescope-session

Source:        	https://github.com/MNarath1/gamescope-session/archive/refs/tags/1.0.tar.gz
BuildArch:      noarch

Requires:       gamescope
Requires:       python3
Requires:       switcheroo-control
Requires:       gawk

BuildRequires:  systemd-rpm-macros

%description
Gamescope session plus based on Valve's gamescope

%prep
%autosetup

%build

%install
mkdir -p %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_datadir}/
mkdir -p %{buildroot}%{_userunitdir}/
cp -rv usr/bin/* %{buildroot}%{_bindir}
cp -rv usr/share/* %{buildroot}%{_datadir}
cp -v usr/lib/systemd/user/* %{buildroot}%{_userunitdir}

# Do post-installation
%post

# Do before uninstallation
%preun

# Do after uninstallation
%postun

# This lists all the files that are included in the rpm package and that
# are going to be installed into target system where the rpm is installed.
%files
%license LICENSE
%doc README.md
%{_bindir}/export-gpu
%{_bindir}/gamescope-session-plus
%{_datadir}/gamescope-session-plus/device-quirks
%{_datadir}/gamescope-session-plus/gamescope-session-plus
%{_userunitdir}/gamescope-session-plus@.service
%{_userunitdir}/gamescope-session.target
%{_datadir}/gamescope/scripts/50-custom/50-disable-explicit-sync.lua
