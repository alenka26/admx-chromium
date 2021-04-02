%define _destdir %_datadir/PolicyDefinitions
%define _unpackaged_files_terminate_build 1

Name: admx-chromium
Version: 89.0
Release: alt1

Summary: Chromium-specific ADMX policy templates
License: MPL-2.0
Group: System/Configuration/Other
Url: https://github.com/altlinux/admx-chromium
BuildArch: noarch

Source0: %name-%version.tar

%description
Chromium-specific ADMX files, which are registry-based policy settings provide
an XML-based structure for defining the display of the Administrative Template
policy settings in the Group Policy Object Editor.

%prep
%setup -q

%install
mkdir -p %buildroot%_destdir
cp -a windows/admx/ %buildroot%_destdir/

%files
%dir %_destdir
%_destdir

%changelog
* Fri Apr 02 2021 Alenka Glukhovskaya <alenka@altlinux.org> 89.0-alt1
- Initial release

