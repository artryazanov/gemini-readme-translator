> 🌐 **Languages:** [English](../README.md) | [Русский](README.ru.md) | [ไทย](README.th.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [हिन्दी](README.hi.md) | [Español](README.es.md) | [Français](README.fr.md) | [العربية](README.ar.md) | [বাংলা](README.bn.md) | [Português](README.pt.md) | [اردو](README.ur.md) | [Bahasa Indonesia](README.id.md) | [Deutsch](README.de.md) | [日本語](README.ja.md) | [मराठी](README.mr.md) | [తెలుగు](README.te.md) | [Türkçe](README.tr.md) | [தமிழ்](README.ta.md) | [Tiếng Việt](README.vi.md) | [한국어](README.ko.md) | [Kiswahili](README.sw.md) | [Italiano](README.it.md) | [ગુજરાતી](README.gu.md) | [فارسی](README.fa.md) | [ಕನ್ನಡ](README.kn.md) | [Polski](README.pl.md) | [മലയാളം](README.ml.md) | [Українська](README.uk.md) | [Română](README.ro.md) | [Nederlands](README.nl.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Српски](README.sr.md) | [עברית](README.he.md) | [Български](README.bg.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Lietuvių](README.lt.md) | [Slovenščina](README.sl.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md)

# Gemini README Translator


[![Latest Release](https://img.shields.io/github/v/release/artryazanov/gemini-readme-translator?sort=semver)](https://github.com/artryazanov/gemini-readme-translator/releases)
[![Run Tests and E2E](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml)
[![Lint Workflows and Code](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml)
[![Update Major Tag](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml)
[![codecov](https://codecov.io/gh/artryazanov/gemini-readme-translator/graph/badge.svg)](https://codecov.io/gh/artryazanov/gemini-readme-translator)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

એક GitHub Action જે Gemini API નો ઉપયોગ કરીને આપમેળે તમારા `README.md` નું બહુવિધ ભાષાઓમાં ભાષાંતર કરે છે. તે બધી ફાઇલોમાં બુદ્ધિપૂર્વક ક્રોસ-લિંક્ડ લેંગ્વેજ નેવિગેશન મેનૂ ઉમેરે છે અને આપમેળે ફેરફારોને કમિટ કરે છે.

## 🚀 સુવિધાઓ
* **બહુ-ભાષા સપોર્ટ:** એક જ રનમાં બહુવિધ ભાષાઓ માટે README બનાવો.
* **ઓટો-નેવિગેશન:** તમારી ફાઇલોની ટોચ પર આપમેળે સ્ટાન્ડર્ડ લેંગ્વેજ સ્વિચર મેનૂ દાખલ કરે છે અને જાળવે છે (અક્ષમ કરી શકાય છે). AI તેને આપમેળે સ્ટાઇલ કરે છે!
* **કસ્ટમ સ્ટાઇલિંગ:** તમે કસ્ટમ મેનૂ સ્ટાઇલ પેરામીટર પ્રદાન કરી શકો છો જેથી AI લેંગ્વેજ સ્વિચરને બરાબર તમે ઇચ્છો તે રીતે જ ફોર્મેટ કરે.
* **ટોકન ટ્રેકિંગ:** Gemini ટોકન વપરાશના આંકડા દર્શાવે છે.

## 🛠 ઉપયોગ

વર્કફ્લો ફાઇલ બનાવો (દા.ત., `.github/workflows/translate.yml`):

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

## 📥 ઇનપુટ્સ

| ઇનપુટ | જરૂરી | ડિફોલ્ટ | વર્ણન |
| --- | --- | --- | --- |
| `api_key` | હા |  | તમારી Google Gemini API કી. |
| `github_token` | હા |  | સ્ટાન્ડર્ડ GitHub ટોકન (`${{ secrets.GITHUB_TOKEN }}`). |
| `languages` | હા |  | અલ્પવિરામથી અલગ કરેલી લક્ષ્ય ભાષાઓ (દા.ત. `ru, es`). |
| `output_dir` | ના | | અનુવાદિત ફાઇલો સાચવવા માટેની ડિરેક્ટરી. ડિફોલ્ટ સોર્સ ફાઇલની ડિરેક્ટરી હોય છે. |
| `add_language_menu` | ના | `true` | ભાષા મેનૂનું ઓટો-જનરેશન બંધ કરવા માટે `false` સેટ કરો. |
| `menu_style` | ના | `> 🌐 **Languages:** [English](README.md) \| [Русский](README.ru.md)` | નવું ભાષા મેનૂ જનરેટ કરતી વખતે AI દ્વારા ઉપયોગમાં લેવાતી સંદર્ભ શૈલી. |
| `commit_message` | ના | `docs: auto-translate README via Gemini` | git કમિટ મેસેજ માટે વપરાતો ટેક્સ્ટ. |
| `model` | ના | `gemini-3.1-pro-preview` | વાપરવા માટેનું Gemini મોડેલ. |
| `source_file` | ના | `README.md` | અનુવાદ કરવા માટેની બેઝ ફાઇલ. |

## 📤 આઉટપુટ્સ

| આઉટપુટ | વર્ણન |
| --- | --- |
| `total_tokens_used` | પ્રક્રિયા કરેલ ટોકન્સની કુલ સંખ્યા. |
| `input_tokens_used` | ઇનપુટ પ્રોમ્પ્ટ્સમાં ટોકન્સની સંખ્યા. |
| `output_tokens_used` | પ્રતિસાદોમાં જનરેટ થયેલ ટોકન્સની સંખ્યા. |
| `duration_seconds` | સેકંડમાં કુલ પ્રોસેસિંગ સમય. |

## 🔑 Google Gemini API કી કેવી રીતે મેળવવી

આ એક્શનનો ઉપયોગ કરવા માટે, તમારે Google AI Studio માંથી મફત API કીની જરૂર પડશે:

1. [Google AI Studio](https://aistudio.google.com/) પર જાઓ.
2. તમારા Google એકાઉન્ટથી સાઇન ઇન કરો.
3. ડાબા નેવિગેશન મેનૂમાં, **Get API key** પર ક્લિક કરો.
4. **Create API key** બટન પર ક્લિક કરો.
5. જનરેટ થયેલી કીની કૉપિ કરો.
6. તમારી GitHub રિપોઝીટરીમાં જાઓ -> **Settings** -> **Secrets and variables** -> **Actions**.
7. **New repository secret** પર ક્લિક કરો, તેને `GEMINI_API_KEY` નામ આપો, તમારી કીને Secret ફીલ્ડમાં પેસ્ટ કરો અને સેવ કરો.

## 🔑 સ્ટાન્ડર્ડ GitHub ટોકનને કેવી રીતે કન્ફિગર કરવું

આ એક્શન કમિટ્સ પુશ કરવા માટે બિલ્ટ-ઇન `GITHUB_TOKEN` નો ઉપયોગ કરે છે. તમારે મેન્યુઅલી Personal Access Token (PAT) બનાવવાની **જરૂર નથી**, પરંતુ તમારે **ચોક્કસપણે** ખાતરી કરવી જ પડશે કે ડિફોલ્ટ ટોકન પાસે સાચી પરવાનગીઓ છે:

1. તમારી રિપોઝીટરીના **Settings** -> **Actions** -> **General** માં જાઓ.
2. નીચે **Workflow permissions** વિભાગ સુધી સ્ક્રોલ કરો.
3. **Read and write permissions** પસંદ કરો.
4. **Save** પર ક્લિક કરો.
5. તમારા વર્કફ્લો YAML માં, સરળ રીતે `github_token` ઇનપુટમાં `${{ secrets.GITHUB_TOKEN }}` પાસ કરો (જેમ કે ઉપયોગના ઉદાહરણમાં બતાવવામાં આવ્યું છે).

## 📄 લાઇસન્સ

આ પ્રોજેક્ટ MIT લાઇસન્સ હેઠળ લાઇસન્સ પ્રાપ્ત છે - વિગતો માટે [LICENSE](https://github.com/artryazanov/gemini-readme-translator/blob/main/LICENSE) ફાઇલ જુઓ.