#
# Conditional build:
%bcond_with	indic_tables		# don't build Indic tables
%bcond_with	jp_tables		# don't build Japanese tables
%bcond_with	ko_tables		# don't build Korean tables
#
Summary:	SCIM Generic Table IMEngine
Name:		scim-tables
Version:	0.5.10
Release:	6
License:	GPL v2+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/scim/%{name}-%{version}.tar.gz
# Source0-md5:	b3c0393acad77a03f3f71eb5b5a5670e
Source1:	CangJie5.png
# http://www.chinesecj.com/newsoftware/index3.php?Type=1
Source2:	CangJie5.txt.in
Patch0:		%{name}-rhbz217639.patch
Patch1:		%{name}-rhbz232860.patch
URL:		http://sourceforge.net/projects/scim
BuildRequires:	gtk+2-devel
BuildRequires:	scim-devel
Requires:	scim
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the Generic Table IMEngine for SCIM.

%package amharic
Summary:	SCIM tables for Amharic
Group:		Libraries
Requires:	scim-tables = %{version}

%description amharic
This package contains scim-tables files for Amharic input.

%package arabic
Summary:	SCIM tables for Arabic
Group:		Libraries
Requires:	scim-tables = %{version}

%description arabic
This package contains scim-tables files for Arabic input.

%package bengali
Summary:	SCIM tables for Bengali
Group:		Libraries
Requires:	scim-tables = %{version}

%description bengali
This package contains scim-tables files for Bengali input.

%package chinese
Summary:	SCIM tables for Chinese
Group:		Libraries
Requires:	scim-tables = %{version}

%description chinese
This package contains scim-tables files for Chinese input.

%package chinese-extra
Summary:	Additional SCIM tables for Chinese
Group:		Libraries
Requires:	scim-tables = %{version}

%description chinese-extra
This package contains additional less used scim-tables files for
Chinese input.

%package greek
Summary:	SCIM tables for Greek Polytonic
Group:		Libraries
Requires:	scim-tables = %{version}

%description greek
This package contains scim-tables files for Greek Polytonic input.

%package gujarati
Summary:	SCIM tables for Gujarati
Group:		Libraries
Requires:	scim-tables = %{version}

%description gujarati
This package contains scim-tables files for Gujarati input.

%package hebrew
Summary:	SCIM tables for Hebrew
Group:		Libraries
Requires:	scim-tables = %{version}

%description hebrew
This package contains scim-tables files for Hebrew input.

%package hindi
Summary:	SCIM tables for Hindi
Group:		Libraries
Requires:	scim-tables = %{version}

%description hindi
This package contains scim-tables files for Hindi input.

%package japanese
Summary:	SCIM tables for Japanese
Group:		Libraries
Requires:	scim-tables = %{version}

%description japanese
This package contains scim-tables files for Japanese.

%package kannada
Summary:	SCIM tables for Kannada
Group:		Libraries
Requires:	scim-tables = %{version}

%description kannada
This package contains scim-tables files for Kannada input.

%package korean
Summary:	SCIM tables for Korean
Group:		Libraries
Requires:	scim-tables = %{version}

%description korean
This package contains scim-tables files for Korean.

%package malayalam
Summary:	SCIM tables for Malayalam scripts
Group:		Libraries
Requires:	scim-tables = %{version}

%description malayalam
This package contains scim-tables files for Malayalam languages.

%package marathi
Summary:	SCIM tables for Marathi
Group:		Libraries
Requires:	scim-tables = %{version}

%description marathi
This package contains scim-tables files for Marathi languages.

%package nepali
Summary:	SCIM tables for Nepali
Group:		Libraries
Requires:	scim-tables = %{version}

%description nepali
This package contains scim-tables files for Nepali input.

%package punjabi
Summary:	SCIM tables for Punjabi
Group:		Libraries
Requires:	scim-tables = %{version}

%description punjabi
This package contains scim-tables files for Punjabi input.

%package russian
Summary:	SCIM tables for Russian
Group:		Libraries
Requires:	scim-tables = %{version}

%description russian
This package contains scim-tables files for Russian input.

%package tamil
Summary:	SCIM tables for Tamil
Group:		Libraries
Requires:	scim-tables = %{version}

%description tamil
This package contains scim-tables files for Tamil input.

%package thai
Summary:	SCIM tables for Thai
Group:		Libraries
Requires:	scim-tables = %{version}

%description thai
This package contains scim-tables files for Thai input.

%package telugu
Summary:	SCIM tables for Telugu
Group:		Libraries
Requires:	scim-tables = %{version}

%description telugu
This package contains scim-tables files for Telugu input.

%package uyghur
Summary:	SCIM tables for Uyghur
Group:		Libraries
Requires:	scim-tables = %{version}

%description uyghur
This package contains scim-tables files for Uyghur input.

%package ukrainian
Summary:	SCIM tables for Ukrainian
Group:		Libraries
Requires:	scim-tables = %{version}

%description ukrainian
This package contains scim-tables files for Ukrainian input.

%package vietnamese
Summary:	SCIM tables for Vietnamese
Group:		Libraries
Requires:	scim-tables = %{version}

%description vietnamese
This package contains scim-tables files for Vietnamese input.

%package additional
Summary:	Other miscellaneous SCIM tables
Group:		Libraries
Requires:	scim-tables = %{version}

%description additional
This package contains some miscellaneous scim-tables.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%{__cp} -f %SOURCE2 tables/zh/

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__install} %{SOURCE1} $RPM_BUILD_ROOT/%{_datadir}/scim/icons/

%{!?with_indic_tables:%{__rm} $RPM_BUILD_ROOT/%{_datadir}/scim/{icons,tables}/{Bengali,Gujarati,Hindi,Kannada,Malayalam,Marathi,Punjabi,Tamil,Telugu}-*}
%{!?with_jp_tables:%{__rm} $RPM_BUILD_ROOT/%{_datadir}/scim/{icons,tables}/{HIRAGANA,KATAKANA,Nippon}*}
%{!?with_ko_tables:%{__rm} $RPM_BUILD_ROOT/%{_datadir}/scim/{icons,tables}/{Hangul,Hanja}*}

%{__rm} ${RPM_BUILD_ROOT}/%{_libdir}/scim-1.0/*/*/*.{la,a}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
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
%doc tables/zh/README-*.txt
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
%doc tables/zh/README-*.txt
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
%{_datadir}/scim/icons/ZhuYin.png
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
%{_datadir}/scim/tables/classicalhebrew.bin

%files nepali
%defattr(644,root,root,755)
%{_datadir}/scim/tables/Nepali_*.bin
%{_datadir}/scim/icons/Nepali.png

%files russian
%defattr(644,root,root,755)
%{_datadir}/scim/icons/Translit.png
%{_datadir}/scim/icons/RussianTraditional.png
%{_datadir}/scim/icons/Yawerty.png
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
%{_datadir}/scim/tables/Hindi-inscript.bin
%{_datadir}/scim/tables/Hindi-phonetic.bin

%files kannada
%defattr(644,root,root,755)
%{_datadir}/scim/icons/Kannada-inscript.png
%{_datadir}/scim/icons/Kannada-kgp.png
%{_datadir}/scim/tables/Kannada-inscript.bin
%{_datadir}/scim/tables/Kannada-kgp.bin

%files malayalam
%defattr(644,root,root,755)
%{_datadir}/scim/icons/Malayalam-inscript.png
%{_datadir}/scim/tables/Malayalam-inscript.bin

%files marathi
%defattr(644,root,root,755)
%{_datadir}/scim/icons/Marathi-remington.png
%{_datadir}/scim/tables/Marathi-remington.bin

%files punjabi
%defattr(644,root,root,755)
%{_datadir}/scim/icons/Punjabi-inscript.png
%{_datadir}/scim/icons/Punjabi-jhelum.png
%{_datadir}/scim/icons/Punjabi-phonetic.png
%{_datadir}/scim/tables/Punjabi-inscript.bin
%{_datadir}/scim/tables/Punjabi-jhelum.bin
%{_datadir}/scim/tables/Punjabi-phonetic.bin

%files tamil
%defattr(644,root,root,755)
%{_datadir}/scim/icons/Tamil-inscript.png
%{_datadir}/scim/icons/Tamil-phonetic.png
%{_datadir}/scim/tables/Tamil-inscript.bin
%{_datadir}/scim/tables/Tamil-phonetic.bin

%files telugu
%defattr(644,root,root,755)
%{_datadir}/scim/icons/Telugu-inscript.png
%{_datadir}/scim/tables/Telugu-inscript.bin
%endif

%if %{with jp_tables}
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
