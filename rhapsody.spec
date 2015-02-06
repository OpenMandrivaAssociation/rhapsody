%define name	rhapsody
%define version 0.28b
%define release 6

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:    Text mode irc client with menu interface
License:	GPL
Url:		http://%{name}.sf.net/
Group:     	Networking/IRC
Source0:    	%{name}_%{version}.tar.bz2
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires:	ncurses-devel
%description
Rhapsody is a text console IRC client for Unix operating systems. 
It is small, fast, portable and easy to use, yet it is full featured. The thing
that separates it from the crowd is its intuitive menu driven user interface.

%prep
%setup -q

%build
./configure -i $RPM_BUILD_ROOT/%_bindir -d %_datadir/%name
make clean
%make

%install
rm -rf $RPM_BUILD_ROOT
perl -pi -e "s|INSTDOCSPATH=(.*)|INSTDOCSPATH=$RPM_BUILD_ROOT\$1|" src/Makefile.inc
%make install
chmod  0644 $RPM_BUILD_ROOT/%_datadir/%{name}/*/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root, 0755)
%doc docs/* 
%{_bindir}/*
%_datadir/%{name}/



%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.28b-5mdv2010.0
+ Revision: 433346
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.28b-4mdv2009.0
+ Revision: 260236
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.28b-3mdv2009.0
+ Revision: 248410
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.28b-1mdv2008.1
+ Revision: 126599
- kill re-definition of %%buildroot on Pixel's request
- import rhapsody


* Wed Mar 08 2006 Jerome Soyer <saispo@mandriva.org> 0.28b-1mdk
- New release 0.28b

* Wed Feb 15 2006 Michael Scherer <misc@mandriva.org> 0.27b-1mdk
- first mandriva release 
