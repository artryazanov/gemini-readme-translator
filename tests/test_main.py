import os
import sys
import pytest
from unittest.mock import patch, MagicMock

# Add project root to sys.path so we can import main
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import main

@pytest.fixture
def mock_env(monkeypatch, tmp_path):
    source_file = tmp_path / "README.md"
    source_file.write_text("# Hello World\nThis is a test.", encoding="utf-8")
    
    github_output = tmp_path / "github_output.txt"
    
    monkeypatch.setenv("INPUT_API_KEY", "fake_api_key")
    monkeypatch.setenv("INPUT_LANGUAGES", "ru, es")
    monkeypatch.setenv("INPUT_MODEL", "gemini-3.1-pro-preview")
    monkeypatch.setenv("INPUT_SOURCE_FILE", str(source_file))
    monkeypatch.setenv("INPUT_ADD_LANGUAGE_MENU", "true")
    monkeypatch.setenv("INPUT_MENU_STYLE", "TEST STYLE")
    monkeypatch.setenv("GITHUB_OUTPUT", str(github_output))
    
    return {
        "source_file": source_file,
        "github_output": github_output,
        "tmp_path": tmp_path
    }

@patch("main.genai.Client")
def test_main_success(mock_client_class, mock_env):
    # Setup mock client behavior
    mock_client = MagicMock()
    mock_client_class.return_value = mock_client
    
    # Create fake response for AI
    def fake_generate_content(model, contents):
        response = MagicMock()
        response.usage_metadata.prompt_token_count = 10
        response.usage_metadata.candidates_token_count = 20
        response.usage_metadata.total_token_count = 30
        
        # Determine if it's the menu generation prompt or translation prompt
        if "expert markdown formatter" in contents:
            response.text = "FAKE MENU\n# Hello World\nThis is a test."
        elif "into ru" in contents:
            response.text = "FAKE MENU\n# Привет мир\nЭто тест."
        else:
            response.text = "FAKE MENU\n# Hola Mundo\nEsto es una prueba."
            
        return response

    mock_client.models.generate_content.side_effect = fake_generate_content
    
    # Run the main function
    main.main()
    
    # Assertions
    mock_client_class.assert_called_once_with(api_key="fake_api_key")
    
    # Check that the original file was updated with the menu
    updated_source = mock_env["source_file"].read_text(encoding="utf-8")
    assert "FAKE MENU" in updated_source
    
    # Check that translated files were created
    ru_file = mock_env["tmp_path"] / "README.ru.md"
    es_file = mock_env["tmp_path"] / "README.es.md"
    
    assert ru_file.exists()
    assert "Привет мир" in ru_file.read_text(encoding="utf-8")
    
    assert es_file.exists()
    assert "Hola Mundo" in es_file.read_text(encoding="utf-8")
    
    # Check GITHUB_OUTPUT
    output_content = mock_env["github_output"].read_text(encoding="utf-8")
    assert "input_tokens_used=" in output_content
    assert "output_tokens_used=" in output_content
    assert "total_tokens_used=" in output_content
    assert "duration_seconds=" in output_content

@patch("main.sys.exit")
def test_main_missing_api_key(mock_exit, monkeypatch):
    mock_exit.side_effect = Exception("SystemExit raised")
    monkeypatch.delenv("INPUT_API_KEY", raising=False)
    
    with pytest.raises(Exception, match="SystemExit raised"):
        main.main()
    
    mock_exit.assert_called_once_with(1)

@patch("main.sys.exit")
def test_main_missing_languages(mock_exit, monkeypatch):
    mock_exit.side_effect = Exception("SystemExit raised")
    monkeypatch.setenv("INPUT_API_KEY", "fake_key")
    monkeypatch.setenv("INPUT_LANGUAGES", "   ") # empty languages
    
    with pytest.raises(Exception, match="SystemExit raised"):
        main.main()
    
    mock_exit.assert_called_once_with(1)

@patch("main.genai.Client")
def test_main_default_menu_style(mock_client_class, mock_env, monkeypatch):
    monkeypatch.delenv("INPUT_MENU_STYLE", raising=False)
    mock_client = MagicMock()
    mock_client_class.return_value = mock_client
    
    def fake_generate_content(model, contents):
        response = MagicMock()
        response.usage_metadata.prompt_token_count = 10
        response.usage_metadata.candidates_token_count = 20
        response.usage_metadata.total_token_count = 30
        
        if "expert markdown formatter" in contents:
            assert "[English]" in contents
            assert "[Русский]" in contents
            assert "[中文]" in contents
            response.text = "FAKE MENU\n# Hello World"
        else:
            response.text = "TRANSLATED"
        return response
    
    mock_client.models.generate_content.side_effect = fake_generate_content
    main.main()

@patch("main.genai.Client")
def test_main_no_menu_generation(mock_client_class, mock_env, monkeypatch):
    monkeypatch.setenv("INPUT_ADD_LANGUAGE_MENU", "false")
    mock_client = MagicMock()
    mock_client_class.return_value = mock_client
    
    def fake_generate_content(model, contents):
        response = MagicMock()
        response.usage_metadata.prompt_token_count = 10
        response.usage_metadata.candidates_token_count = 20
        response.usage_metadata.total_token_count = 30
        response.text = "NO MENU # Hola"
        return response
    
    mock_client.models.generate_content.side_effect = fake_generate_content
    main.main()
    
    updated_source = mock_env["source_file"].read_text(encoding="utf-8")
    assert "FAKE MENU" not in updated_source

@patch("main.genai.Client")
def test_main_translation_error(mock_client_class, mock_env):
    mock_client = MagicMock()
    mock_client_class.return_value = mock_client
    
    def fake_generate_content(model, contents):
        if "expert markdown formatter" in contents:
            response = MagicMock()
            response.usage_metadata.prompt_token_count = 10
            response.usage_metadata.candidates_token_count = 20
            response.usage_metadata.total_token_count = 30
            response.text = "OK"
            return response
        else:
            raise Exception("API Error")
            
    mock_client.models.generate_content.side_effect = fake_generate_content
    
    main.main()
    
    ru_file = mock_env["tmp_path"] / "README.ru.md"
    assert not ru_file.exists()
