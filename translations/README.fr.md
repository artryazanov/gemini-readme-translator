> 🌐 **Languages:** [English](../README.md) | [Русский](README.ru.md) | [ไทย](README.th.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [हिन्दी](README.hi.md) | [Español](README.es.md) | [Français](README.fr.md) | [العربية](README.ar.md) | [বাংলা](README.bn.md) | [Português](README.pt.md) | [اردو](README.ur.md) | [Bahasa Indonesia](README.id.md) | [Deutsch](README.de.md) | [日本語](README.ja.md) | [मराठी](README.mr.md) | [తెలుగు](README.te.md) | [Türkçe](README.tr.md) | [தமிழ்](README.ta.md) | [Tiếng Việt](README.vi.md) | [한국어](README.ko.md) | [Kiswahili](README.sw.md) | [Italiano](README.it.md) | [ગુજરાતી](README.gu.md) | [فارسی](README.fa.md) | [ಕನ್ನಡ](README.kn.md) | [Polski](README.pl.md) | [മലയാളം](README.ml.md) | [Українська](README.uk.md) | [Română](README.ro.md) | [Nederlands](README.nl.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Српски](README.sr.md) | [עברית](README.he.md) | [Български](README.bg.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Lietuvių](README.lt.md) | [Slovenščina](README.sl.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md)

# Gemini README Translator


[![Latest Release](https://img.shields.io/github/v/release/artryazanov/gemini-readme-translator?sort=semver)](https://github.com/artryazanov/gemini-readme-translator/releases)
[![Run Tests and E2E](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml)
[![Lint Workflows and Code](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml)
[![Update Major Tag](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml)
[![codecov](https://codecov.io/gh/artryazanov/gemini-readme-translator/graph/badge.svg)](https://codecov.io/gh/artryazanov/gemini-readme-translator)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Une GitHub Action qui traduit automatiquement votre `README.md` dans plusieurs langues en utilisant l'API Gemini. Elle injecte intelligemment un menu de navigation linguistique interconnecté dans tous les fichiers et effectue automatiquement un commit des modifications.

## 🚀 Fonctionnalités
* **Support multilingue :** Générez des README pour plusieurs langues en une seule exécution.
* **Navigation automatique :** Insère et maintient automatiquement un menu de changement de langue standard en haut de vos fichiers (peut être désactivé). L'IA le stylise automatiquement !
* **Style personnalisé :** Vous pouvez fournir un paramètre de style de menu personnalisé afin que l'IA formate le sélecteur de langue exactement comme vous le souhaitez.
* **Suivi des jetons (tokens) :** Affiche les statistiques d'utilisation des jetons Gemini.

## 🛠 Utilisation

Créez un fichier de workflow (par exemple, `.github/workflows/translate.yml`) :

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

## 📥 Entrées

| Entrée | Requis | Défaut | Description |
| --- | --- | --- | --- |
| `api_key` | Oui |  | Votre clé API Google Gemini. |
| `github_token` | Oui |  | Jeton GitHub standard (`${{ secrets.GITHUB_TOKEN }}`). |
| `languages` | Oui |  | Langues cibles séparées par des virgules (ex. `ru, es`). |
| `output_dir` | Non | | Répertoire où enregistrer les fichiers traduits. Par défaut, il s'agit du répertoire du fichier source. |
| `add_language_menu` | Non | `true` | Définissez sur `false` pour désactiver la génération automatique du menu des langues. |
| `menu_style` | Non | `> 🌐 **Languages:** [English](README.md) \| [Русский](README.ru.md)` | Le style de référence que l'IA utilise lors de la génération d'un nouveau menu des langues. |
| `commit_message` | Non | `docs: auto-translate README via Gemini` | Texte utilisé pour le message de commit git. |
| `model` | Non | `gemini-3.1-pro-preview` | Le modèle Gemini à utiliser. |
| `source_file` | Non | `README.md` | Le fichier de base à traduire. |

## 📤 Sorties

| Sortie | Description |
| --- | --- |
| `total_tokens_used` | Nombre total de jetons traités. |
| `input_tokens_used` | Nombre de jetons dans les prompts d'entrée. |
| `output_tokens_used` | Nombre de jetons générés dans les réponses. |
| `duration_seconds` | Temps de traitement total en secondes. |

## 🔑 Comment obtenir une clé API Google Gemini

Pour utiliser cette action, vous avez besoin d'une clé API gratuite de Google AI Studio :

1. Allez sur [Google AI Studio](https://aistudio.google.com/).
2. Connectez-vous avec votre compte Google.
3. Dans le menu de navigation à gauche, cliquez sur **Get API key**.
4. Cliquez sur le bouton **Create API key**.
5. Copiez la clé générée.
6. Allez dans votre dépôt GitHub -> **Settings** -> **Secrets and variables** -> **Actions**.
7. Cliquez sur **New repository secret**, nommez-le `GEMINI_API_KEY`, collez votre clé dans le champ Secret, et enregistrez.

## 🔑 Comment configurer le Jeton GitHub Standard

Cette action utilise le `GITHUB_TOKEN` intégré pour pousser les commits. Vous **n'avez pas** besoin de créer manuellement un Personal Access Token (PAT), mais vous **devez** vous assurer que le jeton par défaut possède les bonnes permissions :

1. Allez dans les paramètres de votre dépôt (**Settings**) -> **Actions** -> **General**.
2. Faites défiler jusqu'à la section **Workflow permissions**.
3. Sélectionnez **Read and write permissions**.
4. Cliquez sur **Save**.
5. Dans votre fichier YAML de workflow, passez simplement `${{ secrets.GITHUB_TOKEN }}` à l'entrée `github_token` (comme indiqué dans l'exemple d'utilisation).

## 📄 Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](https://github.com/artryazanov/gemini-readme-translator/blob/main/LICENSE) pour plus de détails.