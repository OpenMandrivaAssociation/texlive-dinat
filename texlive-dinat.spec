# revision 15878
# category Package
# catalog-ctan /biblio/bibtex/contrib/german/dinat
# catalog-date 2008-11-11 09:02:39 +0100
# catalog-license pd
# catalog-version 2.5
Name:		texlive-dinat
Version:	2.5
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Bibliography style files intended for texts in german. They
draw up bibliographies in accordance with the german DIN 1505,
parts 2 and 3.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/dinat/dinat.bst
%doc %{_texmfdistdir}/doc/bibtex/dinat/dinat-index.html
%doc %{_texmfdistdir}/doc/bibtex/dinat/history.html
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
