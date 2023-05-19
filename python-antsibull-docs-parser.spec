# Copyright 2023 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

Name: python-antsibull-docs-parser
Epoch: 100
Version: 1.0.0
Release: 1%{?dist}
BuildArch: noarch
Summary: Python library for processing Ansible documentation markup
License: GPL-3.0-or-later
URL: https://github.com/ansible-community/antsibull-docs-parser/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
This is a Python library for processing Ansible documentation markup. It
is named after antsibull-docs where this code originates from. It was
moved out to make it easier to reuse the markup code in other projects
without having to depend on all of antsibull-docs's dependencies.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-antsibull-docs-parser
Summary: Python library for processing Ansible documentation markup
Requires: python3
Provides: python3-antsibull-docs-parser = %{epoch}:%{version}-%{release}
Provides: python3dist(antsibull-docs-parser) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-antsibull-docs-parser = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(antsibull-docs-parser) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-antsibull-docs-parser = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(antsibull-docs-parser) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-antsibull-docs-parser
This is a Python library for processing Ansible documentation markup. It
is named after antsibull-docs where this code originates from. It was
moved out to make it easier to reuse the markup code in other projects
without having to depend on all of antsibull-docs's dependencies.

%files -n python%{python3_version_nodots}-antsibull-docs-parser
%license LICENSE
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-antsibull-docs-parser
Summary: Python library for processing Ansible documentation markup
Requires: python3
Provides: python3-antsibull-docs-parser = %{epoch}:%{version}-%{release}
Provides: python3dist(antsibull-docs-parser) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-antsibull-docs-parser = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(antsibull-docs-parser) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-antsibull-docs-parser = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(antsibull-docs-parser) = %{epoch}:%{version}-%{release}

%description -n python3-antsibull-docs-parser
This is a Python library for processing Ansible documentation markup. It
is named after antsibull-docs where this code originates from. It was
moved out to make it easier to reuse the markup code in other projects
without having to depend on all of antsibull-docs's dependencies.

%files -n python3-antsibull-docs-parser
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-antsibull-docs-parser
Summary: Python library for processing Ansible documentation markup
Requires: python3
Provides: python3-antsibull-docs-parser = %{epoch}:%{version}-%{release}
Provides: python3dist(antsibull-docs-parser) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-antsibull-docs-parser = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(antsibull-docs-parser) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-antsibull-docs-parser = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(antsibull-docs-parser) = %{epoch}:%{version}-%{release}

%description -n python3-antsibull-docs-parser
This is a Python library for processing Ansible documentation markup. It
is named after antsibull-docs where this code originates from. It was
moved out to make it easier to reuse the markup code in other projects
without having to depend on all of antsibull-docs's dependencies.

%files -n python3-antsibull-docs-parser
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
