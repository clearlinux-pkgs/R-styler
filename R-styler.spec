#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-styler
Version  : 1.1.0
Release  : 8
URL      : https://cran.r-project.org/src/contrib/styler_1.1.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/styler_1.1.0.tar.gz
Summary  : Non-Invasive Pretty Printing of R Code
Group    : Development/Tools
License  : GPL-3.0
Requires: R-backports
Requires: R-cli
Requires: R-dplyr
Requires: R-purrr
Requires: R-rematch2
Requires: R-rprojroot
Requires: R-tibble
Requires: R-withr
Requires: R-xfun
BuildRequires : R-backports
BuildRequires : R-cli
BuildRequires : R-dplyr
BuildRequires : R-purrr
BuildRequires : R-rematch2
BuildRequires : R-rprojroot
BuildRequires : R-tibble
BuildRequires : R-withr
BuildRequires : R-xfun
BuildRequires : buildreq-R

%description
user's formatting intent.

%prep
%setup -q -c -n styler

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1542842080

%install
export SOURCE_DATE_EPOCH=1542842080
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library styler
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library styler
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library styler
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library styler|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/styler/DESCRIPTION
/usr/lib64/R/library/styler/INDEX
/usr/lib64/R/library/styler/Meta/Rd.rds
/usr/lib64/R/library/styler/Meta/features.rds
/usr/lib64/R/library/styler/Meta/hsearch.rds
/usr/lib64/R/library/styler/Meta/links.rds
/usr/lib64/R/library/styler/Meta/nsInfo.rds
/usr/lib64/R/library/styler/Meta/package.rds
/usr/lib64/R/library/styler/Meta/vignette.rds
/usr/lib64/R/library/styler/NAMESPACE
/usr/lib64/R/library/styler/NEWS.md
/usr/lib64/R/library/styler/R/styler
/usr/lib64/R/library/styler/R/styler.rdb
/usr/lib64/R/library/styler/R/styler.rdx
/usr/lib64/R/library/styler/doc/customizing_styler.R
/usr/lib64/R/library/styler/doc/customizing_styler.Rmd
/usr/lib64/R/library/styler/doc/customizing_styler.html
/usr/lib64/R/library/styler/doc/index.html
/usr/lib64/R/library/styler/doc/introducing_styler.R
/usr/lib64/R/library/styler/doc/introducing_styler.Rmd
/usr/lib64/R/library/styler/doc/introducing_styler.html
/usr/lib64/R/library/styler/doc/performance_improvements.R
/usr/lib64/R/library/styler/doc/performance_improvements.Rmd
/usr/lib64/R/library/styler/doc/performance_improvements.html
/usr/lib64/R/library/styler/help/AnIndex
/usr/lib64/R/library/styler/help/aliases.rds
/usr/lib64/R/library/styler/help/paths.rds
/usr/lib64/R/library/styler/help/styler.rdb
/usr/lib64/R/library/styler/help/styler.rdx
/usr/lib64/R/library/styler/html/00Index.html
/usr/lib64/R/library/styler/html/R.css
/usr/lib64/R/library/styler/rstudio/addins.dcf
