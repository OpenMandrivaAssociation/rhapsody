%define name	rhapsody
%define version 0.28b
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:    Text mode irc client with menu interface
License:	GPL
Url:		http://%{name}.sf.net/
Group:     	Networking/IRC
Source0:    	%{name}_%{version}.tar.bz2
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

