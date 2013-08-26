Name:           opentracker
Version:        0.4.1
Release:        1%{?dist}
Summary:        An open and free bittorrent tracker.

#Group:          
License:        Beerware
URL:            https://github.com/frimik/opentracker
Source0:        opentracker-%{version}.tar.gz

BuildRequires:  libowfat-devel
BuildRequires:  zlib-devel

%description
This is opentracker. An open bittorrent tracker.


%prep
%setup -q


%build
make


%install
rm -rf %{buildroot}
install -d %{buildroot}%{_bindir}
make install DESTDIR=%{buildroot} BINDIR="%{buildroot}%{_bindir}"


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc
%attr(0755,-,-) %{_bindir}/%{name}



%changelog
* Mon Aug 26 2013 Mikael Fridh <mfridh@ea.com> 0.4.1-1
- build requires zlib-devel (mfridh@ea.com)
- RPM package of opentracker (mfridh@ea.com)

* Mon Aug 26 2013 Mikael Fridh <mfridh@ea.com>
- build requires zlib-devel (mfridh@ea.com)
- RPM package of opentracker (mfridh@ea.com)

* Mon Aug 26 2013 Mikael Fridh <mfridh@ea.com> 0.4-1
- no live sync (mfridh@ea.com)

* Mon Aug 26 2013 Mikael Fridh <mfridh@ea.com> 0.2-1.20130826git
- new package built with tito

