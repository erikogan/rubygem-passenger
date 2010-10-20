Summary: Alternatives aware nginx 
Name: nginx-alternatives
Version: 0.0.1
Release: 1%{?dist}
License: MIT
Group: System Environment/Daemons
#Source0: %{name}-%{version}.tar.gz
Source0: README.%{name}
Requires: nginx
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
This package puts the nginx webserver binary under the control of the
/etc/alternative system.

This package is meant to be obsoleted by a future nginx package (which
will provide the same feature)

%prep
#%setup -q

%build
cp %{SOURCE0} .

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ $1 == 1 ]; then
  mv /usr/sbin/nginx /usr/sbin/nginx.base
  /usr/sbin/alternatives --install /usr/sbin/nginx nginx /usr/sbin/nginx.base 30
fi

%postun
if [ $1 == 0 ]; then
  # Given that other packages will depend on this one, it's 99% likely
  # that this will have been reset back to base. Still good practice
  # to put the expected binary back in place.
  bin=`readlink -f /usr/sbin/nginx`
  /usr/sbin/alternatives --remove nginx /usr/sbin/nginx.base
  mv -f $bin /usr/sbin/nginx
fi

%files
%defattr(-,root,root,-)
%doc README.%{name}

%changelog
* Wed Oct 20 2010 Erik Ogan <erik@stealthymonkeys.com> - 0.0.1-1
- Initial build.

