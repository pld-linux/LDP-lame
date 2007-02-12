Summary:	LDP Linux System Administration Made Easy
Summary(pl.UTF-8):   Jak sobie ułatwić życie - poradnik dla administratora
Name:		LDP-lame
Version:	1.06
Release:	1
License:	distributable
Group:		Documentation
Source0:	http://www.tldp.org/LDP/lame/lame.html.tar.gz
# Source0-md5:	2bc5df0ddf3b8d41d9ccd4683b115616
URL:		http://www.tldp.org/LDP/lame/LAME/linux-admin-made-easy/index.html
Requires:	LDP-base
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Linux Administration Made Easy (LAME) guide attempts to describe
day-to-day administration and maintenance issues commonly faced by
Linux system administrators.

This book can be purchased from bookstores.

%description -l pl.UTF-8
The Linux Administration Made Easy (LAME) - próbuje opisać sytuacje z
jakimi musi się zmagać administrator Linuksa na co dzień.

Książka jest dostępna także w księgarniach.

%prep
%setup -q -n linux-admin-made-easy

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_docdir}/LDP/lame
cp -a * $RPM_BUILD_ROOT%{_docdir}/LDP/lame

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_docdir}/LDP/lame
