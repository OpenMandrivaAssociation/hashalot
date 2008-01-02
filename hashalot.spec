%define name    hashalot
%define version 0.3
%define release %mkrel 2

Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2 
Summary: Binary hash generator
License: GPL
Group: System/Base
Url: http://www.paranoiacs.org/~sluskyb/hacks/hashalot
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
This program will read a passphrase from standard input and print a binary
(not printable) hhash to standard output.  The output is suitable for use as
an encryption key.

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q -n %{name}-%{version}

%build
%configure
%make
chmod 644 AUTHORS COPYING INSTALL NEWS README
chmod 644 *.c *.h

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING INSTALL NEWS README
%_sbindir/hashalot
%_sbindir/rmd160
%_sbindir/sha256
%_sbindir/sha384
%_sbindir/sha512
%_mandir/man1/hashalot*

