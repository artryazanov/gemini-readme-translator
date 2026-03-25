> 🌐 **Languages:** [English](../README.md) | [Русский](README.ru.md) | [ไทย](README.th.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [हिन्दी](README.hi.md) | [Español](README.es.md) | [Français](README.fr.md) | [العربية](README.ar.md) | [বাংলা](README.bn.md) | [Português](README.pt.md) | [اردو](README.ur.md) | [Bahasa Indonesia](README.id.md) | [Deutsch](README.de.md) | [日本語](README.ja.md) | [मराठी](README.mr.md) | [తెలుగు](README.te.md) | [Türkçe](README.tr.md) | [தமிழ்](README.ta.md) | [Tiếng Việt](README.vi.md) | [한국어](README.ko.md) | [Kiswahili](README.sw.md) | [Italiano](README.it.md) | [ગુજરાતી](README.gu.md) | [فارسی](README.fa.md) | [ಕನ್ನಡ](README.kn.md) | [Polski](README.pl.md) | [മലയാളം](README.ml.md) | [Українська](README.uk.md) | [Română](README.ro.md) | [Nederlands](README.nl.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Српски](README.sr.md) | [עברית](README.he.md) | [Български](README.bg.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Lietuvių](README.lt.md) | [Slovenščina](README.sl.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md)

# Gemini README Translator


[![Latest Release](https://img.shields.io/github/v/release/artryazanov/gemini-readme-translator?sort=semver)](https://github.com/artryazanov/gemini-readme-translator/releases)
[![Run Tests and E2E](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml)
[![Lint Workflows and Code](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml)
[![Update Major Tag](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml)
[![codecov](https://codecov.io/gh/artryazanov/gemini-readme-translator/graph/badge.svg)](https://codecov.io/gh/artryazanov/gemini-readme-translator)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

GitHub Action darbība, kas automātiski tulko jūsu `README.md` vairākās valodās, izmantojot Gemini API. Tā viedi ievieto savstarpēji saistītu valodu navigācijas izvēlni visos failos un automātiski veic izmaiņu fiksēšanu (commit).

## 🚀 Iespējas
* **Vairāku valodu atbalsts:** Ģenerējiet README vairākām valodām vienā izpildes reizē.
* **Automātiskā navigācija:** Automātiski ievieto un uztur standarta valodu pārslēdzēja izvēlni failu augšpusē (var tikt atspējota). AI to stilizē automātiski!
* **Pielāgots stils:** Jūs varat norādīt pielāgotu izvēlnes stila parametru, lai AI formatētu valodu pārslēdzēju tieši tā, kā jūs to vēlaties.
* **Marķieru (token) izsekošana:** Izvada Gemini marķieru lietojuma statistiku.

## 🛠 Lietošana

Izveidojiet darbplūsmas failu (piemēram, `.github/workflows/translate.yml`):

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

## 📥 Ievades parametri

| Ievade | Obligāts | Noklusējums | Apraksts |
| --- | --- | --- | --- |
| `api_key` | Jā |  | Jūsu Google Gemini API atslēga. |
| `github_token` | Jā |  | Standarta GitHub marķieris (`${{ secrets.GITHUB_TOKEN }}`). |
| `languages` | Jā |  | Ar komatu atdalītas mērķa valodas (piemēram, `ru, es`). |
| `output_dir` | Nē | | Direktorija, kur saglabāt iztulkotus failus. Pēc noklusējuma izmanto avota faila direktoriju. |
| `add_language_menu` | Nē | `true` | Iestatiet uz `false`, lai atspējotu automātisko valodas izvēlnes ģenerēšanu. |
| `use_absolute_links`| Nē | `true` | Iestatiet uz `false`, lai ģenerētajās valodu izvēlnēs izmantotu relatīvās saites, nevis absolūtos GitHub URL. |
| `menu_style` | Nē | `> 🌐 **Languages:** [English](README.md) \| [Русский](README.ru.md)` | Atsauces stils, ko AI izmanto, ģenerējot jaunu valodu izvēlni. |
| `commit_message` | Nē | `docs: auto-translate README via Gemini` | Teksts, ko izmanto git commit ziņojumam. |
| `model` | Nē | `gemini-3.1-pro-preview` | Izmantojamais Gemini modelis. |
| `source_file` | Nē | `README.md` | Bāzes fails, ko nepieciešams tulkot. |

## 📤 Izvades parametri

| Izvade | Apraksts |
| --- | --- |
| `total_tokens_used` | Kopējais apstrādāto marķieru skaits. |
| `input_tokens_used` | Marķieru skaits ievades uzvednēs. |
| `output_tokens_used` | Marķieru skaits ģenerētajās atbildēs. |
| `duration_seconds` | Kopējais apstrādes laiks sekundēs. |

## 🔑 Kā iegūt Google Gemini API atslēgu

Lai izmantotu šo Action, jums ir nepieciešama bezmaksas API atslēga no Google AI Studio:

1. Dodieties uz [Google AI Studio](https://aistudio.google.com/).
2. Pierakstieties ar savu Google kontu.
3. Kreisās puses navigācijas izvēlnē noklikšķiniet uz **Get API key** (Iegūt API atslēgu).
4. Noklikšķiniet uz pogas **Create API key** (Izveidot API atslēgu).
5. Nokopējiet izveidoto atslēgu.
6. Dodieties uz savu GitHub repozitoriju -> **Settings** -> **Secrets and variables** -> **Actions**.
7. Noklikšķiniet uz **New repository secret**, nosauciet to par `GEMINI_API_KEY`, ielīmējiet atslēgu Secret laukā un saglabājiet.

## 🔑 Kā konfigurēt standarta GitHub marķieri (Token)

Šī darbība izmanto iebūvēto `GITHUB_TOKEN`, lai pievienotu izmaiņas (push commits). Jums **nav** manuāli jāveido Personālās Piekļuves Marķieris (PAT), taču jums **ir** jāpārliecinās, ka noklusējuma marķierim ir pareizās atļaujas:

1. Dodieties uz sava repozitorija **Settings** -> **Actions** -> **General**.
2. Ritiniet uz leju līdz sadaļai **Workflow permissions**.
3. Izvēlieties **Read and write permissions**.
4. Noklikšķiniet uz **Save**.
5. Savā darbplūsmas YAML failā vienkārši padodiet `${{ secrets.GITHUB_TOKEN }}` ievadei `github_token` (kā parādīts lietošanas piemērā).

## 📄 Licence

Šis projekts ir licencēts saskaņā ar MIT licenci - sīkāku informāciju skatiet [LICENSE](https://github.com/artryazanov/gemini-readme-translator/blob/main/LICENSE) failā.