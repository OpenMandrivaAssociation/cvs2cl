%define url http://www.red-bean.com/cvs2cl/

Summary:	Generator of ChangeLogs from `cvs log` output
Name:		cvs2cl
Version:	2.73
Release:	4
Source0:	%{url}/cvs2cl.pl
Source1:	%{url}/changelogs.html
License:	GPL
Group:		Development/Other
URL:		%{url}
BuildArch:	noarch

%description
CVS2CL attempts to produce a nice ChangeLog from the cvs log output, some
say nicer than rcs2log. It is included with the open source CVS book :

http://cvsbook.red-bean.com/

%prep
%setup -T -c

%install
mkdir -p %{buildroot}/%{_bindir}
install -m755 %{SOURCE0} %{buildroot}/%{_bindir}/%{name}
install -m644 %{SOURCE1} ./

%files
%doc changelogs.html
%{_bindir}/%{name}



