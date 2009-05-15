%define module   GD-SecurityImage
%define version    1.70
%define release    %mkrel 2

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Security image (captcha) generator
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/GD/%{module}-%{version}.tar.gz
BuildRequires: perl-devel
BuildRequires: perl(GD)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
The (so called) _"Security Images"_ are so popular. Most internet software
use these in their registration screens to block robot programs (which may
register tons of fake member accounts). Security images are basicaly,
graphical *CAPTCHA*s (*C*ompletely *A*utomated *P*ublic *T*uring Test to
Tell *C*omputers and *H*umans *A*part). This module gives you a basic
interface to create such an image. The final output is the actual graphic
data, the mime type of the graphic and the created random string. The
module also has some _"styles"_ that are used to create the background (or
foreground) of the image.

If you are an 'Authen::Captcha' user, see the GD::SecurityImage::AC manpage
for migration from 'Authen::Captcha' to 'GD::SecurityImage'.

This module is *just an image generator*. Not a _captcha handler_. The
validation of the generated graphic is left to your programming taste. But
there are some _captcha handlers_ for several Perl FrameWorks. If you are
an user of one of these frameworks, see the /"GD::SecurityImage
Implementations" manpage in the /"SEE ALSO" manpage section for
information.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/GD

