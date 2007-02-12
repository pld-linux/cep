Summary:	Compress/uncompress PostScript files
Summary(pl.UTF-8):   Kompresja/dekompresja plików PostScript
Name:		cep
Version:	1.03
Release:	1
License:	Public Domain
Group:		Applications/Graphics
Source0:	http://www.agh.edu.pl/pub/tex/GUST/contrib/PS-supp/%{name}.zip
# Source0-md5:	f1ce5e65b73bbcc1130dbde4a0b7c2af
Source1:	%{name}-add.tar.gz
# Source1-md5:	d97220c4c5862487585fbe76f0c5fb00
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ghostscript
BuildRequires:	unzip
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cep/cop compresses Postscript files producing self-extracting
Postscript level 2 files, that can be used instead of original files.

%description -l pl.UTF-8
cep/cop kompresuje pliki Postscript produkując samorozpakowywalne
pliki PS poziomu 2, które mogą być wykorzystane zamiast oryginalnych
plików.

%prep
%setup -q -n cep -b 1

%build
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc 0cep_lic.pol 0cep_lic.eng *.inf
%attr(755,root,root) %{_bindir}/*
%{_datadir}/cep
%{_mandir}/*/*
