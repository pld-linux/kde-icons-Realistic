#$Revision: 1.1 $, $Date: 2004-04-16 18:49:35 $

%define         _name Realistic

Summary:	KDE icons - %{_name}
Summary(pl):	Motyw ikon do KDE - %{_name}
Name:		kde-icons-%{_name}
Version:	20040407
Release:	1
License:	GPL
Group:		Themes
Source0:	http://www.metawire.org/%7Ejpcohen/files/%{_name}.tar.gz
# Source0-md5:	9ff674394f1b212181bcbc4e4132a53b
URL:		http://www.kde-look.org/content/show.php?content=9707
Requires:	kdelibs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
%{_name} is a photo-icon theme.

%description -l pl
%{_name} to fotograficzny motyw ikon.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_iconsdir}

%{__tar} xfz %{SOURCE0} -C $RPM_BUILD_ROOT%{_iconsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_iconsdir}/
