%global tl_name dinat
%global tl_revision 76790

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.5
Release:	%{tl_revision}.1
Summary:	Bibliography style for German texts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/biblio/bibtex/contrib/german/dinat
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dinat.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dinat.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Bibliography style files intended for texts in german. They draw up
bibliographies in accordance with the german DIN 1505, parts 2 and 3.

