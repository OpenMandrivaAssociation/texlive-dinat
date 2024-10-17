Name:		texlive-dinat
Version:	15878
Release:	2
Summary:	Bibliography style for German texts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/biblio/bibtex/contrib/german/dinat
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dinat.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dinat.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Bibliography style files intended for texts in german. They
draw up bibliographies in accordance with the german DIN 1505,
parts 2 and 3.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/dinat/dinat.bst
%doc %{_texmfdistdir}/doc/bibtex/dinat/dinat-index.html
%doc %{_texmfdistdir}/doc/bibtex/dinat/history.html

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex doc %{buildroot}%{_texmfdistdir}
