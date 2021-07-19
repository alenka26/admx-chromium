%define _destdir %_datadir/PolicyDefinitions
%define _unpackaged_files_terminate_build 1

Name: admx-chromium
Version: 91.0
Release: alt2

Summary: Chromium-specific ADMX policy templates
License: MPL-2.0
Group: System/Configuration/Other
Url: https://github.com/altlinux/admx-chromium
BuildArch: noarch

BuildRequires: admx-lint

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

%check
for file in *.admx *-*/*.adml; do
    admx-lint --input_file "$file"
done

%files
%dir %_destdir
%_destdir

%changelog
* Mon Jul 19 2021 Alenka Glukhovskaya <alenka@altlinux.org> 91.0-alt2
- Added admx and adml files checking via admx-lint

* Fri Apr 02 2021 Alenka Glukhovskaya <alenka@altlinux.org> 89.0-alt1
- Initial release

