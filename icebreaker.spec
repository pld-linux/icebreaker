Summary:	An addictive action-puzzle game involving bouncing penguins
Summary(pl):	Wci�gaj�ca gra zr�czno�ciowo-�amig��wkowa z pingwinkami
Name:		icebreaker
Version:	1.09
Release:	1
License:	GPL
Group:		X11/Applications/Games
Group(de):	X11/Applikationen/Spiele
Group(pl):	X11/Aplikacje/Gry
Source0:	http://www.mattdm.org/icebreaker/%{name}-%{version}.tgz
Source1:	%{name}.desktop
Source2:	%{name}.xpm
URL:		http://www.mattdm.org/icebreaker/
BuildRequires:	SDL-devel
BuildRequires:	SDL_mixer-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
So, uh, there's a bunch of penguins on an iceberg in Antarctica. You
have been selected to catch them so they can be shipped to Finland,
where they are essential to a secret plot for world domination.

%description -l pl
Hmm... jest ca�a masa pingwin�w na g�rze lodowej na Antarktyce.
Zosta�e� wybrany, aby je z�apa�, �eby mog�y zosta� dostarczone do
Finlandii, gdzie s� nieodzowne dla tajnego spisku maj�cego na celu
dominacj� �wiata.

%prep
%setup -q

%build
%{__make} CFLAGS="%{rpmcflags} `sdl-config --cflags` \
             -DDATAPREFIX=\\\"%{_datadir}/icebreaker\\\"\
	     -DHISCOREPREFIX=\\\"/var/games\\\"" \
     LDFLAGS="`sdl-config --libs`"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/icebreaker,/var/games}
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_applnkdir}/Games}

install *.wav *.bmp $RPM_BUILD_ROOT%{_datadir}/icebreaker
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}
install icebreaker $RPM_BUILD_ROOT%{_bindir}
touch $RPM_BUILD_ROOT/var/games/icebreaker.scores

gzip -9nf ChangeLog README TODO 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(2755,root,games) %{_bindir}/*
%{_applnkdir}/Games/*
%{_pixmapsdir}/*
%{_datadir}/icebreaker
%attr(664,root,games) %config(noreplace) %verify(not size mtime md5) /var/games/icebreaker.scores
