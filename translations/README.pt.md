> 🌐 **Languages:** [English](../README.md) | [Русский](README.ru.md) | [ไทย](README.th.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [हिन्दी](README.hi.md) | [Español](README.es.md) | [Français](README.fr.md) | [العربية](README.ar.md) | [বাংলা](README.bn.md) | [Português](README.pt.md) | [اردو](README.ur.md) | [Bahasa Indonesia](README.id.md) | [Deutsch](README.de.md) | [日本語](README.ja.md) | [मराठी](README.mr.md) | [తెలుగు](README.te.md) | [Türkçe](README.tr.md) | [தமிழ்](README.ta.md) | [Tiếng Việt](README.vi.md) | [한국어](README.ko.md) | [Kiswahili](README.sw.md) | [Italiano](README.it.md) | [ગુજરાતી](README.gu.md) | [فارسی](README.fa.md) | [ಕನ್ನಡ](README.kn.md) | [Polski](README.pl.md) | [മലയാളം](README.ml.md) | [Українська](README.uk.md) | [Română](README.ro.md) | [Nederlands](README.nl.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Српски](README.sr.md) | [עברית](README.he.md) | [Български](README.bg.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Lietuvių](README.lt.md) | [Slovenščina](README.sl.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md)

# Gemini README Translator


[![Latest Release](https://img.shields.io/github/v/release/artryazanov/gemini-readme-translator?sort=semver)](https://github.com/artryazanov/gemini-readme-translator/releases)
[![Run Tests and E2E](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml)
[![Lint Workflows and Code](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml)
[![Update Major Tag](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml)
[![codecov](https://codecov.io/gh/artryazanov/gemini-readme-translator/graph/badge.svg)](https://codecov.io/gh/artryazanov/gemini-readme-translator)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Uma GitHub Action que traduz automaticamente seu `README.md` para vários idiomas usando a API do Gemini. Ela injeta de forma inteligente um menu de navegação de idiomas com links cruzados em todos os arquivos e faz o commit automático das alterações.

## 🚀 Recursos
* **Suporte a Vários Idiomas:** Gere READMEs para vários idiomas em uma única execução.
* **Navegação Automática:** Insere e mantém automaticamente um menu padrão de troca de idiomas no topo dos seus arquivos (pode ser desativado). A IA o estiliza automaticamente!
* **Estilo Personalizado:** Você pode fornecer um parâmetro de estilo de menu personalizado para que a IA formate o seletor de idiomas exatamente como você deseja.
* **Rastreamento de Tokens:** Gera estatísticas de uso de tokens do Gemini.

## 🛠 Uso

Crie um arquivo de workflow (ex: `.github/workflows/translate.yml`):

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

## 📥 Entradas

| Entrada | Obrigatório | Padrão | Descrição |
| --- | --- | --- | --- |
| `api_key` | Sim |  | Sua Chave de API do Google Gemini. |
| `github_token` | Sim |  | Token padrão do GitHub (`${{ secrets.GITHUB_TOKEN }}`). |
| `languages` | Sim |  | Idiomas de destino separados por vírgula (ex: `ru, es`). |
| `output_dir` | Não | | Diretório para salvar os arquivos traduzidos. O padrão é o diretório do arquivo de origem. |
| `add_language_menu` | Não | `true` | Defina como `false` para desativar a geração automática do menu de idiomas. |
| `use_absolute_links`| Não | `true` | Defina como `false` para usar links relativos em vez de URLs absolutos do GitHub nos menus de idioma gerados. |
| `menu_style` | Não | `> 🌐 **Languages:** [English](README.md) \| [Русский](README.ru.md)` | O estilo de referência que a IA usa ao gerar um novo menu de idiomas. |
| `commit_message` | Não | `docs: auto-translate README via Gemini` | Texto usado para a mensagem do git commit. |
| `model` | Não | `gemini-3.1-pro-preview` | O modelo do Gemini a ser usado. |
| `source_file` | Não | `README.md` | O arquivo base para traduzir. |

## 📤 Saídas

| Saída | Descrição |
| --- | --- |
| `total_tokens_used` | Número total de tokens processados. |
| `input_tokens_used` | Número de tokens nos prompts de entrada. |
| `output_tokens_used` | Número de tokens gerados nas respostas. |
| `duration_seconds` | Tempo total de processamento em segundos. |

## 🔑 Como obter uma Chave de API do Google Gemini

Para usar esta action, você precisa de uma chave de API gratuita do Google AI Studio:

1. Acesse o [Google AI Studio](https://aistudio.google.com/).
2. Faça login com sua conta do Google.
3. No menu de navegação à esquerda, clique em **Get API key** (Obter chave de API).
4. Clique no botão **Create API key** (Criar chave de API).
5. Copie a chave gerada.
6. Vá para o seu repositório GitHub -> **Settings** (Configurações) -> **Secrets and variables** (Segredos e variáveis) -> **Actions**.
7. Clique em **New repository secret** (Novo segredo de repositório), nomeie-o como `GEMINI_API_KEY`, cole sua chave no campo Secret (Segredo) e salve.

## 🔑 Como configurar o Token Padrão do GitHub

Esta action usa o `GITHUB_TOKEN` integrado para fazer o push dos commits. Você **não** precisa criar um Personal Access Token (PAT) manualmente, mas **deve** garantir que o token padrão tenha as permissões corretas:

1. Vá para **Settings** (Configurações) do seu repositório -> **Actions** -> **General** (Geral).
2. Role para baixo até a seção **Workflow permissions** (Permissões de fluxo de trabalho).
3. Selecione **Read and write permissions** (Permissões de leitura e gravação).
4. Clique em **Save** (Salvar).
5. No seu workflow em YAML, basta passar `${{ secrets.GITHUB_TOKEN }}` para a entrada `github_token` (como mostrado no exemplo de uso).

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - consulte o arquivo [LICENSE](https://github.com/artryazanov/gemini-readme-translator/blob/main/LICENSE) para obter detalhes.