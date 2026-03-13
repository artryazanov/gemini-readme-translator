> 🌐 **Languages:** [English](../README.md) | [Русский](README.ru.md) | [ไทย](README.th.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [हिन्दी](README.hi.md) | [Español](README.es.md) | [Français](README.fr.md) | [العربية](README.ar.md) | [বাংলা](README.bn.md) | [Português](README.pt.md) | [اردو](README.ur.md) | [Bahasa Indonesia](README.id.md) | [Deutsch](README.de.md) | [日本語](README.ja.md) | [मराठी](README.mr.md) | [తెలుగు](README.te.md) | [Türkçe](README.tr.md) | [தமிழ்](README.ta.md) | [Tiếng Việt](README.vi.md) | [한국어](README.ko.md) | [Kiswahili](README.sw.md) | [Italiano](README.it.md) | [ગુજરાતી](README.gu.md) | [فارسی](README.fa.md) | [ಕನ್ನಡ](README.kn.md) | [Polski](README.pl.md) | [മലയാളം](README.ml.md) | [Українська](README.uk.md) | [Română](README.ro.md) | [Nederlands](README.nl.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Српски](README.sr.md) | [עברית](README.he.md) | [Български](README.bg.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Lietuvių](README.lt.md) | [Slovenščina](README.sl.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md)

# Traduttore di README con Gemini


[![Latest Release](https://img.shields.io/github/v/release/artryazanov/gemini-readme-translator?sort=semver)](https://github.com/artryazanov/gemini-readme-translator/releases)
[![Run Tests and E2E](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml)
[![Lint Workflows and Code](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml)
[![Update Major Tag](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml)
[![codecov](https://codecov.io/gh/artryazanov/gemini-readme-translator/graph/badge.svg)](https://codecov.io/gh/artryazanov/gemini-readme-translator)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Una GitHub Action che traduce automaticamente il tuo `README.md` in più lingue utilizzando l'API di Gemini. Inserisce in modo intelligente un menu di navigazione per le lingue con collegamenti incrociati in tutti i file e committa automaticamente le modifiche.

## 🚀 Caratteristiche
* **Supporto Multilingua:** Genera i README per diverse lingue in un'unica esecuzione.
* **Navigazione Automatica:** Inserisce e mantiene automaticamente un menu di selezione lingua standard in cima ai tuoi file (può essere disabilitato). L'IA lo formatta automaticamente!
* **Stile Personalizzato:** Puoi fornire un parametro per lo stile personalizzato del menu, in modo che l'IA formatti il selettore della lingua esattamente come desideri.
* **Tracciamento Token:** Restituisce in output le statistiche di utilizzo dei token di Gemini.

## 🛠 Utilizzo

Crea un file di workflow (es., `.github/workflows/translate.yml`):

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

## 📥 Input

| Input | Obbligatorio | Predefinito | Descrizione |
| --- | --- | --- | --- |
| `api_key` | Sì |  | La tua Chiave API di Google Gemini. |
| `github_token` | Sì |  | Il token standard di GitHub (`${{ secrets.GITHUB_TOKEN }}`). |
| `languages` | Sì |  | Lingue di destinazione separate da virgola (es. `ru, es`). |
| `output_dir` | No | | Directory in cui salvare i file tradotti. Per impostazione predefinita è la directory del file di origine. |
| `add_language_menu` | No | `true` | Imposta su `false` per disabilitare la generazione automatica del menu delle lingue. |
| `menu_style` | No | `> 🌐 **Languages:** [English](README.md) \| [Русский](README.ru.md)` | Lo stile di riferimento che l'IA usa durante la generazione di un nuovo menu delle lingue. |
| `commit_message` | No | `docs: auto-translate README via Gemini` | Testo usato per il messaggio di commit git. |
| `model` | No | `gemini-3.1-pro-preview` | Il modello Gemini da utilizzare. |
| `source_file` | No | `README.md` | Il file di base da tradurre. |

## 📤 Output

| Output | Descrizione |
| --- | --- |
| `total_tokens_used` | Numero totale di token elaborati. |
| `input_tokens_used` | Numero di token nei prompt di input. |
| `output_tokens_used` | Numero di token generati nelle risposte. |
| `duration_seconds` | Tempo totale di elaborazione in secondi. |

## 🔑 Come ottenere una Chiave API per Google Gemini

Per utilizzare questa action, hai bisogno di una chiave API gratuita da Google AI Studio:

1. Vai su [Google AI Studio](https://aistudio.google.com/).
2. Accedi con il tuo account Google.
3. Nel menu di navigazione a sinistra, fai clic su **Get API key**.
4. Fai clic sul pulsante **Create API key**.
5. Copia la chiave generata.
6. Vai al tuo repository GitHub -> **Settings** -> **Secrets and variables** -> **Actions**.
7. Fai clic su **New repository secret**, chiamalo `GEMINI_API_KEY`, incolla la tua chiave nel campo Secret e salva.

## 🔑 Come configurare il Token Standard di GitHub

Questa action utilizza il `GITHUB_TOKEN` integrato per inviare i commit. **Non è necessario** creare manualmente un Personal Access Token (PAT), ma **devi** assicurarti che il token predefinito abbia i permessi corretti:

1. Vai in **Settings** -> **Actions** -> **General** nel tuo repository.
2. Scorri verso il basso fino alla sezione **Workflow permissions**.
3. Seleziona **Read and write permissions**.
4. Fai clic su **Save**.
5. Nel tuo workflow YAML, passa semplicemente `${{ secrets.GITHUB_TOKEN }}` all'input `github_token` (come mostrato nell'esempio di utilizzo).

## 📄 Licenza

Questo progetto è concesso sotto licenza MIT - vedi il file [LICENSE](https://github.com/artryazanov/gemini-readme-translator/blob/main/LICENSE) per i dettagli.