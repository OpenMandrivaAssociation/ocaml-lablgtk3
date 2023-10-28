%define _disable_ld_no_undefined 1

%undefine _package_note_flags

Name:           ocaml-lablgtk3
Version:        3.1.3
Release:        1
Summary:        OCaml interface to gtk3
Group:          Development/OCaml
License:        LGPLv2+ with exceptions
URL:            https://garrigue.github.io/lablgtk/
Source0:        https://github.com/garrigue/lablgtk/archive/%{version}/lablgtk3-%{version}.tar.gz
# Fedora only patch: unbundle xml-light
Patch0:         %{name}-xml-light.patch
Patch1:         ocaml-lablgtk3-version.patch
BuildRequires:  help2man
BuildRequires:  ocaml >= 4.05.0
BuildRequires:  ocaml-cairo-devel >= 0.6
BuildRequires:  ocaml-camlp5-devel
BuildRequires:  ocaml-camlp-streams-devel
BuildRequires:  ocaml-csexp-devel
BuildRequires:  ocaml-dune-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-xml-light-devel
BuildRequires:  pkgconfig(goocanvas-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtksourceview-3.0)
BuildRequires:  pkgconfig(gtkspell3-3.0)

%global _description %{expand:
LablGTK3 is an Objective Caml interface to gtk3.  It uses the rich
type system of Objective Caml to provide a strongly typed, yet very
comfortable, object-oriented interface to gtk3.}

%description %_description

%files
%doc CHANGES.md CHANGELOG.API README.md doc
%license LGPL LICENSE
%{_mandir}/man1/gdk_pixbuf_mlsource3.1*
%{_mandir}/man1/lablgladecc3.1*
%{_bindir}/gdk_pixbuf_mlsource3
%{_bindir}/lablgladecc3
%{_libdir}/ocaml/stublibs/dlllablgtk3_stubs.so
%{_libdir}/ocaml/lablgtk3/META
%{_libdir}/ocaml/lablgtk3/*.cma
%{_libdir}/ocaml/lablgtk3/*.cmi
%{_libdir}/ocaml/lablgtk3/*.cmxs

#-----------------------------------------------------------------
%package        devel
Summary:        Development files for %{name}
Group:          Development/OCaml
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(gtk+-3.0)
Requires:       ocaml-cairo-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%files devel
%{_libdir}/ocaml/lablgtk3/*.a
%{_libdir}/ocaml/lablgtk3/*.cmx
%{_libdir}/ocaml/lablgtk3/*.cmxa
%{_libdir}/ocaml/lablgtk3/*.cmt
%{_libdir}/ocaml/lablgtk3/*.cmti
%{_libdir}/ocaml/lablgtk3/*.mli
%{_libdir}/ocaml/lablgtk3/*.h
%{_libdir}/ocaml/lablgtk3/dune-package
%{_libdir}/ocaml/lablgtk3/opam

#-----------------------------------------------------------------
%package        goocanvas2
Summary:        OCaml interface to GooCanvas
Group:          Development/OCaml
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(goocanvas-2.0)

%description    goocanvas2 %_description

This package contains OCaml bindings for the GTK3 GooCanvas library.

%files goocanvas2
%{_libdir}/ocaml/stublibs/dlllablgtk3_goocanvas2_stubs.so
%{_libdir}/ocaml/lablgtk3-goocanvas2/META
%{_libdir}/ocaml/lablgtk3-goocanvas2/*.cma
%{_libdir}/ocaml/lablgtk3-goocanvas2/*.cmi
%{_libdir}/ocaml/lablgtk3-goocanvas2/*.cmxs

#-----------------------------------------------------------------
%package        goocanvas2-devel
Summary:        Development files for %{name}-goocanvas2
Group:          Development/OCaml
Requires:       %{name}-goocanvas2%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description    goocanvas2-devel
The %{name}-goocanvas2-devel package contains libraries and signature
files for developing applications that use %{name}-goocanvas2.

%files goocanvas2-devel
%{_libdir}/ocaml/lablgtk3-goocanvas2/*.a
%{_libdir}/ocaml/lablgtk3-goocanvas2/*.cmx
%{_libdir}/ocaml/lablgtk3-goocanvas2/*.cmxa
%{_libdir}/ocaml/lablgtk3-goocanvas2/*.cmt
%{_libdir}/ocaml/lablgtk3-goocanvas2/*.cmti
%{_libdir}/ocaml/lablgtk3-goocanvas2/*.mli
%{_libdir}/ocaml/lablgtk3-goocanvas2/dune-package
%{_libdir}/ocaml/lablgtk3-goocanvas2/opam

#-----------------------------------------------------------------
%package        gtkspell3
Summary:        OCaml interface to gtkspell3
Group:          Development/OCaml
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(gtkspell3-3.0)

%description    gtkspell3 %_description

This package contains OCaml bindings for gtkspell3.

%files gtkspell3
%{_libdir}/ocaml/stublibs/dlllablgtk3_gtkspell3_stubs.so
%{_libdir}/ocaml/lablgtk3-gtkspell3/META
%{_libdir}/ocaml/lablgtk3-gtkspell3/*.cma
%{_libdir}/ocaml/lablgtk3-gtkspell3/*.cmi
%{_libdir}/ocaml/lablgtk3-gtkspell3/*.cmxs

#-----------------------------------------------------------------
%package        gtkspell3-devel
Summary:        Development files for %{name}-gtkspell3
Group:          Development/OCaml
Requires:       %{name}-gtkspell3%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description    gtkspell3-devel
The %{name}-gtkspell3-devel package contains libraries and signature
files for developing applications that use %{name}-gtkspell3.

%files gtkspell3-devel
%{_libdir}/ocaml/lablgtk3-gtkspell3/*.a
%{_libdir}/ocaml/lablgtk3-gtkspell3/*.cmx
%{_libdir}/ocaml/lablgtk3-gtkspell3/*.cmxa
%{_libdir}/ocaml/lablgtk3-gtkspell3/*.cmt
%{_libdir}/ocaml/lablgtk3-gtkspell3/*.cmti
%{_libdir}/ocaml/lablgtk3-gtkspell3/*.mli
%{_libdir}/ocaml/lablgtk3-gtkspell3/dune-package
%{_libdir}/ocaml/lablgtk3-gtkspell3/opam

#-----------------------------------------------------------------
%package        sourceview3
Summary:        OCaml interface to gtksourceview3
Group:          Development/OCaml
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(gtksourceview-3.0)

%description    sourceview3 %_description

This package contains OCaml bindings for gtksourceview3.

%files sourceview3
%{_libdir}/ocaml/stublibs/dlllablgtk3_sourceview3_stubs.so
%{_libdir}/ocaml/lablgtk3-sourceview3/META
%{_libdir}/ocaml/lablgtk3-sourceview3/*.cma
%{_libdir}/ocaml/lablgtk3-sourceview3/*.cmi
%{_libdir}/ocaml/lablgtk3-sourceview3/*.cmxs

#-----------------------------------------------------------------
%package        sourceview3-devel
Summary:        Development files for %{name}-sourceview3
Group:          Development/OCaml
Requires:       %{name}-sourceview3%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description    sourceview3-devel
The %{name}-sourceview3-devel package contains libraries and signature
files for developing applications that use %{name}-sourceview3.

%files sourceview3-devel
%{_libdir}/ocaml/lablgtk3-sourceview3/*.a
%{_libdir}/ocaml/lablgtk3-sourceview3/*.cmx
%{_libdir}/ocaml/lablgtk3-sourceview3/*.cmxa
%{_libdir}/ocaml/lablgtk3-sourceview3/*.cmt
%{_libdir}/ocaml/lablgtk3-sourceview3/*.cmti
%{_libdir}/ocaml/lablgtk3-sourceview3/*.mli
%{_libdir}/ocaml/lablgtk3-sourceview3/dune-package
%{_libdir}/ocaml/lablgtk3-sourceview3/opam

#-----------------------------------------------------------------
%prep
%autosetup -n lablgtk-%{version} -p1

# This file is empty, so drop it before we make assemble the docs
rm doc/FAQ.text

# Make sure we do not use the bundled copy of xml-light
rm -fr tools/instrospection/xml-light

# This version number marker was removed in the 3.1.2 release, leading to no
# version number in the META files
sed -i '/(name lablgtk3)/a(version %{version})' dune-project

%build
export LABLGTK_EXTRA_FLAGS=-g
dune build

# Relink the stublibs with $RPM_LD_FLAGS.
pushd _build/default/src
ocamlmklib -g -ldopt '%{build_ldflags}' $(pkgconf --libs gtk+-3.0) \
  -o lablgtk3_stubs $(ar t liblablgtk3_stubs.a)
cd ../src-goocanvas2
ocamlmklib -g -ldopt '%{build_ldflags}' $(pkgconf --libs goocanvas-2.0) \
  -o lablgtk3_goocanvas2_stubs $(ar t liblablgtk3_goocanvas2_stubs.a)
cd ../src-gtkspell3
ocamlmklib -g -ldopt '%{build_ldflags}' $(pkgconf --libs gtkspell3-3.0) \
  -o lablgtk3_gtkspell3_stubs $(ar t liblablgtk3_gtkspell3_stubs.a)
cd ../src-sourceview3
ocamlmklib -g -ldopt '%{build_ldflags}' $(pkgconf --libs gtksourceview-3.0) \
  -o lablgtk3_sourceview3_stubs $(ar t liblablgtk3_sourceview3_stubs.a)
popd

# Make the man pages
HELP2MAN="-N --version-string=%{version}"
cd _build/install/default/bin
help2man $HELP2MAN -o ../../../../gdk_pixbuf_mlsource3.1 ./gdk_pixbuf_mlsource3
help2man $HELP2MAN -o ../../../../lablgladecc3.1 ./lablgladecc3
cd -

%install
dune install --destdir=%{buildroot}

# Install the man pages
mkdir -p %{buildroot}%{_mandir}/man1
cp -p gdk_pixbuf_mlsource3.1 lablgladecc3.1 %{buildroot}%{_mandir}/man1

# Remove files we do not need to package
rm %{buildroot}%{_libdir}/ocaml/*/*.ml

# This just contains the README, LICENSE, and CHANGES files, 3 times, in
# directories with names other than the ones we want.
rm -rf %{buildroot}%{_prefix}/doc

%check
dune runtest
