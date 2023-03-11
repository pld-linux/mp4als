Summary:	MPEG-4 Audio Lossless Coding - RM23
Summary(pl.UTF-8):	Kodek MPEG-4 Audio Lossless Coding - RM23
Name:		mp4als
Version:	RM23
%define	gitref	b61dd140febf3ccd31d3aa5ecedbb273e5c1e6bf
Release:	1
License:	MPEG-4 Audio
Group:		Applications/Sound
Source0:	https://github.com/kojima-r/mp4alsRM23/archive/%{gitref}/%{name}-%{gitref}.tar.gz
# Source0-md5:	7f2db05f3efa4bdad7e07a47dfc2f4fe
URL:		https://github.com/kojima-r/mp4alsRM23
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MPEG-4 Audio Lossless Coding - RM23.

%description -l pl.UTF-8
Kodek MPEG-4 Audio Lossless Coding - RM23.

%prep
%setup -q -n %{name}%{version}-%{gitref}

head -n 25 src/mp4als.cpp > license.txt

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{rpmcppflags} %{!?debug:-DNDEBUG} -DWARN_BUFFERSIZEDB_OVER_24BIT -DPERMIT_SAMPLERATE_OVER_16BIT -fno-strict-aliasing"

%install
rm -rf $RPM_BUILD_ROOT

install -D bin/linux/mp4alsRM23 $RPM_BUILD_ROOT%{_bindir}/mp4als

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc license.txt readme.txt
%attr(755,root,root) %{_bindir}/mp4als
