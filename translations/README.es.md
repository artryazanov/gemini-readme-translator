> 🌐 **Languages:** [English](../README.md) | [Русский](README.ru.md) | [ไทย](README.th.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [हिन्दी](README.hi.md) | [Español](README.es.md) | [Français](README.fr.md) | [العربية](README.ar.md) | [বাংলা](README.bn.md) | [Português](README.pt.md) | [اردو](README.ur.md) | [Bahasa Indonesia](README.id.md) | [Deutsch](README.de.md) | [日本語](README.ja.md) | [मराठी](README.mr.md) | [తెలుగు](README.te.md) | [Türkçe](README.tr.md) | [தமிழ்](README.ta.md) | [Tiếng Việt](README.vi.md) | [한국어](README.ko.md) | [Kiswahili](README.sw.md) | [Italiano](README.it.md) | [ગુજરાતી](README.gu.md) | [فارسی](README.fa.md) | [ಕನ್ನಡ](README.kn.md) | [Polski](README.pl.md) | [മലയാളം](README.ml.md) | [Українська](README.uk.md) | [Română](README.ro.md) | [Nederlands](README.nl.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Čeština](README.cs.md) | [Српски](README.sr.md) | [עברית](README.he.md) | [Български](README.bg.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Lietuvių](README.lt.md) | [Slovenščina](README.sl.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md)

# Gemini README Translator


[![Latest Release](https://img.shields.io/github/v/release/artryazanov/gemini-readme-translator?sort=semver)](https://github.com/artryazanov/gemini-readme-translator/releases)
[![Run Tests and E2E](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/tests.yml)
[![Lint Workflows and Code](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/lint.yml)
[![Update Major Tag](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml/badge.svg)](https://github.com/artryazanov/gemini-readme-translator/actions/workflows/update-major-tag.yml)
[![codecov](https://codecov.io/gh/artryazanov/gemini-readme-translator/graph/badge.svg)](https://codecov.io/gh/artryazanov/gemini-readme-translator)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Una GitHub Action que traduce automáticamente tu `README.md` a múltiples idiomas utilizando la API de Gemini. Inyecta de manera inteligente un menú de navegación de idiomas interconectado en todos los archivos y realiza los commits de los cambios automáticamente.

## 🚀 Características
* **Soporte multilingüe:** Genera archivos README en múltiples idiomas en una sola ejecución.
* **Navegación automática:** Inserta y mantiene automáticamente un menú estándar para cambiar de idioma en la parte superior de tus archivos (puede ser desactivado). ¡La IA lo estiliza automáticamente!
* **Estilo personalizado:** Puedes proporcionar un parámetro de estilo de menú personalizado para que la IA formatee el selector de idiomas exactamente como desees.
* **Seguimiento de tokens:** Muestra estadísticas del uso de tokens de Gemini.

## 🛠 Uso

Crea un archivo de flujo de trabajo (workflow) (por ejemplo, `.github/workflows/translate.yml`):

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

| Entrada | Requerido | Por defecto | Descripción |
| --- | --- | --- | --- |
| `api_key` | Sí |  | Tu clave API de Google Gemini. |
| `github_token` | Sí |  | Token estándar de GitHub (`${{ secrets.GITHUB_TOKEN }}`). |
| `languages` | Sí |  | Idiomas de destino separados por comas (ej. `ru, es`). |
| `output_dir` | No | | Directorio para guardar los archivos traducidos. Por defecto es el directorio del archivo de origen. |
| `add_language_menu` | No | `true` | Establécelo en `false` para desactivar la generación automática del menú de idiomas. |
| `menu_style` | No | `> 🌐 **Languages:** [English](README.md) \| [Русский](README.ru.md)` | El estilo de referencia que la IA usa al generar un nuevo menú de idiomas. |
| `commit_message` | No | `docs: auto-translate README via Gemini` | Texto utilizado para el mensaje de commit de git. |
| `model` | No | `gemini-3.1-pro-preview` | El modelo de Gemini a utilizar. |
| `source_file` | No | `README.md` | El archivo base para traducir. |

## 📤 Salidas

| Salida | Descripción |
| --- | --- |
| `total_tokens_used` | Número total de tokens procesados. |
| `input_tokens_used` | Número de tokens en los prompts de entrada. |
| `output_tokens_used` | Número de tokens generados en las respuestas. |
| `duration_seconds` | Tiempo total de procesamiento en segundos. |

## 🔑 Cómo obtener una Clave API de Google Gemini

Para usar esta acción, necesitas una clave API gratuita de Google AI Studio:

1. Ve a [Google AI Studio](https://aistudio.google.com/).
2. Inicia sesión con tu cuenta de Google.
3. En el menú de navegación de la izquierda, haz clic en **Get API key** (Obtener clave API).
4. Haz clic en el botón **Create API key** (Crear clave API).
5. Copia la clave generada.
6. Ve a tu repositorio de GitHub -> **Settings** (Configuración) -> **Secrets and variables** (Secretos y variables) -> **Actions** (Acciones).
7. Haz clic en **New repository secret** (Nuevo secreto del repositorio), nómbralo `GEMINI_API_KEY`, pega tu clave en el campo *Secret* (Secreto) y guarda.

## 🔑 Cómo configurar el Token estándar de GitHub

Esta acción utiliza el `GITHUB_TOKEN` integrado para hacer *push* de los commits. **No** necesitas crear un Token de Acceso Personal (PAT) manualmente, pero **debes** asegurarte de que el token por defecto tenga los permisos correctos:

1. Ve a tu repositorio en **Settings** (Configuración) -> **Actions** (Acciones) -> **General**.
2. Desplázate hacia abajo hasta la sección **Workflow permissions** (Permisos de flujo de trabajo).
3. Selecciona **Read and write permissions** (Permisos de lectura y escritura).
4. Haz clic en **Save** (Guardar).
5. En tu YAML de flujo de trabajo, simplemente pasa `${{ secrets.GITHUB_TOKEN }}` a la entrada `github_token` (como se muestra en el ejemplo de uso).

## 📄 Licencia

Este proyecto está bajo la Licencia MIT; consulta el archivo [LICENSE](https://github.com/artryazanov/gemini-readme-translator/blob/main/LICENSE) para más detalles.