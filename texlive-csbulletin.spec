Name:		texlive-csbulletin
Version:	65250
Release:	1
Summary:	LaTeX class for articles submitted to the CSTUG Bulletin (Zpravodaj)
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/csbulletin
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/csbulletin.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/csbulletin.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/csbulletin
%doc %{_texmfdistdir}/doc/latex/csbulletin

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
