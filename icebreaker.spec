Summary:	An addictive action-puzzle game involving bouncing penguins
Summary(pl.UTF-8):	Wciągająca gra zręcznościowo-łamigłówkowa z pingwinkami
Name:		icebreaker
Version:	1.9.8
Release:	2
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://www.mattdm.org/icebreaker/1.9.x/%{name}-%{version}.tgz
# Source0-md5:	34fee91bc647a64eec6756eb5602aef8
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://www.mattdm.org/icebreaker/
BuildRequires:	SDL_mixer-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
So, uh, there's a bunch of penguins on an iceberg in Antarctica. You
have been selected to catch them so they can be shipped to Finland,
where they are essential to a secret plot for world domination.

%description -l pl.UTF-8
Hmm... jest cała masa pingwinów na górze lodowej na Antarktyce.
Zostałeś wybrany, aby je złapać, żeby mogły zostać dostarczone do
Finlandii, gdzie są nieodzowne dla tajnego spisku mającego na celu
dominację nad światem.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} `sdl-config --cflags` \
		-DDATAPREFIX=\\\"%{_datadir}/icebreaker\\\"\
		-DHISCOREPREFIX=\\\"/var/games\\\"" \
	LDFLAGS="`sdl-config --libs`"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/icebreaker,/var/games} \
	$RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

install *.wav *.bmp *.ibt $RPM_BUILD_ROOT%{_datadir}/icebreaker
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}
install icebreaker $RPM_BUILD_ROOT%{_bindir}

touch $RPM_BUILD_ROOT/var/games/icebreaker.scores

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README README.themes TODO
%attr(2755,root,games) %{_bindir}/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
%{_datadir}/icebreaker
%attr(664,root,games) %config(noreplace) %verify(not md5 mtime size) /var/games/icebreaker.scores
