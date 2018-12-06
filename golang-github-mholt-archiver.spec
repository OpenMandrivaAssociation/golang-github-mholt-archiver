%global goipath    github.com/mholt/archiver
Version: 2.0

%global common_description %{expand:
Package archiver makes it trivially easy to make and extract common archive
formats such as .zip, and .tar.gz. Simply name the input and output file(s).

Files are put into the root of the archive; directories are recursively added,
preserving structure.

The archiver command runs the same cross-platform and has no external
dependencies (not even libc); powered by the Go standard library,
dsnet/compress, nwaples/rardecode, and ulikunitz/xz. Enjoy!

Supported formats/extensions:

    .zip
    .tar
    .tar.gz & .tgz
    .tar.bz2 & .tbz2
    .tar.xz & .txz
    .tar.lz4 & .tlz4
    .tar.sz & .tsz
    .rar (open only)}

%gometa

Name:           %{goname}
Release:        3%{?dist}
Summary:        Easily create and extract archive files with Go
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
BuildRequires:  golang(github.com/dsnet/compress/bzip2)
BuildRequires:  golang(github.com/nwaples/rardecode)
BuildRequires:  golang(github.com/ulikunitz/xz)

%description
%{common_description}

%package devel
Summary: %{summary}
BuildArch: noarch
Requires: %{name} = %{version}-%{release}

%description devel
%{common_description}

This package contains the source code needed for building packages that import
the %{goipath} Go namespace.

%prep
%gosetup -q

%build
%gobuildroot
%gobuild -o _bin/archiver %{goipath}/cmd/archiver

%install
%goinstall
install -m 0755 -vd        %{buildroot}%{_bindir}
install -m 0755 -vp _bin/* %{buildroot}%{_bindir}/

%check
%gochecks

%files
%license LICENSE
%doc README.md
%{_bindir}/*

%files devel -f devel.file-list

%changelog
* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 2.0-3
- Rebuild with fixed binutils

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 26 2018 Dominik Mierzejewski <dominik@greysector.net> - 2.0-1
- initial package for Fedora
