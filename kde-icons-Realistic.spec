
%define		_name	Realistic

Summary:	KDE icons - %{_name}
Summary(pl.UTF-8):	Motyw ikon do KDE - %{_name}
Name:		kde-icons-%{_name}
Version:	20040407
Release:	1
License:	GPL
Group:		Themes
Source0:	http://www.metawire.org/~jpcohen/files/%{_name}.tar.gz
# Source0-md5:	9ff674394f1b212181bcbc4e4132a53b
URL:		http://www.kde-look.org/content/show.php?content=9707
Requires:	kdelibs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
%{_name} is a photo-realistic icon theme.

%description -l pl.UTF-8
%{_name} to motyw ikon cechujący się szczególną fotograficzną 
jakością.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_iconsdir}

%{__tar} xzf %{SOURCE0} -C $RPM_BUILD_ROOT%{_iconsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_iconsdir}/Realistic
