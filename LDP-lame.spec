Summary:	LDP Linux System Administration Made Easy
Summary(pl):	Jak sobie u³atwiæ ¿ycie - poradnik dla administratora
Name:		LDP-lame
Version:	1.06
Release:	1
License:	distributable
Group:		Documentation
Source0:	http://www.tldp.org/LDP/lame/lame.html.tar.gz
# Source0-md5:	2bc5df0ddf3b8d41d9ccd4683b115616
URL:		http://www.tldp.org/LDP/lame/LAME/linux-admin-made-easy/index.html
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Linux Administration Made Easy (LAME) guide attempts to describe
day-to-day administration and maintenance issues commonly faced by
Linux system administrators.

This book can be purchased from bookstores.

%description -l pl
The Linux Administration Made Easy (LAME) - próbuje opisaæ sytuacje z
jakimi musi siê zmagaæ administrator Linuksa na co dzieñ.

Ksi±¿ka jest dostêpna tak¿e w ksiêgarniach.

%prep
%setup -q -n linux-admin-made-easy

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_docdir}/LDP/lame

cp -ar * $RPM_BUILD_ROOT%{_docdir}/LDP/lame

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_docdir}/LDP/lame
