from playwright.sync_api import sync_playwright
import subprocess
import time


def test_streamlit_e2e():
    """Test E2E avec navigateur réel"""
    process = subprocess.Popen(
        ["streamlit", "run", "src/main.py", "--server.headless=true"]
    )
    time.sleep(5)

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto("http://localhost:8501")

            # Interagir avec le chat
            page.fill('[data-testid="stChatInputTextArea"]', "Bonjour")
            page.press('[data-testid="stChatInputSubmitButton"]', "Enter")

            time.sleep(2)

            browser.close()
    finally:
        process.kill()
