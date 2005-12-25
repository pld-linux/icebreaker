Summary:	An addictive action-puzzle game involving bouncing penguins
Summary(pl):	Wci±gaj±ca gra zrêczno¶ciowo-³amig³ówkowa z pingwinkami
Name:		icebreaker
Version:	1.2.1
Release:	1
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://www.mattdm.org/icebreaker/1.2.x/%{name}-%{version}.tgz
# Source0-md5:	9453119cf3342a8828e4805c0c49be50
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://www.mattdm.org/icebreaker/
BuildRequires:	SDL_mixer-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
So, uh, there's a bunch of penguins on an iceberg in Antarctica. You
have been selected to catch them so they can be shipped to Finland,
where they are essential to a secret plot for world domination.

%description -l pl
Hmm... jest ca³a masa pingwinów na górze lodowej na Antarktyce.
Zosta³e¶ wybrany, aby je z³apaæ, ¿eby mog³y zostaæ dostarczone do
Finlandii, gdzie s± nieodzowne dla tajnego spisku maj±cego na celu
dominacjê nad ¶wiatem.

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

install *.wav *.bmp $RPM_BUILD_ROOT%{_datadir}/icebreaker
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}
install icebreaker $RPM_BUILD_ROOT%{_bindir}

touch $RPM_BUILD_ROOT/var/games/icebreaker.scores

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%attr(2755,root,games) %{_bindir}/*
%{_desktopdir}/*
%{_pixmapsdir}/*
%{_datadir}/icebreaker
%attr(664,root,games) %config(noreplace) %verify(not md5 mtime size) /var/games/icebreaker.scores
