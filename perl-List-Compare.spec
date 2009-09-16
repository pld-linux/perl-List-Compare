#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	List
%define		pnam	Compare
Summary:	List::Compare - comparing elements of two lists
Summary(pl.UTF-8):	List::Compare - porównywanie elementów dwóch list
Name:		perl-List-Compare
Version:	0.37
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/List/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7c730dd58cc31a5bbb8eb7006edd1704
URL:		http://search.cpan.org/dist/List-Compare/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
List::Compare is a simple, object-oriented implementation of very
common Perl code used to determine interesting relationships between
two lists at a time.

%description -l pl.UTF-8
List::Compare jest prostą, obiektowo zorientowaną implementacją
popularnego perlowego kodu, używanego do określania relacji pomiędzy
dwoma listami.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests: %{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change* README
%{perl_vendorlib}/List/Compare.pm
%{perl_vendorlib}/List/Compare
%{_mandir}/man3/*
