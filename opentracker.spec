Name:           opentracker
Version:        0.2
Release:        1.20130826git%{?dist}
Summary:        An open and free bittorrent tracker.

#Group:          
License:        Beerware
URL:            https://github.com/frimik/opentracker
Source0:        opentracker-0.1-0.1.20130826git.tar.gz

BuildRequires:  libowfat-devel

%description
This is opentracker. An open bittorrent tracker.


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc



%changelog
* Mon Aug 26 2013 Mikael Fridh <mfridh@ea.com> 0.2-1.20130826git
- new package built with tito

