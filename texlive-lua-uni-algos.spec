Name:		texlive-lua-uni-algos
Version:	62204
Release:	2
Summary:	Unicode algorithms for LuaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/lua-uni-algos
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lua-uni-algos.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lua-uni-algos.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Lua code working with Unicode data has to deal with quite some
challenges. For example there are many canonically equivalent
sequences which should be treated in the same way, and even
identifying a single character becomes quite different once you
have to deal with all kinds of combining characters, emoji
sequences and syllables in different scripts. Therefore
lua-uni-algos wants to build a collection of small libraries
implementing algorithms to deal with lots of the details in
Unicode, such that authors of LuaTeX packages can focus on
their actual functionality instead of having to fight against
the peculiarities of Unicode. Given that this package provides
Lua modules, it is only useful in Lua(HB)TeX. Additionally, it
expects an up-to-date version of the unicode-data package to be
present. This package is intended for package authors only; no
user-level functionality provided.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/luatex/lua-uni-algos
%doc %{_texmfdistdir}/doc/luatex/lua-uni-algos

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
