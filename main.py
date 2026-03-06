import os
import sys
import time
from google import genai

def write_github_output(key: str, value: str):
    output_file = os.environ.get('GITHUB_OUTPUT')
    if output_file:
        with open(output_file, 'a') as f:
            f.write(f"{key}={value}\n")

def process_response(response, stats):
    if hasattr(response, 'usage_metadata') and response.usage_metadata:
        stats["input_tokens"] += getattr(response.usage_metadata, 'prompt_token_count', 0)
        stats["output_tokens"] += getattr(response.usage_metadata, 'candidates_token_count', 0)
        stats["total_tokens"] += getattr(response.usage_metadata, 'total_token_count', 0)
    
    text = response.text.strip()
    # Remove potential markdown block wrappers from AI output
    if text.startswith("```markdown"):
        text = text[11:].strip()
    if text.endswith("```"):
        text = text[:-3].strip()
    return text

def main():
    api_key = os.environ.get("INPUT_API_KEY")
    if not api_key:
        print("Error: INPUT_API_KEY is not set.")
        sys.exit(1)

    languages_input = os.environ.get("INPUT_LANGUAGES", "")
    model_name = os.environ.get("INPUT_MODEL", "gemini-3.1-pro-preview")
    source_file = os.environ.get("INPUT_SOURCE_FILE", "README.md")
    add_language_menu = os.environ.get("INPUT_ADD_LANGUAGE_MENU", "true").lower() == "true"
    menu_style = os.environ.get("INPUT_MENU_STYLE", "> 🌐 **Languages:** [English](README.md) | [Русский](README.ru.md) | [中文](README.zh-CN.md)")
    output_dir = os.environ.get("INPUT_OUTPUT_DIR", "").strip()

    target_langs = [lang.strip() for lang in languages_input.split(",") if lang.strip()]
    if not target_langs:
        print("Error: No target languages specified.")
        sys.exit(1)

    target_files = {}
    for lang in target_langs:
        base_name_only = os.path.splitext(os.path.basename(source_file))[0]
        ext = os.path.splitext(source_file)[1]
        if output_dir:
            target_files[lang] = os.path.join(output_dir, f"{base_name_only}.{lang}{ext}")
        else:
            base_name = os.path.splitext(source_file)[0]
            target_files[lang] = f"{base_name}.{lang}{ext}"
            
    if output_dir and not os.path.exists(output_dir):
        try:
            os.makedirs(output_dir, exist_ok=True)
        except Exception as e:
            print(f"Error creating output directory: {e}")
            sys.exit(1)

    client = genai.Client(api_key=api_key)

    stats = {"input_tokens": 0, "output_tokens": 0, "total_tokens": 0}
    start_time = time.time()

    if not os.path.exists(source_file):
        print(f"Error: Source file {source_file} not found.")
        sys.exit(1)

    with open(source_file, "r", encoding="utf-8") as f:
        original_content = f.read()


    content_to_translate = original_content

    # 1. Handle Language Menu Generation (if enabled)
    if add_language_menu:
        required_links_text = f"English -> {source_file}\n"
        for lang in target_langs:
            required_links_text += f"{lang} -> {target_files[lang]}\n"
        
        print(f"Updating original {source_file} to ensure correct language menu...")
        prompt_original = f"""
        You are an expert markdown formatter. I have a README file. 
        Your task is to ensure it has a language navigation menu linking exactly to these files:
        
        {required_links_text}
        
        Rules:
        1. If a language navigation menu already exists ANYWHERE in the file:
           - Update its links to point EXACTLY to the destinations listed above.
           - Ensure the names of the languages are written beautifully and correctly natively.
           - PRESERVE the user's original styling, formatting, emojis, separators, and HTML/Markdown structure.
           - PRESERVE the exact location of the menu in the file.
           - Remove any old language links that are not in the list above.
        2. If NO language navigation menu exists:
           - Insert a new menu at the VERY TOP of the file.
           - Generate this new menu using the following requested style as a reference:
             {menu_style}
           - Format the language names nicely (e.g., 'English', 'Русский', 'Español', '中文', etc.).
        3. DO NOT translate, summarize, or change ANY other text, formatting, code blocks, or links in the document.
        4. Output ONLY the raw markdown of the updated file. No conversational text.
        
        Document:
        {original_content}
        """
        try:
            res_original = client.models.generate_content(
                model=model_name,
                contents=prompt_original
            )
            content_to_translate = process_response(res_original, stats)

            with open(source_file, "w", encoding="utf-8") as f:
                f.write(content_to_translate)
            print(f"Original file {source_file} updated with menu.")
        except Exception as e:
            print(f"Error updating original file: {e}")
            sys.exit(1)
    else:
        print("Language menu generation is disabled. Skipping original file update.")

    # 2. Translate to target languages
    for lang in target_langs:
        target_file = target_files[lang]
        print(f"Translating to {lang} -> {target_file}...")

        menu_rule = "1. Find the language navigation menu in the text and keep the menu items, links, and structure exactly as they appear in the original text. Do not translate the language names in the menu." if add_language_menu else "1. Do not generate or add any language navigation menus."

        prompt_translate = f"""
        You are an expert technical translator. Translate the following README markdown content into {lang}.
        
        Rules:
        {menu_rule}
        2. Preserve all markdown formatting, code blocks, URLs, image links, and badges exactly as they are.
        3. Translate only the descriptive text and headers.
        4. Output ONLY the raw translated markdown. No conversational text.
        
        Content to translate:
        {content_to_translate}
        """
        
        try:
            res_translate = client.models.generate_content(
                model=model_name,
                contents=prompt_translate
            )
            translated_content = process_response(res_translate, stats)

            with open(target_file, "w", encoding="utf-8") as f:
                f.write(translated_content)
            print(f"Successfully generated {target_file}")
        except Exception as e:
            print(f"Error translating to {lang}: {e}")

    # Calculate duration and write outputs
    duration = int(time.time() - start_time)
    print("\n--- Translation Statistics ---")
    print(f"Duration: {duration}s")
    print(f"Input Tokens: {stats['input_tokens']}")
    print(f"Output Tokens: {stats['output_tokens']}")
    print(f"Total Tokens: {stats['total_tokens']}")

    write_github_output("duration_seconds", str(duration))
    write_github_output("input_tokens_used", str(stats["input_tokens"]))
    write_github_output("output_tokens_used", str(stats["output_tokens"]))
    write_github_output("total_tokens_used", str(stats["total_tokens"]))

if __name__ == "__main__":
    main()
