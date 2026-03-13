> 🌐 **Jeziki:** [English](../README.md) | [Русский](README.ru.md) | [ไทย](README.th.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [हिन्दी](README.hi.md) | [Español](README.es.md) | [Français](README.fr.md) | [العربية](README.ar.md) | [বাংলা](README.bn.md) | [Português](README.pt.md) | [اردو](README.ur.md) | [Bahasa Indonesia](README.id.md) | [Deutsch](README.de.md) | [日本語](README.ja.md) | [मराठी](README.mr.md) | [తెలుగు](README.te.md) | [Türkçe](README.tr.md) | [தமிழ்](README.ta.md) | [Tiếng Việt](README.vi.md) | [한국어](README.ko.md) | [Kiswahili](README.sw.md) | [Italiano](README.it.md) | [ગુજરાતી](README.gu.md) | [فارسی](README.fa.md) | [ಕನ್ನಡ](README.kn.md) | [Polski](README.pl.md) | [മലയാളം](README.ml.md) | [Українська](README.uk.md) | [Română](README.ro.md) | [Nederlands](README.nl.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Српски](README.sr.md) | [עברית](README.he.md) | [Български](README.bg.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Lietuvių](README.lt.md) | [Slovenščina](README.sl.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md)

# Gemini README Translator


[![Latest Release](https://img.shields.io/github/v/release/artryazanov/gemini-readme-translator?sort=semver)](https://github.com/artryazanov/gemini-readme-translator/releases)
[![Run Tests and E2E](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml)
[![Lint Workflows and Code](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml)
[![Update Major Tag](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml)
[![codecov](https://codecov.io/gh/artryazanov/gemini-readme-translator/graph/badge.svg)](https://codecov.io/gh/artryazanov/gemini-readme-translator)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

GitHub Action, ki samodejno prevede vaš `README.md` v več jezikov s pomočjo Gemini API-ja. Inteligentno vstavi navzkrižno povezan navigacijski meni za jezike v vse datoteke in samodejno uveljavi (commit) spremembe.

## 🚀 Funkcije
* **Večjezična podpora:** Ustvarite datoteke README za več jezikov v enem zagonu.
* **Samodejna navigacija:** Samodejno vstavi in vzdržuje standardni meni za preklapljanje jezikov na vrhu vaših datotek (lahko se onemogoči). Umetna inteligenca ga oblikuje samodejno!
* **Stiliranje po meri:** Določite lahko parameter za slog menija po meri, tako da umetna inteligenca oblikuje preklopnik jezikov natanko tako, kot želite.
* **Sledenje žetonom:** Prikaže statistiko uporabe žetonov (tokenov) Gemini.

## 🛠 Uporaba

Ustvarite datoteko poteka dela (npr. `.github/workflows/translate.yml`):

```yaml
name: Auto Translate README

on:
  push:
    paths:
      - 'README.md'
  workflow_dispatch:

jobs:
  translate:
    runs-on: ubuntu-latest
    permissions:
      contents: write

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v6

      - name: Gemini README Translator
        id: translator
        uses: artryazanov/gemini-readme-translator@v1
        with:
          api_key: ${{ secrets.GEMINI_API_KEY }}
          github_token: ${{ secrets.GITHUB_TOKEN }}
          languages: 'ru, zh-CN, es'
          add_language_menu: 'true'
          menu_style: '> 🌐 **Languages:** [English](README.md) | [Русский](README.ru.md)'

      - name: Print Translation Stats
        run: |
          echo "Postopek je trajal ${{ steps.translator.outputs.duration_seconds }} sekund."
          echo "Skupno porabljenih žetonov: ${{ steps.translator.outputs.total_tokens_used }}"
          echo "Vhodni žetoni: ${{ steps.translator.outputs.input_tokens_used }}"
          echo "Izhodni žetoni: ${{ steps.translator.outputs.output_tokens_used }}"

```

## 📥 Vnosi

| Vnos | Obvezno | Privzeto | Opis |
| --- | --- | --- | --- |
| `api_key` | Da |  | Vaš Google Gemini API ključ. |
| `github_token` | Da |  | Standardni GitHub žeton (`${{ secrets.GITHUB_TOKEN }}`). |
| `languages` | Da |  | Ciljni jeziki, ločeni z vejico (npr. `ru, es`). |
| `output_dir` | Ne | | Imenik za shranjevanje prevedenih datotek. Privzeto je to imenik izvorne datoteke. |
| `add_language_menu` | Ne | `true` | Nastavite na `false`, da onemogočite samodejno ustvarjanje menija za jezike. |
| `menu_style` | Ne | `> 🌐 **Languages:** [English](README.md) \| [Русский](README.ru.md)` | Referenčni slog, ki ga umetna inteligenca uporabi pri ustvarjanju novega menija za jezike. |
| `commit_message` | Ne | `docs: auto-translate README via Gemini` | Besedilo uporabljeno za git commit sporočilo. |
| `model` | Ne | `gemini-3.1-pro-preview` | Model Gemini, ki se bo uporabil. |
| `source_file` | Ne | `README.md` | Osnovna datoteka za prevod. |

## 📤 Izhodi

| Izhod | Opis |
| --- | --- |
| `total_tokens_used` | Skupno število obdelanih žetonov. |
| `input_tokens_used` | Število žetonov v vhodnih pozivih. |
| `output_tokens_used` | Število žetonov, ustvarjenih v odzivih. |
| `duration_seconds` | Skupni čas obdelave v sekundah. |

## 🔑 Kako pridobiti Google Gemini API ključ

Za uporabo te akcije potrebujete brezplačen API ključ iz Google AI Studia:

1. Pojdite na [Google AI Studio](https://aistudio.google.com/).
2. Prijavite se s svojim Google računom.
3. V levem navigacijskem meniju kliknite na **Get API key**.
4. Kliknite gumb **Create API key**.
5. Kopirajte ustvarjeni ključ.
6. Pojdite v svoj repozitorij GitHub -> **Settings** -> **Secrets and variables** -> **Actions**.
7. Kliknite **New repository secret**, poimenujte ga `GEMINI_API_KEY`, prilepite svoj ključ v polje Secret in shranite.

## 🔑 Kako konfigurirati standardni GitHub žeton

Ta akcija uporablja vgrajeni `GITHUB_TOKEN` za potiskanje potrditev (commits). **Ni vam treba** ročno ustvarjati osebnega žetona za dostop (PAT), vendar **morate** zagotoviti, da ima privzeti žeton pravilna dovoljenja:

1. Pojdite v **Settings** vašega repozitorija -> **Actions** -> **General**.
2. Pomaknite se navzdol do razdelka **Workflow permissions**.
3. Izberite **Read and write permissions**.
4. Kliknite **Save**.
5. V datoteki YAML poteka dela preprosto podajte `${{ secrets.GITHUB_TOKEN }}` kot vhod `github_token` (kot je prikazano v primeru uporabe).

## 📄 Licenca

Ta projekt je licenciran pod licenco MIT - za podrobnosti glejte datoteko [LICENSE](https://github.com/artryazanov/gemini-readme-translator/blob/main/LICENSE).