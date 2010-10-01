%define name cvs2cl
%define version 2.72
%define release %mkrel 1
%define url http://www.red-bean.com/cvs2cl/

Summary: Generator of ChangeLog(s) from `cvs log` output
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{url}/cvs2cl.pl
Source1: %{url}/changelogs.html
License: GPL
Group: Development/Other
URL: %url
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildArchitectures: noarch

%description
CVS2CL attempt to product a nice ChangeLog from cvs log output, some
say nicer than rcs2log. He included with the OpenSouce cvs book :

http://cvsbook.red-bean.com/

%prep
%setup -T -c

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/%{_bindir}
install -m755 %{SOURCE0} %{buildroot}/%{_bindir}/%{name}
install -m644 %{SOURCE1} ./

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc changelogs.html
%{_bindir}/%{name}


