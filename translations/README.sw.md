> 🌐 **Languages:** [English](../README.md) | [Русский](README.ru.md) | [ไทย](README.th.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [हिन्दी](README.hi.md) | [Español](README.es.md) | [Français](README.fr.md) | [العربية](README.ar.md) | [বাংলা](README.bn.md) | [Português](README.pt.md) | [اردو](README.ur.md) | [Bahasa Indonesia](README.id.md) | [Deutsch](README.de.md) | [日本語](README.ja.md) | [मराठी](README.mr.md) | [తెలుగు](README.te.md) | [Türkçe](README.tr.md) | [தமிழ்](README.ta.md) | [Tiếng Việt](README.vi.md) | [한국어](README.ko.md) | [Kiswahili](README.sw.md) | [Italiano](README.it.md) | [ગુજરાતી](README.gu.md) | [فارسی](README.fa.md) | [ಕನ್ನಡ](README.kn.md) | [Polski](README.pl.md) | [മലയാളം](README.ml.md) | [Українська](README.uk.md) | [Română](README.ro.md) | [Nederlands](README.nl.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Српски](README.sr.md) | [עברית](README.he.md) | [Български](README.bg.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Lietuvių](README.lt.md) | [Slovenščina](README.sl.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md)

# Mtafsiri wa README wa Gemini


[![Latest Release](https://img.shields.io/github/v/release/artryazanov/gemini-readme-translator?sort=semver)](https://github.com/artryazanov/gemini-readme-translator/releases)
[![Run Tests and E2E](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml)
[![Lint Workflows and Code](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml)
[![Update Major Tag](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml)
[![codecov](https://codecov.io/gh/artryazanov/gemini-readme-translator/graph/badge.svg)](https://codecov.io/gh/artryazanov/gemini-readme-translator)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Action ya GitHub inayotafsiri kiotomatiki faili yako ya `README.md` kwa lugha nyingi ikitumia API ya Gemini. Inaingiza kwa ufasaha menyu ya viungo vya lugha inayoingiliana kwenye faili zote na kufanya commit ya mabadiliko kiotomatiki.

## 🚀 Vipengele
* **Usaidizi wa Lugha Nyingi:** Tengeneza faili za README za lugha nyingi kwa mkupuo mmoja.
* **Usogezaji wa Kiotomatiki:** Huweka na kudumisha menyu sanifu ya kubadilisha lugha juu ya faili zako (inaweza kuzimwa). AI huipangilia kiotomatiki!
* **Uwekaji wa Mtindo Maalum:** Unaweza kutoa kigezo maalum cha mtindo wa menyu ili AI iweze kupangilia kibadilisha lugha jinsi unavyotaka.
* **Ufuatiliaji wa Tokeni:** Hutoa takwimu za matumizi ya tokeni za Gemini.

## 🛠 Matumizi

Tengeneza faili ya utendakazi (mfano, `.github/workflows/translate.yml`):

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

## 📥 Vigezo vya Kuingiza (Inputs)

| Kigezo (Input) | Inahitajika | Chaguo-msingi | Maelezo |
| --- | --- | --- | --- |
| `api_key` | Ndiyo |  | Ufunguo wako wa API ya Google Gemini. |
| `github_token` | Ndiyo |  | Tokeni sanifu ya GitHub (`${{ secrets.GITHUB_TOKEN }}`). |
| `languages` | Ndiyo |  | Lugha lengwa zilizotenganishwa na koma (mf. `ru, es`). |
| `output_dir` | Hapana | | Folda ya kuhifadhi faili zilizotafsiriwa. Chaguo-msingi ni folda ya faili asili. |
| `add_language_menu` | Hapana | `true` | Weka `false` ili kuzuia utengenezaji kiotomatiki wa menyu ya lugha. |
| `use_absolute_links`| Hapana | `true` | Weka iwe `false` ili utumie viungo vya karibu badala ya URL kamili za GitHub kwenye menyu za lugha zilizoundwa. |
| `menu_style` | Hapana | `> 🌐 **Languages:** [English](README.md) \| [Русский](README.ru.md)` | Mtindo wa rejea ambao AI hutumia inapotengeneza menyu mpya ya lugha. |
| `commit_message` | Hapana | `docs: auto-translate README via Gemini` | Maandishi yanayotumiwa kwa ujumbe wa git commit. |
| `model` | Hapana | `gemini-3.1-pro-preview` | Muundo wa Gemini utakaotumika. |
| `source_file` | Hapana | `README.md` | Faili kuu la kutafsiri. |

## 📤 Vigezo vya Kutoa (Outputs)

| Kigezo (Output) | Maelezo |
| --- | --- |
| `total_tokens_used` | Jumla ya idadi ya tokeni zilizochakatwa. |
| `input_tokens_used` | Idadi ya tokeni kwenye vidokezo (prompts) vya kuingiza. |
| `output_tokens_used` | Idadi ya tokeni zilizozalishwa kwenye majibu. |
| `duration_seconds` | Jumla ya muda wa kuchakata katika sekunde. |

## 🔑 Jinsi ya kupata Ufunguo wa API wa Google Gemini

Ili kutumia Action hii, unahitaji ufunguo wa API wa bure kutoka Google AI Studio:

1. Nenda kwenye [Google AI Studio](https://aistudio.google.com/).
2. Ingia (Sign in) kwa kutumia akaunti yako ya Google.
3. Kwenye menyu ya kuelekeza kushoto, bofya **Get API key**.
4. Bofya kitufe cha **Create API key**.
5. Nakili ufunguo uliotengenezwa.
6. Nenda kwenye hifadhi yako ya GitHub (repository) -> **Settings** -> **Secrets and variables** -> **Actions**.
7. Bofya **New repository secret**, ipe jina `GEMINI_API_KEY`, weka (paste) ufunguo wako kwenye uwanja wa Secret, na uhifadhi.

## 🔑 Jinsi ya kusanidi Tokeni Sanifu ya GitHub

Action hii inatumia `GITHUB_TOKEN` iliyojengewa ndani ili kusukuma (push) commits. **Hauhitaji** kutengeneza Tokeni ya Ufikiaji Binafsi (PAT) wewe mwenyewe, lakini **lazima** uhakikishe kuwa tokeni chaguo-msingi ina ruhusa sahihi:

1. Nenda kwenye **Settings** za hifadhi yako -> **Actions** -> **General**.
2. Shuka chini hadi kwenye sehemu ya **Workflow permissions**.
3. Chagua **Read and write permissions**.
4. Bofya **Save**.
5. Kwenye faili yako ya YAML ya utendakazi, pitisha tu `${{ secrets.GITHUB_TOKEN }}` kwenye kigezo cha `github_token` (kama inavyoonyeshwa kwenye mfano wa matumizi).

## 📄 Leseni

Mradi huu umepewa leseni chini ya Leseni ya MIT - angalia faili la [LICENSE](https://github.com/artryazanov/gemini-readme-translator/blob/main/LICENSE) kwa maelezo zaidi.