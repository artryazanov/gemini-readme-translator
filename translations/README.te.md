> 🌐 **Languages:** [English](../README.md) | [Русский](README.ru.md) | [ไทย](README.th.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [हिन्दी](README.hi.md) | [Español](README.es.md) | [Français](README.fr.md) | [العربية](README.ar.md) | [বাংলা](README.bn.md) | [Português](README.pt.md) | [اردو](README.ur.md) | [Bahasa Indonesia](README.id.md) | [Deutsch](README.de.md) | [日本語](README.ja.md) | [मराठी](README.mr.md) | [తెలుగు](README.te.md) | [Türkçe](README.tr.md) | [தமிழ்](README.ta.md) | [Tiếng Việt](README.vi.md) | [한국어](README.ko.md) | [Kiswahili](README.sw.md) | [Italiano](README.it.md) | [ગુજરાતી](README.gu.md) | [فارسی](README.fa.md) | [ಕನ್ನಡ](README.kn.md) | [Polski](README.pl.md) | [മലയാളം](README.ml.md) | [Українська](README.uk.md) | [Română](README.ro.md) | [Nederlands](README.nl.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Српски](README.sr.md) | [עברית](README.he.md) | [Български](README.bg.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Lietuvių](README.lt.md) | [Slovenščina](README.sl.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md)

# Gemini README Translator


[![Latest Release](https://img.shields.io/github/v/release/artryazanov/gemini-readme-translator?sort=semver)](https://github.com/artryazanov/gemini-readme-translator/releases)
[![Run Tests and E2E](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml)
[![Lint Workflows and Code](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml)
[![Update Major Tag](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml)
[![codecov](https://codecov.io/gh/artryazanov/gemini-readme-translator/graph/badge.svg)](https://codecov.io/gh/artryazanov/gemini-readme-translator)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Gemini API ని ఉపయోగించి మీ `README.md` ఫైల్‌ను స్వయంచాలకంగా బహుళ భాషల్లోకి అనువదించే GitHub యాక్షన్ ఇది. ఇది తెలివిగా అన్ని ఫైల్‌లలో క్రాస్-లింక్ చేయబడిన భాషా నావిగేషన్ మెనుని చొప్పించి, మార్పులను స్వయంచాలకంగా కమిట్ చేస్తుంది.

## 🚀 ఫీచర్లు
* **బహుళ-భాషా మద్దతు:** ఒకే రన్‌లో బహుళ భాషల కోసం READMEలను రూపొందించండి.
* **ఆటో-నావిగేషన్:** మీ ఫైల్‌ల ఎగువ భాగంలో ప్రామాణిక భాషా స్విచ్చర్ మెనుని స్వయంచాలకంగా చొప్పిస్తుంది మరియు నిర్వహిస్తుంది (దీన్ని డిసేబుల్ చేయవచ్చు). AI దీన్ని స్వయంచాలకంగా స్టైల్ చేస్తుంది!
* **కస్టమ్ స్టైలింగ్:** మీరు కస్టమ్ మెను స్టైల్ పారామీటర్‌ను అందించవచ్చు, తద్వారా AI మీకు కావాల్సిన విధంగానే భాషా స్విచ్చర్‌ను ఫార్మాట్ చేస్తుంది.
* **టోకెన్ ట్రాకింగ్:** జెమినీ (Gemini) టోకెన్ వినియోగ గణాంకాలను అవుట్‌పుట్ చేస్తుంది.

## 🛠 వాడుక

ఒక వర్క్‌ఫ్లో ఫైల్‌ను సృష్టించండి (ఉదా., `.github/workflows/translate.yml`):

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

## 📥 ఇన్‌పుట్‌లు

| ఇన్‌పుట్ | తప్పనిసరి | డిఫాల్ట్ | వివరణ |
| --- | --- | --- | --- |
| `api_key` | అవును |  | మీ Google Gemini API కీ. |
| `github_token` | అవును |  | ప్రామాణిక GitHub టోకెన్ (`${{ secrets.GITHUB_TOKEN }}`). |
| `languages` | అవును |  | కామాలతో వేరుచేయబడిన లక్షిత భాషలు (ఉదా. `ru, es`). |
| `output_dir` | కాదు | | అనువదించబడిన ఫైల్‌లను సేవ్ చేయాల్సిన డైరెక్టరీ. డిఫాల్ట్‌గా సోర్స్ ఫైల్ యొక్క డైరెక్టరీ తీసుకోబడుతుంది. |
| `add_language_menu` | కాదు | `true` | భాషా మెను యొక్క స్వయంచాలక ఉత్పత్తిని డిసేబుల్ చేయడానికి దీనిని `false` గా సెట్ చేయండి. |
| `menu_style` | కాదు | `> 🌐 **Languages:** [English](README.md) \| [Русский](README.ru.md)` | కొత్త భాషా మెనుని రూపొందించేటప్పుడు AI ఉపయోగించే రిఫరెన్స్ స్టైల్. |
| `commit_message` | కాదు | `docs: auto-translate README via Gemini` | git కమిట్ సందేశం కోసం ఉపయోగించే వచనం. |
| `model` | కాదు | `gemini-3.1-pro-preview` | ఉపయోగించాల్సిన Gemini మోడల్. |
| `source_file` | కాదు | `README.md` | అనువదించాల్సిన ఆధార ఫైల్ (బేస్ ఫైల్). |

## 📤 అవుట్‌పుట్‌లు

| అవుట్‌పుట్ | వివరణ |
| --- | --- |
| `total_tokens_used` | ప్రాసెస్ చేయబడిన మొత్తం టోకెన్ల సంఖ్య. |
| `input_tokens_used` | ఇన్‌పుట్ ప్రాంప్ట్‌లలోని టోకెన్ల సంఖ్య. |
| `output_tokens_used` | ప్రతిస్పందనలలో (responses) రూపొందించబడిన టోకెన్ల సంఖ్య. |
| `duration_seconds` | మొత్తం ప్రాసెసింగ్ సమయం సెకన్లలో. |

## 🔑 Google Gemini API కీని ఎలా పొందాలి

ఈ యాక్షన్‌ను ఉపయోగించడానికి, మీకు Google AI Studio నుండి ఉచిత API కీ అవసరం:

1. [Google AI Studio](https://aistudio.google.com/) కి వెళ్లండి.
2. మీ Google ఖాతాతో సైన్ ఇన్ చేయండి.
3. ఎడమవైపు నావిగేషన్ మెనులో, **Get API key** పై క్లిక్ చేయండి.
4. **Create API key** బటన్‌పై క్లిక్ చేయండి.
5. రూపొందించబడిన కీని కాపీ చేయండి.
6. మీ GitHub రిపోజిటరీకి వెళ్లండి -> **Settings** -> **Secrets and variables** -> **Actions**.
7. **New repository secret** పై క్లిక్ చేసి, దానికి `GEMINI_API_KEY` అని పేరు పెట్టి, Secret ఫీల్డ్‌లో మీ కీని పేస్ట్ చేసి సేవ్ చేయండి.

## 🔑 ప్రామాణిక (Standard) GitHub టోకెన్‌ను ఎలా కాన్ఫిగర్ చేయాలి

కమిట్‌లను పుష్ చేయడానికి ఈ యాక్షన్ అంతర్నిర్మిత `GITHUB_TOKEN` ని ఉపయోగిస్తుంది. మీరు మాన్యువల్‌గా పర్సనల్ యాక్సెస్ టోకెన్‌ (PAT) ను సృష్టించాల్సిన **అవసరం లేదు**, కానీ డిఫాల్ట్ టోకెన్‌కు సరైన అనుమతులు ఉన్నాయని మీరు **తప్పనిసరిగా** నిర్ధారించుకోవాలి:

1. మీ రిపోజిటరీ **Settings** -> **Actions** -> **General** కి వెళ్లండి.
2. క్రిందికి స్క్రోల్ చేసి **Workflow permissions** విభాగానికి వెళ్లండి.
3. **Read and write permissions** ఎంచుకోండి.
4. **Save** పై క్లిక్ చేయండి.
5. మీ వర్క్‌ఫ్లో YAML లో, (వాడుక ఉదాహరణలో చూపిన విధంగా) `github_token` ఇన్‌పుట్‌కు `${{ secrets.GITHUB_TOKEN }}` ను పంపండి.

## 📄 లైసెన్స్ (License)

ఈ ప్రాజెక్ట్ MIT లైసెన్స్ క్రింద లైసెన్స్ పొందింది - వివరాల కోసం [LICENSE](https://github.com/artryazanov/gemini-readme-translator/blob/main/LICENSE) ఫైల్‌ను చూడండి.