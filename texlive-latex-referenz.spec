Name:		texlive-latex-referenz
Version:	20190228
Release:	2
Summary:	Examples from the book "LaTeX Referenz"
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/examples/LaTeX-Referenz
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-referenz.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-referenz.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
This bundle contains all the examples, as source, eps and pdf,
of the author's book "LaTeX Referenz" (2nd ed.), published by
DANTE/Lehmanns. The examples can be run as usual with the
example class ttctexa.cls, which is in the distribution.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/latex-referenz

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
