%global tl_name lua-uni-algos
%global tl_revision 76195

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.5
Release:	%{tl_revision}.1
Summary:	Unicode algorithms for LuaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/generic/lua-uni-algos
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lua-uni-algos.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lua-uni-algos.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Lua code working with Unicode data has to deal with quite some
challenges. For example there are many canonically equivalent sequences
which should be treated in the same way, and even identifying a single
character becomes quite different once you have to deal with all kinds
of combining characters, emoji sequences and syllables in different
scripts. Therefore lua-uni-algos wants to build a collection of small
libraries implementing algorithms to deal with lots of the details in
Unicode, such that authors of LuaTeX packages can focus on their actual
functionality instead of having to fight against the peculiarities of
Unicode. Given that this package provides Lua modules, it is only useful
in Lua(HB)TeX. Additionally, it expects an up-to-date version of the
unicode-data package to be present. This package is intended for package
authors only; no user-level functionality provided.

