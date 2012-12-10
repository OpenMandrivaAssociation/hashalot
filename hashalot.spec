%define name    hashalot
%define version 0.3
%define release %mkrel 6

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



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3-6mdv2011.0
+ Revision: 619354
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.3-5mdv2010.0
+ Revision: 429386
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.3-4mdv2009.0
+ Revision: 246792
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.3-2mdv2008.1
+ Revision: 140746
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import hashalot


* Sun Oct 30 2005 Anne Nicolas <anne.nicolas@mandriva.com> 0.3-2mdk
- Fix permissions on debug files

* Sat Oct 29 2005 Anne Nicolas <anne.nicolas@mandriva.com> 0.3-1mdk
- initial release
