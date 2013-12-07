# revision 15878
# category Package
# catalog-ctan /biblio/bibtex/contrib/german/dinat
# catalog-date 2008-11-11 09:02:39 +0100
# catalog-license pd
# catalog-version 2.5
Name:		texlive-dinat
Version:	2.5
Release:	6
Summary:	Bibliography style for German texts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/biblio/bibtex/contrib/german/dinat
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dinat.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dinat.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.5-2
+ Revision: 750959
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.5-1
+ Revision: 718232
- texlive-dinat
- texlive-dinat
- texlive-dinat
- texlive-dinat

