%global packname  ggplot2
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          0.8.9
Release:          1
Summary:          An implementation of the Grammar of Graphics
Group:            Sciences/Mathematics
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildArch:        noarch
Requires:         R-core
Requires:         R-reshape R-grid R-proto 
Requires:         R-plyr R-splines R-MASS R-RColorBrewer R-digest R-colorspace 
Requires:         R-quantreg R-Hmisc R-mapproj R-maps R-hexbin R-gpclib R-maptools 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-reshape R-grid R-proto
BuildRequires:    R-plyr R-splines R-MASS R-RColorBrewer R-digest R-colorspace 
BuildRequires:    R-quantreg R-Hmisc R-mapproj R-maps R-hexbin R-gpclib R-maptools 

%description
An implementation of the grammar of graphics in R. It combines the
advantages of both base and lattice graphics: conditioning and shared axes
are handled automatically, and you can still build up a plot step by step
from multiple data sources. It also implements a sophisticated
multidimensional conditioning system and a consistent interface to map
data to aesthetic attributes. See the ggplot2 website for more
information, documentation and examples.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
