# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/csbulletin
# catalog-date 2008-08-17 11:40:59 +0200
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-csbulletin
Version:	1.0
Release:	4
Summary:	LaTeX class for articles submitted to the CSTUG Bulletin (Zpravodaj)
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/csbulletin
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/csbulletin.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/csbulletin.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides the class for articles for the CSTUG
Bulletin (Zpravodaj Ceskoslovenskeho sdruzeni uzivatelu TeXu).
You can see the structure of a document by looking to the
source file of the manual.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/csbulletin/csbulacronym.sty
%{_texmfdistdir}/tex/latex/csbulletin/csbulletin.cls
%doc %{_texmfdistdir}/doc/latex/csbulletin/LICENSE.txt
%doc %{_texmfdistdir}/doc/latex/csbulletin/README
%doc %{_texmfdistdir}/doc/latex/csbulletin/csbulletin.pdf
%doc %{_texmfdistdir}/doc/latex/csbulletin/csbulletin.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 750654
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 718170
- texlive-csbulletin
- texlive-csbulletin
- texlive-csbulletin
- texlive-csbulletin

