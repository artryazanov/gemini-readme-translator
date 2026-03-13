> 🌐 **Languages:** [English](README.md) | [English (en)](translations/README.en.md) | [Русский](translations/README.ru.md) | [ไทย](translations/README.th.md) | [简体中文](translations/README.zh-CN.md) | [繁體中文](translations/README.zh-TW.md) | [हिन्दी](translations/README.hi.md) | [Español](translations/README.es.md) | [Français](translations/README.fr.md) | [العربية](translations/README.ar.md) | [বাংলা](translations/README.bn.md) | [Português](translations/README.pt.md) | [اردو](translations/README.ur.md) | [Bahasa Indonesia](translations/README.id.md) | [Deutsch](translations/README.de.md) | [日本語](translations/README.ja.md) | [मराठी](translations/README.mr.md) | [తెలుగు](translations/README.te.md) | [Türkçe](translations/README.tr.md) | [தமிழ்](translations/README.ta.md) | [Tiếng Việt](translations/README.vi.md) | [한국어](translations/README.ko.md) | [Kiswahili](translations/README.sw.md) | [Italiano](translations/README.it.md) | [ગુજરાતી](translations/README.gu.md) | [فارسی](translations/README.fa.md) | [ಕನ್ನಡ](translations/README.kn.md) | [Polski](translations/README.pl.md) | [മലയാളം](translations/README.ml.md) | [Українська](translations/README.uk.md) | [Română](translations/README.ro.md) | [Nederlands](translations/README.nl.md) | [Ελληνικά](translations/README.el.md) | [Magyar](translations/README.hu.md) | [Svenska](translations/README.sv.md) | [Čeština](translations/README.cs.md) | [Српски](translations/README.sr.md) | [עברית](translations/README.he.md) | [Български](translations/README.bg.md) | [Dansk](translations/README.da.md) | [Suomi](translations/README.fi.md) | [Norsk](translations/README.no.md) | [Slovenčina](translations/README.sk.md) | [Hrvatski](translations/README.hr.md) | [Lietuvių](translations/README.lt.md) | [Slovenščina](translations/README.sl.md) | [Latviešu](translations/README.lv.md) | [Eesti](translations/README.et.md)

# ജെമിനി README വിവർത്തകൻ (Gemini README Translator)


[![Latest Release](https://img.shields.io/github/v/release/artryazanov/gemini-readme-translator?sort=semver)](https://github.com/artryazanov/gemini-readme-translator/releases)
[![Run Tests and E2E](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml)
[![Lint Workflows and Code](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml)
[![Update Major Tag](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml)
[![codecov](https://codecov.io/gh/artryazanov/gemini-readme-translator/graph/badge.svg)](https://codecov.io/gh/artryazanov/gemini-readme-translator)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Gemini API ഉപയോഗിച്ച് നിങ്ങളുടെ `README.md` ഫയലുകൾ ഒന്നിലധികം ഭാഷകളിലേക്ക് സ്വയമേവ വിവർത്തനം ചെയ്യുന്ന ഒരു GitHub ആക്ഷൻ ആണിത്. ഇത് എല്ലാ ഫയലുകളിലേക്കും പരസ്പരം ബന്ധിപ്പിച്ചിട്ടുള്ള (cross-linked) ഒരു ലാംഗ്വേജ് നാവിഗേഷൻ മെനു ബുദ്ധിപൂർവ്വം ഉൾപ്പെടുത്തുന്നു. കൂടാതെ മാറ്റങ്ങൾ നേരിട്ട് കമ്മിറ്റ് (commit) ചെയ്യാനോ അല്ലെങ്കിൽ റിവ്യൂവിനായി ഒരു പുൾ റിക്വസ്റ്റ് (Pull Request) ഉണ്ടാക്കാനോ ഇതിന് കഴിയും.

## 🚀 സവിശേഷതകൾ
* **ബഹുഭാഷാ പിന്തുണ:** ഒറ്റയടിക്ക് ഒന്നിലധികം ഭാഷകൾക്കായി README ഫയലുകൾ ജനറേറ്റ് ചെയ്യുന്നു.
* **ഓട്ടോ-നാവിഗേഷൻ:** നിങ്ങളുടെ ഫയലുകളുടെ മുകളിൽ ഒരു സ്റ്റാൻഡേർഡ് ലാംഗ്വേജ് സ്വിച്ചർ മെനു സ്വയമേവ നൽകുകയും പരിപാലിക്കുകയും ചെയ്യുന്നു (ആവശ്യമെങ്കിൽ ഇത് പ്രവർത്തനരഹിതമാക്കാം). AI ഇതിനെ സ്വയമേവ സ്റ്റൈൽ ചെയ്യുന്നു!
* **കസ്റ്റം സ്റ്റൈലിംഗ്:** നിങ്ങൾക്ക് ഇഷ്ടാനുസൃതമായ ഒരു മെനു സ്റ്റൈൽ പാരാമീറ്റർ നൽകാൻ സാധിക്കും, അതുവഴി AI ലാംഗ്വേജ് സ്വിച്ചറിനെ നിങ്ങൾക്ക് ആവശ്യമുള്ള രീതിയിൽ തന്നെ ക്രമീകരിക്കുന്നു.
* **ടോക്കൺ ട്രാക്കിംഗ്:** ജെമിനി ടോക്കൺ ഉപയോഗത്തിന്റെ കണക്കുകൾ ലഭ്യമാക്കുന്നു.

## 🛠 ഉപയോഗക്രമം

ഒരു വർക്ക്ഫ്ലോ ഫയൽ നിർമ്മിക്കുക (ഉദാഹരണത്തിന്, `.github/workflows/translate.yml`):

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
        uses: artryazanov/gemini-readme-translator@v1
        with:
          api_key: ${{ secrets.GEMINI_API_KEY }}
          github_token: ${{ secrets.GITHUB_TOKEN }}
          languages: 'ru, zh-CN, es'
          add_language_menu: 'true'
          menu_style: '> 🌐 **Languages:** [English](README.md) | [Русский](README.ru.md)'


```

## 📥 ഇൻപുട്ടുകൾ (Inputs)

| ഇൻപുട്ട് (Input) | നിർബന്ധമാണോ (Required) | ഡിഫോൾട്ട് (Default) | വിവരണം (Description) |
| --- | --- | --- | --- |
| `api_key` | അതെ |  | നിങ്ങളുടെ ഗൂഗിൾ ജെമിനി (Google Gemini) API കീ. |
| `github_token` | അതെ |  | സ്റ്റാൻഡേർഡ് GitHub ടോക്കൺ (`${{ secrets.GITHUB_TOKEN }}`). |
| `languages` | അതെ |  | കോമ ഉപയോഗിച്ച് വേർതിരിച്ച ലക്ഷ്യ ഭാഷകൾ (ഉദാഹരണത്തിന് `ru, es`). |
| `output_dir` | അല്ല | | വിവർത്തനം ചെയ്ത ഫയലുകൾ സേവ് ചെയ്യേണ്ട ഡയറക്ടറി. ഡിഫോൾട്ടായി സോഴ്സ് ഫയലിന്റെ ഡയറക്ടറി ഉപയോഗിക്കുന്നു. |
| `add_language_menu` | അല്ല | `true` | ലാംഗ്വേജ് മെനു സ്വയമേവ നിർമ്മിക്കുന്നത് പ്രവർത്തനരഹിതമാക്കാൻ `false` ആയി സജ്ജമാക്കുക. |
| `menu_style` | അല്ല | `> 🌐 **Languages:** [English](README.md) \| [Русский](README.ru.md)` | പുതിയ ലാംഗ്വേജ് മെനു ജനറേറ്റ് ചെയ്യുമ്പോൾ AI ഉപയോഗിക്കുന്ന റഫറൻസ് സ്റ്റൈൽ. |
| `commit_message` | അല്ല | `docs: auto-translate README via Gemini` | ഗിറ്റ് (git) കമ്മിറ്റ് മെസ്സേജിനായി ഉപയോഗിക്കുന്ന ടെക്സ്റ്റ്. |
| `model` | അല്ല | `gemini-3.1-pro-preview` | ഉപയോഗിക്കേണ്ട ജെമിനി മോഡൽ. |
| `source_file` | അല്ല | `README.md` | വിവർത്തനം ചെയ്യേണ്ട അടിസ്ഥാന ഫയൽ. |

## 🔑 ഗൂഗിൾ ജെമിനി (Google Gemini) API കീ എങ്ങനെ ലഭിക്കും?

ഈ ആക്ഷൻ ഉപയോഗിക്കുന്നതിന്, നിങ്ങൾക്ക് Google AI Studio-യിൽ നിന്നുള്ള ഒരു സൗജന്യ API കീ ആവശ്യമാണ്:

1. [Google AI Studio](https://aistudio.google.com/) സന്ദർശിക്കുക.
2. നിങ്ങളുടെ ഗൂഗിൾ അക്കൗണ്ട് ഉപയോഗിച്ച് സൈൻ ഇൻ ചെയ്യുക.
3. ഇടതുവശത്തുള്ള നാവിഗേഷൻ മെനുവിൽ, **Get API key** എന്നതിൽ ക്ലിക്ക് ചെയ്യുക.
4. **Create API key** ബട്ടൺ ക്ലിക്ക് ചെയ്യുക.
5. നിർമ്മിക്കപ്പെട്ട കീ കോപ്പി (copy) ചെയ്യുക.
6. നിങ്ങളുടെ GitHub റെപ്പോസിറ്ററിയിൽ -> **Settings** -> **Secrets and variables** -> **Actions** എന്നതിലേക്ക് പോവുക.
7. **New repository secret** എന്നതിൽ ക്ലിക്ക് ചെയ്ത്, അതിന് `GEMINI_API_KEY` എന്ന് പേര് നൽകുക, തുടർന്ന് സീക്രട്ട് ഫീൽഡിൽ നിങ്ങളുടെ കീ പേസ്റ്റ് ചെയ്ത് സേവ് ചെയ്യുക.

## 🔑 സ്റ്റാൻഡേർഡ് GitHub ടോക്കൺ എങ്ങനെ കോൺഫിഗർ ചെയ്യാം?

കമ്മിറ്റുകൾ പുഷ് ചെയ്യാനോ പുൾ റിക്വസ്റ്റുകൾ നിർമ്മിക്കാനോ ഈ ആക്ഷൻ ബിൽറ്റ്-ഇൻ ആയിട്ടുള്ള `GITHUB_TOKEN` ആണ് ഉപയോഗിക്കുന്നത്. നിങ്ങൾ സ്വയം ഒരു പേഴ്സണൽ ആക്സസ് ടോക്കൺ (PAT) നിർമ്മിക്കേണ്ട **ആവശ്യമില്ല**, എന്നാൽ ഡിഫോൾട്ട് ടോക്കണിന് ശരിയായ അനുമതികൾ (permissions) ഉണ്ടെന്ന് നിങ്ങൾ **ഉറപ്പുവരുത്തേണ്ടതുണ്ട്**:

1. നിങ്ങളുടെ റെപ്പോസിറ്ററിയിലെ **Settings** -> **Actions** -> **General** എന്നതിലേക്ക് പോവുക.
2. താഴേക്ക് സ്ക്രോൾ ചെയ്ത് **Workflow permissions** എന്ന സെക്ഷനിൽ എത്തുക.
3. **Read and write permissions** തിരഞ്ഞെടുക്കുക.
4. **Save** ക്ലിക്ക് ചെയ്യുക.
5. നിങ്ങളുടെ വർക്ക്ഫ്ലോ YAML ഫയലിൽ, `github_token` ഇൻപുട്ടിലേക്ക് `${{ secrets.GITHUB_TOKEN }}` നൽകുക (ഉപയോഗക്രമം ഉദാഹരണത്തിൽ കാണിച്ചിരിക്കുന്നത് പോലെ).

## 📄 ലൈസൻസ് (License)

ഈ പ്രോജക്റ്റ് MIT ലൈസൻസിന് കീഴിലാണ് ലൈസൻസ് ചെയ്തിരിക്കുന്നത് - കൂടുതൽ വിവരങ്ങൾക്ക് [LICENSE](https://github.com/artryazanov/gemini-readme-translator/blob/main/LICENSE) ഫയൽ കാണുക.