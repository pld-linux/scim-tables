# TODO: skim support (skim-devel >= 1.2.1)
#
# Conditional build:
%bcond_without	indic_tables	# don't build Indic tables
%bcond_without	ja_tables	# don't build Japanese tables
%bcond_without	ko_tables	# don't build Korean tables
#
Summary:	SCIM Generic Table IMEngine
Summary(pl.UTF-8):	Silnik IM Generic Table dla platformy SCIM
Name:		scim-tables
Version:	0.5.14.1
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/scim/%{name}-%{version}.tar.gz
# Source0-md5:	c2bb5f79c381cefb656ac8c8b3dc5b53
Source1:	CangJie5.png
# http://www.chinesecj.com/newsoftware/index3.php?Type=1
Source2:	CangJie5.txt.in
Patch0:		%{name}-rhbz217639.patch
Patch1:		%{name}-rhbz232860.patch
URL:		http://sourceforge.net/projects/scim/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gettext-tools >= 0.14
BuildRequires:	gtk+2-devel
BuildRequires:	intltool >= 0.33
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	pkgconfig
BuildRequires:	scim-devel >= 1.4.9
Requires:	scim >= 1.4.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the Generic Table IMEngine for SCIM.

%description -l pl.UTF-8
Ten pakiet zawiera silnik IM Generic Table (ogólny silnik oparty na
tablicach) dla platformy wprowadzania SCIM.

%package amharic
Summary:	SCIM tables for Amharic
Summary(pl.UTF-8):	Tablice SCIM dla języka amharskiego
Group:		Libraries
Requires:	scim-tables = %{version}-%{release}

%description amharic
This package contains scim-tables files for Amharic input.

%description amharic -l pl.UTF-8
Ten pakiet zawiera pliki scim-tables do wprowadzania tekstu w języku
amharskim.

%package arabic
Summary:	SCIM tables for Arabic
Summary(pl.UTF-8):	Tablice SCIM dla języka arabskiego
Group:		Libraries
Requires:	scim-tables = %{version}-%{release}

%description arabic
This package contains scim-tables files for Arabic input.

%description arabic -l pl.UTF-8
Ten pakiet zawiera pliki scim-tables do wprowadzania tekstu w języku
arabskim.

%package bengali
Summary:	SCIM tables for Bengali
Summary(pl.UTF-8):	Tablice SCIM dla języka bengalskiego
Group:		Libraries
Requires:	scim-tables = %{version}-%{release}

%description bengali
This package contains scim-tables files for Bengali input.

%description bengali -l pl.UTF-8
Ten pakiet zawiera pliki scim-tables do wprowadzania tekstu w języku
bengalskim.

%package chinese
Summary:	SCIM tables for Chinese
Summary(pl.UTF-8):	Tablice SCIM dla języka chińskiego
Group:		Libraries
Requires:	scim-tables = %{version}-%{release}

%description chinese
This package contains scim-tables files for Chinese input.

%description chinese -l pl.UTF-8
Ten pakiet zawiera pliki scim-tables do wprowadzania tekstu w języku
chińskim.

%package chinese-extra
Summary:	Additional SCIM tables for Chinese
Summary(pl.UTF-8):	Dodatkowe tablice SCIM dla języka chińskiego
Group:		Libraries
Requires:	scim-tables = %{version}-%{release}

%description chinese-extra
This package contains additional less used scim-tables files for
Chinese input.

%description chinese-extra -l pl.UTF-8
Ten pakiet zawiera rzadziej używane pliki scim-tables do wprowadzania
tekstu w języku chińskim.

%package greek
Summary:	SCIM tables for Greek Polytonic
Summary(pl.UTF-8):	Tablice SCIM dla języka greckieto w systemie politonicznym
Group:		Libraries
Requires:	scim-tables = %{version}-%{release}

%description greek
This package contains scim-tables files for Greek Polytonic input.

%description greek -l pl.UTF-8
Ten pakiet zawiera pliki scim-tables do wprowadzania tekstu w języku
greckim w systemie politonicznym.

%package gujarati
Summary:	SCIM tables for Gujarati
Summary(pl.UTF-8):	Tablice SCIM dla języka gudźarati
Group:		Libraries
Requires:	scim-tables = %{version}-%{release}

%description gujarati
This package contains scim-tables files for Gujarati input.

%description gujarati -l pl.UTF-8
Ten pakiet zawiera pliki scim-tables do wprowadzania tekstu w języku
gudźarati.

%package hebrew
Summary:	SCIM tables for Hebrew
Summary(pl.UTF-8):	Tablice SCIM dla języka hebrajskiego
Group:		Libraries
Requires:	scim-tables = %{version}-%{release}

%description hebrew
This package contains scim-tables files for Hebrew input.

%description hebrew -l pl.UTF-8
Ten pakiet zawiera pliki scim-tables do wprowadzania tekstu w języku
hebrajskim.

%package hindi
Summary:	SCIM tables for Hindi
Summary(pl.UTF-8):	Tablice SCIM dla języka hindi
Group:		Libraries
Requires:	scim-tables = %{version}-%{release}

%description hindi
This package contains scim-tables files for Hindi input.

%description hindi -l pl.UTF-8
Ten pakiet zawiera pliki scim-tables do wprowadzania tekstu w języku
hindi.

%package japanese
Summary:	SCIM tables for Japanese
Summary(pl.UTF-8):	Tablice SCIM dla języka japońskiego
Group:		Libraries
Requires:	scim-tables = %{version}-%{release}

%description japanese
This package contains scim-tables files for Japanese.

%description japanese -l pl.UTF-8
Ten pakiet zawiera pliki scim-tables do wprowadzania tekstu w języku
japońskim.

%package kannada
Summary:	SCIM tables for Kannada
Summary(pl.UTF-8):	Tablice SCIM dla języka kannada
Group:		Libraries
Requires:	scim-tables = %{version}-%{release}

%description kannada
This package contains scim-tables files for Kannada input.

%description kannada -l pl.UTF-8
Ten pakiet zawiera pliki scim-tables do wprowadzania tekstu w języku
kannada.

%package korean
Summary:	SCIM tables for Korean
Summary(pl.UTF-8):	Tablice SCIM dla języka koreańskiego
Group:		Libraries
Requires:	scim-tables = %{version}-%{release}

%description korean
This package contains scim-tables files for Korean.

%description korean -l pl.UTF-8
Ten pakiet zawiera pliki scim-tables do wprowadzania tekstu w języku
koreańskim.

%package malayalam
Summary:	SCIM tables for Malayalam scripts
Summary(pl.UTF-8):	Tablice SCIM dla języka malajalam
Group:		Libraries
Requires:	scim-tables = %{version}-%{release}

%description malayalam
This package contains scim-tables files for Malayalam languages.

%description malayalam -l pl.UTF-8
Ten pakiet zawiera pliki scim-tables do wprowadzania tekstu w języku
malajalam.

%package marathi
Summary:	SCIM tables for Marathi
Summary(pl.UTF-8):	Tablice SCIM dla języka marathi
Group:		Libraries
Requires:	scim-tables = %{version}-%{release}

%description marathi
This package contains scim-tables files for Marathi languages.

%description marathi -l pl.UTF-8
Ten pakiet zawiera pliki scim-tables do wprowadzania tekstu w języku
marathi.

%package nepali
Summary:	SCIM tables for Nepali
Summary(pl.UTF-8):	Tablice SCIM dla języka nepalskiego
Group:		Libraries
Requires:	scim-tables = %{version}-%{release}

%description nepali
This package contains scim-tables files for Nepali input.

%description nepali -l pl.UTF-8
Ten pakiet zawiera pliki scim-tables do wprowadzania tekstu w języku
nepalskim.

%package punjabi
Summary:	SCIM tables for Punjabi
Summary(pl.UTF-8):	Tablice SCIM dla języka pendżabskiego
Group:		Libraries
Requires:	scim-tables = %{version}-%{release}

%description punjabi
This package contains scim-tables files for Punjabi input.

%description punjabi -l pl.UTF-8
Ten pakiet zawiera pliki scim-tables do wprowadzania tekstu w języku
pendżabskim.

%package russian
Summary:	SCIM tables for Russian
Summary(pl.UTF-8):	Tablice SCIM dla języka rosyjskiego
Group:		Libraries
Requires:	scim-tables = %{version}-%{release}

%description russian
This package contains scim-tables files for Russian input.

%description russian -l pl.UTF-8
Ten pakiet zawiera pliki scim-tables do wprowadzania tekstu w języku
rosyjskim.

%package tamil
Summary:	SCIM tables for Tamil
Summary(pl.UTF-8):	Tablice SCIM dla języka tamilskiego
Group:		Libraries
Requires:	scim-tables = %{version}-%{release}

%description tamil
This package contains scim-tables files for Tamil input.

%description tamil -l pl.UTF-8
Ten pakiet zawiera pliki scim-tables do wprowadzania tekstu w języku
tamilskim.

%package thai
Summary:	SCIM tables for Thai
Summary(pl.UTF-8):	Tablice SCIM dla języka tajskiego
Group:		Libraries
Requires:	scim-tables = %{version}-%{release}

%description thai
This package contains scim-tables files for Thai input.

%description thai -l pl.UTF-8
Ten pakiet zawiera pliki scim-tables do wprowadzania tekstu w języku
tajskim.

%package telugu
Summary:	SCIM tables for Telugu
Summary(pl.UTF-8):	Tablice SCIM dla języka telugu
Group:		Libraries
Requires:	scim-tables = %{version}-%{release}

%description telugu
This package contains scim-tables files for Telugu input.

%description telugu -l pl.UTF-8
Ten pakiet zawiera pliki scim-tables do wprowadzania tekstu w języku
telugu.

%package ukrainian
Summary:	SCIM tables for Ukrainian
Summary(pl.UTF-8):	Tablice SCIM dla języka ukraińskiego
Group:		Libraries
Requires:	scim-tables = %{version}-%{release}

%description ukrainian
This package contains scim-tables files for Ukrainian input.

%description ukrainian -l pl.UTF-8
Ten pakiet zawiera pliki scim-tables do wprowadzania tekstu w języku
ukraińskim.

%package uyghur
Summary:	SCIM tables for Uyghur
Summary(pl.UTF-8):	Tablice SCIM dla języka ujgurskiego
Group:		Libraries
Requires:	scim-tables = %{version}-%{release}

%description uyghur
This package contains scim-tables files for Uyghur input.

%description uyghur -l pl.UTF-8
Ten pakiet zawiera pliki scim-tables do wprowadzania tekstu w języku
ujgurskim.

%package vietnamese
Summary:	SCIM tables for Vietnamese
Summary(pl.UTF-8):	Tablice SCIM dla języka wietnamskiego
Group:		Libraries
Requires:	scim-tables = %{version}-%{release}

%description vietnamese
This package contains scim-tables files for Vietnamese input.

%description vietnamese -l pl.UTF-8
Ten pakiet zawiera pliki scim-tables do wprowadzania tekstu w języku
wietnamskim.

%package additional
Summary:	Other miscellaneous SCIM tables
Summary(pl.UTF-8):	Dodatkowe różne tablice SCIM
Group:		Libraries
Requires:	scim-tables = %{version}-%{release}

%description additional
This package contains some miscellaneous scim-tables.

%description additional -l pl.UTF-8
Ten pakiet zawiera różne pliki dla scim-tables.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

%{__cp} -f %{SOURCE2} tables/zh/

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__install} %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/scim/icons

%{!?with_indic_tables:%{__rm} $RPM_BUILD_ROOT%{_datadir}/scim/{icons,tables}/{Bengali,Gujarati,Hindi,Kannada,Malayalam,Marathi,Punjabi,Tamil,Telugu}-*}
%{!?with_ja_tables:%{__rm} $RPM_BUILD_ROOT%{_datadir}/scim/{icons,tables}/{HIRAGANA,KATAKANA,Nippon}*}
%{!?with_ko_tables:%{__rm} $RPM_BUILD_ROOT%{_datadir}/scim/{icons,tables}/{Hangul,Hanja}*}

%{__rm} $RPM_BUILD_ROOT%{_libdir}/scim-1.0/*/*/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/scim-make-table
%attr(755,root,root) %{_libdir}/scim-1.0/*/IMEngine/table.so
%attr(755,root,root) %{_libdir}/scim-1.0/*/SetupUI/table-imengine-setup.so
%{_datadir}/scim/icons/table.png
%dir %{_datadir}/scim/tables
%{_mandir}/man1/scim-make-table.1*

%files amharic
%defattr(644,root,root,755)
%{_datadir}/scim/tables/Amharic.bin
%{_datadir}/scim/icons/Amharic.png

%files arabic
%defattr(644,root,root,755)
%{_datadir}/scim/tables/Arabic.bin
%{_datadir}/scim/icons/Arabic.png

%files chinese
%defattr(644,root,root,755)
%doc tables/zh/README-CangJie.txt
%{_datadir}/scim/icons/Array30.png
%{_datadir}/scim/icons/CangJie3.png
%{_datadir}/scim/icons/CangJie5.png
%{_datadir}/scim/icons/CantonHK.png
%{_datadir}/scim/icons/Quick.png
%{_datadir}/scim/icons/SmartCangJie6.png
%{_datadir}/scim/icons/Wubi.png
%{_datadir}/scim/icons/ZhuYin.png
%{_datadir}/scim/tables/Array30.bin
%{_datadir}/scim/tables/CangJie3.bin
%{_datadir}/scim/tables/CangJie5.bin
%{_datadir}/scim/tables/CantonHK.bin
%{_datadir}/scim/tables/Quick.bin
%{_datadir}/scim/tables/SmartCangJie6.bin
%{_datadir}/scim/tables/Wubi.bin
%{_datadir}/scim/tables/ZhuYin.bin

%files chinese-extra
%defattr(644,root,root,755)
%doc tables/zh/README-{Erbi,Wu}.txt
%{_datadir}/scim/icons/CNS11643.png
%{_datadir}/scim/icons/CangJie.png
%{_datadir}/scim/icons/Cantonese.png
%{_datadir}/scim/icons/Dayi.png
%{_datadir}/scim/icons/EZ.png
%{_datadir}/scim/icons/Erbi.png
%{_datadir}/scim/icons/Erbi-QS.png
%{_datadir}/scim/icons/Jyutping.png
%{_datadir}/scim/icons/Simplex.png
%{_datadir}/scim/icons/Stroke5.png
%{_datadir}/scim/icons/Wu.png
%{_datadir}/scim/icons/Ziranma.png
%{_datadir}/scim/tables/CNS11643.bin
%{_datadir}/scim/tables/CangJie.bin
%{_datadir}/scim/tables/Cantonese.bin
%{_datadir}/scim/tables/Dayi3.bin
%{_datadir}/scim/tables/EZ-Big.bin
%{_datadir}/scim/tables/Erbi.bin
%{_datadir}/scim/tables/Erbi-QS.bin
%{_datadir}/scim/tables/Jyutping.bin
%{_datadir}/scim/tables/Simplex.bin
%{_datadir}/scim/tables/Stroke5.bin
%{_datadir}/scim/tables/Wu.bin
%{_datadir}/scim/tables/ZhuYin-Big.bin
%{_datadir}/scim/tables/Ziranma.bin

%files greek
%defattr(644,root,root,755)
%{_datadir}/scim/tables/greekpoly.bin

%files hebrew
%defattr(644,root,root,755)
%{_datadir}/scim/icons/HebrewComputer.png
%{_datadir}/scim/tables/HebrewComputer.bin
%{_datadir}/scim/tables/classicalhebrew.bin

%files nepali
%defattr(644,root,root,755)
%{_datadir}/scim/tables/Nepali_*.bin
%{_datadir}/scim/icons/Nepali.png

%files russian
%defattr(644,root,root,755)
%{_datadir}/scim/icons/Translit.png
%{_datadir}/scim/icons/RussianComputer.png
%{_datadir}/scim/icons/RussianTraditional.png
%{_datadir}/scim/icons/Yawerty.png
%{_datadir}/scim/tables/RussianComputer.bin
%{_datadir}/scim/tables/RussianTraditional.bin
%{_datadir}/scim/tables/Yawerty.bin
%{_datadir}/scim/tables/Translit.bin

%files thai
%defattr(644,root,root,755)
%{_datadir}/scim/icons/Thai.png
%{_datadir}/scim/tables/Thai.bin

%files ukrainian
%defattr(644,root,root,755)
%{_datadir}/scim/icons/Ukrainian-Translit.png
%{_datadir}/scim/tables/Ukrainian-Translit.bin

%files uyghur
%defattr(644,root,root,755)
%{_datadir}/scim/icons/Uyghur.png
%{_datadir}/scim/tables/Uyghur-Romanized.bin
%{_datadir}/scim/tables/Uyghur-Standard.bin

%files vietnamese
%defattr(644,root,root,755)
%{_datadir}/scim/icons/Viqr.png
%{_datadir}/scim/tables/Viqr.bin

%files additional
%defattr(644,root,root,755)
%{_datadir}/scim/icons/IPA-X-SAMPA.png
%{_datadir}/scim/icons/LaTeX.png
%{_datadir}/scim/tables/IPA-Kirshenbaum.bin
%{_datadir}/scim/tables/IPA-X-SAMPA.bin
%{_datadir}/scim/tables/LaTeX.bin

%if %{with indic_tables}
%files bengali
%defattr(644,root,root,755)
%{_datadir}/scim/icons/Bengali-inscript.png
%{_datadir}/scim/icons/Bengali-probhat.png
%{_datadir}/scim/tables/Bengali-inscript.bin
%{_datadir}/scim/tables/Bengali-probhat.bin

%files gujarati
%defattr(644,root,root,755)
%{_datadir}/scim/icons/Gujarati-inscript.png
%{_datadir}/scim/icons/Gujarati-phonetic.png
%{_datadir}/scim/tables/Gujarati-inscript.bin
%{_datadir}/scim/tables/Gujarati-phonetic.bin

%files hindi
%defattr(644,root,root,755)
%{_datadir}/scim/icons/Hindi-inscript.png
%{_datadir}/scim/icons/Hindi-phonetic.png
%{_datadir}/scim/icons/Hindi-remington.png
%{_datadir}/scim/tables/Hindi-inscript.bin
%{_datadir}/scim/tables/Hindi-phonetic.bin
%{_datadir}/scim/tables/Hindi-remington.bin

%files kannada
%defattr(644,root,root,755)
%{_datadir}/scim/icons/Kannada-inscript.png
%{_datadir}/scim/icons/Kannada-kgp.png
%{_datadir}/scim/tables/Kannada-inscript.bin
%{_datadir}/scim/tables/Kannada-kgp.bin

%files malayalam
%defattr(644,root,root,755)
%{_datadir}/scim/icons/Malayalam-inscript.png
%{_datadir}/scim/icons/Malayalam-phonetic.png
%{_datadir}/scim/tables/Malayalam-inscript.bin
%{_datadir}/scim/tables/Malayalam-phonetic.bin

%files marathi
%defattr(644,root,root,755)
%{_datadir}/scim/icons/Marathi-remington.png
%{_datadir}/scim/tables/Marathi-remington.bin

%files punjabi
%defattr(644,root,root,755)
%{_datadir}/scim/icons/Punjabi-inscript.png
%{_datadir}/scim/icons/Punjabi-jhelum.png
%{_datadir}/scim/icons/Punjabi-phonetic.png
%{_datadir}/scim/icons/Punjabi-remington.png
%{_datadir}/scim/tables/Punjabi-inscript.bin
%{_datadir}/scim/tables/Punjabi-jhelum.bin
%{_datadir}/scim/tables/Punjabi-phonetic.bin
%{_datadir}/scim/tables/Punjabi-remington.bin

%files tamil
%defattr(644,root,root,755)
%{_datadir}/scim/icons/Tamil-inscript.png
%{_datadir}/scim/icons/Tamil-phonetic.png
%{_datadir}/scim/icons/Tamil-remington.png
%{_datadir}/scim/icons/Tamil-tamil99.png
%{_datadir}/scim/tables/Tamil-inscript.bin
%{_datadir}/scim/tables/Tamil-phonetic.bin
%{_datadir}/scim/tables/Tamil-remington.bin
%{_datadir}/scim/tables/Tamil-tamil99.bin

%files telugu
%defattr(644,root,root,755)
%{_datadir}/scim/icons/Telugu-inscript.png
%{_datadir}/scim/tables/Telugu-inscript.bin
%endif

%if %{with ja_tables}
%files japanese
%defattr(644,root,root,755)
%doc tables/ja/kanjidic*
%{_datadir}/scim/icons/HIRAGANA.png
%{_datadir}/scim/icons/KATAKANA.png
%{_datadir}/scim/icons/Nippon.png
%{_datadir}/scim/tables/HIRAGANA.bin
%{_datadir}/scim/tables/KATAKANA.bin
%{_datadir}/scim/tables/Nippon.bin
%endif

%if %{with ko_tables}
%files korean
%defattr(644,root,root,755)
%{_datadir}/scim/icons/Hangul.png
%{_datadir}/scim/icons/Hanja.png
%{_datadir}/scim/tables/Hangul.bin
%{_datadir}/scim/tables/HangulRomaja.bin
%{_datadir}/scim/tables/Hanja.bin
%endif
