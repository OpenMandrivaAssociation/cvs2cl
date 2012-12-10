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




%changelog
* Fri Oct 01 2010 Funda Wang <fwang@mandriva.org> 2.72-1mdv2011.0
+ Revision: 582266
- update to new version 2.72

* Wed Sep 02 2009 Thierry Vignaud <tv@mandriva.org> 2.71-2mdv2011.0
+ Revision: 425486
- rebuild

* Sat Aug 23 2008 Olivier Thauvin <nanardon@mandriva.org> 2.71-1mdv2009.0
+ Revision: 275279
- 2.71

* Tue Jul 22 2008 Thierry Vignaud <tv@mandriva.org> 2.62-3mdv2009.0
+ Revision: 240517
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Jul 02 2007 Olivier Thauvin <nanardon@mandriva.org> 2.62-1mdv2008.0
+ Revision: 46908
- 2.62


* Sat Aug 05 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/05/06 00:24:21 (53169)
- rebuild

* Sat Aug 05 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/05/06 00:22:34 (53168)
Import cvs2cl

* Thu Oct 20 2005 Olivier Thauvin <nanardon@mandriva.org> 2.59-1mdk
- 2.59
- create a builddir to have cleaner build process

* Tue Aug 10 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.57-1mdk
- new release
- drop tag

