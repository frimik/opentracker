Name:           opentracker
Version:        0.3
Release:        1.20130826git%{?dist}
Summary:        An open and free bittorrent tracker.

#Group:          
License:        Beerware
URL:            https://github.com/frimik/opentracker
Source0:        opentracker-%{version}.tar.gz

BuildRequires:  libowfat-devel

%description
This is opentracker. An open bittorrent tracker.


%prep
%setup -q


%build
make


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} BINDIR="%{buildroot}/usr/bin"


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc
%attr(0755,-,-) %{_bindir}/%{name}



%changelog
* Mon Aug 26 2013 Mikael Fridh <mfridh@ea.com> 0.3-1.20130826git
- fii (mfridh@ea.com)
- spec file (mfridh@ea.com)

* Mon Aug 26 2013 Mikael Fridh <mfridh@ea.com> 0.2-1.20130826git
- new package built with tito

