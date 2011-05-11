#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Regexp
%define		pnam	IPv6
%include	/usr/lib/rpm/macros.perl
Summary:	Regexp::IPv6 - Regular expression for IPv6 addresses
#Summary(pl.UTF-8):	
Name:		perl-Regexp-IPv6
Version:	0.03
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Regexp/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	892abe3f43eb0cc76283767f99a335e6
URL:		http://search.cpan.org/dist/Regexp-IPv6/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module exports the $IPv6_re regular expression that matches any
valid IPv6 address as described in "RFC 2373 - 2.2 Text Representation
of Addresses" but ::. Any string not compliant with such RFC will
be rejected.

To match full strings use /^$IPv6_re$/.



# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Regexp/*.pm
%{_mandir}/man3/*
