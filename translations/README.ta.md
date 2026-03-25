> 🌐 **Languages:** [English](../README.md) | [Русский](README.ru.md) | [ไทย](README.th.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [हिन्दी](README.hi.md) | [Español](README.es.md) | [Français](README.fr.md) | [العربية](README.ar.md) | [বাংলা](README.bn.md) | [Português](README.pt.md) | [اردو](README.ur.md) | [Bahasa Indonesia](README.id.md) | [Deutsch](README.de.md) | [日本語](README.ja.md) | [मराठी](README.mr.md) | [తెలుగు](README.te.md) | [Türkçe](README.tr.md) | [தமிழ்](README.ta.md) | [Tiếng Việt](README.vi.md) | [한국어](README.ko.md) | [Kiswahili](README.sw.md) | [Italiano](README.it.md) | [ગુજરાતી](README.gu.md) | [فارسی](README.fa.md) | [ಕನ್ನಡ](README.kn.md) | [Polski](README.pl.md) | [മലയാളം](README.ml.md) | [Українська](README.uk.md) | [Română](README.ro.md) | [Nederlands](README.nl.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Српски](README.sr.md) | [עברית](README.he.md) | [Български](README.bg.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Lietuvių](README.lt.md) | [Slovenščina](README.sl.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md)

# Gemini README Translator


[![Latest Release](https://img.shields.io/github/v/release/artryazanov/gemini-readme-translator?sort=semver)](https://github.com/artryazanov/gemini-readme-translator/releases)
[![Run Tests and E2E](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml)
[![Lint Workflows and Code](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml)
[![Update Major Tag](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml)
[![codecov](https://codecov.io/gh/artryazanov/gemini-readme-translator/graph/badge.svg)](https://codecov.io/gh/artryazanov/gemini-readme-translator)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Gemini API-ஐப் பயன்படுத்தி உங்கள் `README.md` கோப்பை பல மொழிகளில் தானியங்கியாக மொழிபெயர்க்கும் ஒரு GitHub Action இது. இது அனைத்து கோப்புகளிலும் ஒருவருக்கொருவர் இணைக்கப்பட்ட மொழி வழிசெலுத்தல் மெனுவை புத்திசாலித்தனமாகச் செருகுகிறது, மேலும் மாற்றங்களைத் தானாகவே கமிட் (commit) செய்கிறது.

## 🚀 அம்சங்கள்
* **பன்மொழி ஆதரவு:** ஒரே செயல்பாட்டில் பல மொழிகளுக்கான README-களை உருவாக்கலாம்.
* **தானியங்கு வழிசெலுத்தல் (Auto-Navigation):** உங்கள் கோப்புகளின் மேலே நிலையான மொழி மாற்றும் மெனுவை இது தானாகவே செருகி பராமரிக்கிறது (இதை முடக்கவும் முடியும்). AI தானாகவே இதனை வடிவமைக்கிறது!
* **விருப்பமான வடிவமைப்பு (Custom Styling):** மொழி மாற்றும் மெனு உங்களுக்குத் தேவையான அதே வடிவமைப்பில் இருப்பதற்கு, நீங்கள் விருப்பமான மெனு வடிவமைப்பு அளவுருவை (parameter) வழங்கலாம்.
* **டோக்கன் கண்காணிப்பு (Token Tracking):** Gemini டோக்கன் பயன்பாட்டுப் புள்ளிவிவரங்களை வெளியிடுகிறது.

## 🛠 பயன்பாடு

ஒரு workflow கோப்பை உருவாக்கவும் (உதாரணமாக, `.github/workflows/translate.yml`):

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

## 📥 உள்ளீடுகள் (Inputs)

| உள்ளீடு (Input) | தேவையானது (Required) | இயல்புநிலை (Default) | விளக்கம் (Description) |
| --- | --- | --- | --- |
| `api_key` | ஆம் |  | உங்களின் Google Gemini API Key. |
| `github_token` | ஆம் |  | நிலையான GitHub token (`${{ secrets.GITHUB_TOKEN }}`). |
| `languages` | ஆம் |  | காற்புள்ளியால் பிரிக்கப்பட்ட இலக்கு மொழிகள் (உதாரணமாக: `ru, es`). |
| `output_dir` | இல்லை | | மொழிபெயர்க்கப்பட்ட கோப்புகளைச் சேமிப்பதற்கான கோப்பகம் (Directory). இதன் இயல்புநிலை மூலக் கோப்பின் கோப்பகமாகும். |
| `add_language_menu` | இல்லை | `true` | மொழி மெனு தானாகவே உருவாக்கப்படுவதை முடக்க `false` என அமைக்கவும். |
| `use_absolute_links`| இல்லை | `true` | உருவாக்கப்பட்ட மொழி மெனுக்களில் முழுமையான GitHub URL களுக்குப் பதிலாக தொடர்புடைய இணைப்புகளைப் பயன்படுத்த `false` என அமைக்கவும். |
| `menu_style` | இல்லை | `> 🌐 **Languages:** [English](README.md) \| [Русский](README.ru.md)` | புதிய மொழி மெனுவை உருவாக்கும் போது AI பயன்படுத்தும் குறிப்பு வடிவமைப்பு (Reference style). |
| `commit_message` | இல்லை | `docs: auto-translate README via Gemini` | git commit செய்திக்காகப் பயன்படுத்தப்படும் உரை. |
| `model` | இல்லை | `gemini-3.1-pro-preview` | பயன்படுத்த வேண்டிய Gemini மாடல். |
| `source_file` | இல்லை | `README.md` | மொழிபெயர்க்க வேண்டிய அடிப்படைக் கோப்பு. |

## 📤 வெளியீடுகள் (Outputs)

| வெளியீடு (Output) | விளக்கம் (Description) |
| --- | --- |
| `total_tokens_used` | செயலாக்கப்பட்ட டோக்கன்களின் மொத்த எண்ணிக்கை. |
| `input_tokens_used` | உள்ளீட்டு (Input prompts) டோக்கன்களின் எண்ணிக்கை. |
| `output_tokens_used` | பதில்களில் (Responses) உருவாக்கப்பட்ட டோக்கன்களின் எண்ணிக்கை. |
| `duration_seconds` | செயலாக்கத்திற்கு எடுத்துக்கொள்ளப்பட்ட மொத்த நேரம் வினாடிகளில். |

## 🔑 Google Gemini API Key-ஐப் பெறுவது எப்படி?

இந்த Action-ஐப் பயன்படுத்த, உங்களுக்கு Google AI Studio-வில் இருந்து ஒரு இலவச API key தேவை:

1. [Google AI Studio](https://aistudio.google.com/)-க்குச் செல்லவும்.
2. உங்கள் Google கணக்கைக் கொண்டு உள்நுழையவும் (Sign in).
3. இடதுபுற வழிசெலுத்தல் மெனுவில், **Get API key** என்பதை கிளிக் செய்யவும்.
4. **Create API key** பட்டனைக் கிளிக் செய்யவும்.
5. உருவாக்கப்பட்ட key-ஐ நகலெடுக்கவும் (Copy).
6. உங்கள் GitHub ரெபாசிட்டரிக்குச் செல்லவும் -> **Settings** -> **Secrets and variables** -> **Actions**.
7. **New repository secret** என்பதைக் கிளிக் செய்து, அதற்கு `GEMINI_API_KEY` என பெயரிடவும். அதன்பின் Secret புலத்தில் உங்கள் key-ஐ ஒட்டி (Paste), சேமிக்கவும்.

## 🔑 நிலையான GitHub Token-ஐ எவ்வாறு கட்டமைப்பது (Configure)?

கமிட்களை (commits) புஷ் செய்ய இந்த Action உள்ளமைக்கப்பட்ட `GITHUB_TOKEN`-ஐப் பயன்படுத்துகிறது. நீங்கள் கைமுறையாக ஒரு Personal Access Token (PAT)-ஐ உருவாக்கத் **தேவையில்லை**, ஆனால் இயல்புநிலை டோக்கனுக்கு சரியான அனுமதிகள் (permissions) இருப்பதை நீங்கள் **கட்டாயம்** உறுதி செய்ய வேண்டும்:

1. உங்கள் ரெபாசிட்டரியின் **Settings** -> **Actions** -> **General** பகுதிக்குச் செல்லவும்.
2. கீழே ஸ்க்ரோல் செய்து **Workflow permissions** பகுதிக்கு வரவும்.
3. **Read and write permissions** என்பதைத் தேர்ந்தெடுக்கவும்.
4. **Save** என்பதைக் கிளிக் செய்யவும்.
5. பயன்பாட்டு எடுத்துக்காட்டில் காட்டியுள்ளபடி, உங்கள் workflow YAML-ல் `github_token` உள்ளீட்டிற்கு `${{ secrets.GITHUB_TOKEN }}` என்பதைச் சேர்க்கவும்.

## 📄 உரிமம் (License)

இந்தத் திட்டம் MIT உரிமத்தின் கீழ் உரிமம் பெற்றுள்ளது - விவரங்களுக்கு [LICENSE](https://github.com/artryazanov/gemini-readme-translator/blob/main/LICENSE) கோப்பைப் பார்க்கவும்.