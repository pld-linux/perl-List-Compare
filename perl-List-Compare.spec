%include	/usr/lib/rpm/macros.perl
%define		pdir	List
%define		pnam	Compare
Summary:	List::Compare - comparing elements of two lists
Summary(pl):	List::Compare - porównywanie elementów dwóch list
Name:		perl-List-Compare
Version:	0.16
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6.1
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
List::Compare is a simple, object-oriented implementation of very
common Perl code used to determine interesting relationships between
two lists at a time.

%description -l pl
List::Compare jest prostą, obiektowo zorientowaną implementacją
popularnego Perlowego kodu, używanego do określania relacji pomiędzy
dwoma listami.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}
#%%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change* README
%{perl_sitelib}/%{pdir}/*.pm
%{_mandir}/man3/*
