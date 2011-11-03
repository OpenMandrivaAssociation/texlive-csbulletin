# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/csbulletin
# catalog-date 2008-08-17 11:40:59 +0200
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-csbulletin
Version:	1.0
Release:	1
Summary:	LaTeX class for articles submitted to the CSTUG Bulletin (Zpravodaj)
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/csbulletin
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/csbulletin.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/csbulletin.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package provides the class for articles for the CSTUG
Bulletin (Zpravodaj Ceskoslovenskeho sdruzeni uzivatelu TeXu).
You can see the structure of a document by looking to the
source file of the manual.

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
%{_texmfdistdir}/tex/latex/csbulletin/csbulacronym.sty
%{_texmfdistdir}/tex/latex/csbulletin/csbulletin.cls
%doc %{_texmfdistdir}/doc/latex/csbulletin/LICENSE.txt
%doc %{_texmfdistdir}/doc/latex/csbulletin/README
%doc %{_texmfdistdir}/doc/latex/csbulletin/csbulletin.pdf
%doc %{_texmfdistdir}/doc/latex/csbulletin/csbulletin.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
