> 🌐 **Languages:** [English](../README.md) | [Русский](README.ru.md) | [ไทย](README.th.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [हिन्दी](README.hi.md) | [Español](README.es.md) | [Français](README.fr.md) | [العربية](README.ar.md) | [বাংলা](README.bn.md) | [Português](README.pt.md) | [اردو](README.ur.md) | [Bahasa Indonesia](README.id.md) | [Deutsch](README.de.md) | [日本語](README.ja.md) | [मराठी](README.mr.md) | [తెలుగు](README.te.md) | [Türkçe](README.tr.md) | [தமிழ்](README.ta.md) | [Tiếng Việt](README.vi.md) | [한국어](README.ko.md) | [Kiswahili](README.sw.md) | [Italiano](README.it.md) | [ગુજરાતી](README.gu.md) | [فارسی](README.fa.md) | [ಕನ್ನಡ](README.kn.md) | [Polski](README.pl.md) | [മലയാളം](README.ml.md) | [Українська](README.uk.md) | [Română](README.ro.md) | [Nederlands](README.nl.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Српски](README.sr.md) | [עברית](README.he.md) | [Български](README.bg.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Lietuvių](README.lt.md) | [Slovenščina](README.sl.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md)

# Gemini README Translator


[![Latest Release](https://img.shields.io/github/v/release/artryazanov/gemini-readme-translator?sort=semver)](https://github.com/artryazanov/gemini-readme-translator/releases)
[![Run Tests and E2E](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml)
[![Lint Workflows and Code](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml)
[![Update Major Tag](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml)
[![codecov](https://codecov.io/gh/artryazanov/gemini-readme-translator/graph/badge.svg)](https://codecov.io/gh/artryazanov/gemini-readme-translator)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

GitHub Action, joka kääntää `README.md`-tiedostosi automaattisesti useille kielille käyttämällä Gemini API:a. Se lisää älykkäästi ristiinlinkitetyn kielenvalintavalikon kaikkiin tiedostoihin ja vahvistaa (commit) muutokset automaattisesti.

## 🚀 Ominaisuudet
* **Monikielinen tuki:** Luo README-tiedostot useille kielille yhdellä ajolla.
* **Automaattinen navigointi:** Lisää ja ylläpitää automaattisesti vakioidun kielenvalintavalikon tiedostojesi yläosassa (voidaan poistaa käytöstä). Tekoäly tyylittelee sen automaattisesti!
* **Mukautettu tyylittely:** Voit antaa mukautetun valikkotyyliparametrin, jolloin tekoäly muotoilee kielenvalitsimen juuri haluamallasi tavalla.
* **Tokenien seuranta:** Tulostaa Geminin token-käyttötilastot.

## 🛠 Käyttö

Luo työnkulkutiedosto (esim. `.github/workflows/translate.yml`):

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
          echo "Process took ${{ steps.translator.outputs.duration_seconds }} seconds."
          echo "Total tokens used: ${{ steps.translator.outputs.total_tokens_used }}"
          echo "Input tokens: ${{ steps.translator.outputs.input_tokens_used }}"
          echo "Output tokens: ${{ steps.translator.outputs.output_tokens_used }}"

```

## 📥 Syötteet

| Syöte | Pakollinen | Oletus | Kuvaus |
| --- | --- | --- | --- |
| `api_key` | Kyllä |  | Google Gemini API -avain. |
| `github_token` | Kyllä |  | Vakio GitHub-token (`${{ secrets.GITHUB_TOKEN }}`). |
| `languages` | Kyllä |  | Pilkuilla erotetut kohdekielet (esim. `ru, es`). |
| `output_dir` | Ei | | Hakemisto käännettyjen tiedostojen tallentamiseen. Oletuksena lähdetiedoston hakemisto. |
| `add_language_menu` | Ei | `true` | Aseta arvoon `false` poistaaksesi kielivalikon automaattisen luonnin käytöstä. |
| `use_absolute_links`| Ei | `true` | Aseta `false` käyttääksesi suhteellisia linkkejä absoluuttisten GitHub-URL-osoitteiden sijaan luoduissa kielivalikoissa. |
| `menu_style` | Ei | `> 🌐 **Languages:** [English](README.md) \| [Русский](README.ru.md)` | Viitetyyli, jota tekoäly käyttää luodessaan uutta kielivalikkoa. |
| `commit_message` | Ei | `docs: auto-translate README via Gemini` | Git-vahvistusviestissä (commit) käytettävä teksti. |
| `model` | Ei | `gemini-3.1-pro-preview` | Käytettävä Gemini-malli. |
| `source_file` | Ei | `README.md` | Käännettävä perustiedosto. |

## 📤 Tulosteet

| Tuloste | Kuvaus |
| --- | --- |
| `total_tokens_used` | Käsiteltyjen tokenien kokonaismäärä. |
| `input_tokens_used` | Syötekyselyissä käytettyjen tokenien määrä. |
| `output_tokens_used` | Vastauksissa luotujen tokenien määrä. |
| `duration_seconds` | Käsittelyn kokonaisaika sekunteina. |

## 🔑 Kuinka saada Google Gemini API -avain

Tämän toiminnon käyttämiseksi tarvitset ilmaisen API-avaimen Google AI Studiosta:

1. Mene osoitteeseen [Google AI Studio](https://aistudio.google.com/).
2. Kirjaudu sisään Google-tililläsi.
3. Napsauta vasemmasta navigointivalikosta **Get API key**.
4. Napsauta **Create API key** -painiketta.
5. Kopioi luotu avain.
6. Siirry GitHub-arkistoosi -> **Settings** -> **Secrets and variables** -> **Actions**.
7. Napsauta **New repository secret**, nimeä se `GEMINI_API_KEY`, liitä avaimesi Secret-kenttään ja tallenna.

## 🔑 Kuinka määrittää vakio GitHub-token

Tämä toiminto käyttää sisäänrakennettua `GITHUB_TOKEN`ia commit-vahvistusten puskemiseen. Sinun **ei** tarvitse luoda henkilökohtaista käyttöoikeustunnusta (PAT) manuaalisesti, mutta sinun **täytyy** varmistaa, että oletustokenilla on oikeat käyttöoikeudet:

1. Siirry arkistosi kohtaan **Settings** -> **Actions** -> **General**.
2. Vieritä alas kohtaan **Workflow permissions**.
3. Valitse **Read and write permissions**.
4. Napsauta **Save**.
5. Välitä työnkulkusi YAML-tiedostossa yksinkertaisesti `${{ secrets.GITHUB_TOKEN }}` `github_token`-syötteelle (kuten käyttöesimerkissä on esitetty).

## 📄 Lisenssi

Tämä projekti on lisensoitu MIT-lisenssillä – katso lisätietoja [LICENSE](https://github.com/artryazanov/gemini-readme-translator/blob/main/LICENSE)-tiedostosta.