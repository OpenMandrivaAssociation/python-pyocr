Summary:	A Python wrapper for OCR engines (Tesseract, Cuneiform, etc)
Name:		python-pyocr
Version:	0.8.5
Release:	1
License:	GPL-3.0-or-later
Group:		Development/Python
Source0:	https://pipy.org/project/packages/source/p/pyocr/pyocr-%{version}.tar.gz
URL:		https://pypi.org/project/pyocr/
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
A Python wrapper for OCR engines (Tesseract, Cuneiform, etc).

%files
%{py_sitedir}/pyocr
%{py_sitedir}/pyocr-*.*-info

#----------------------------------------------------------------------

%prep
%autosetup -p1 -n pyocr-%{version}

%build
%py_build

%install
%py_install

