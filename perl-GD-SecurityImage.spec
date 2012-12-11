%define upstream_name    GD-SecurityImage
%define upstream_version 1.70

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Security image (captcha) generator
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/GD/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(GD)
BuildArch:	noarch

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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/GD

%changelog
* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 1.700.0-1mdv2010.0
+ Revision: 401659
- rebuild using %%perl_convert_version
- fixed license field

* Fri May 15 2009 Jérôme Quelin <jquelin@mandriva.org> 1.70-2mdv2010.0
+ Revision: 375950
- rebuild

* Fri May 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.70-1mdv2010.0
+ Revision: 370124
- update to new version 1.70

* Tue Mar 17 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.66-1mdv2009.1
+ Revision: 356304
- import perl-GD-SecurityImage


* Tue Mar 17 2009 cpan2dist 1.66-1mdv
- initial mdv release, generated with cpan2dist

