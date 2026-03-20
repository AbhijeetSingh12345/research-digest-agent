import json
import re


# 🧹 Clean text (remove extra spaces, newlines, junk)
def clean_text(text):
    text = re.sub(r'\s+', ' ', text)  # remove extra whitespace
    text = text.strip()
    return text


# 🛡️ Safe JSON parsing (LLM often returns broken JSON)
def safe_json_loads(text):
    try:
        return json.loads(text)
    except:
        # Try to fix common issues
        try:
            text = text.strip()

            # Remove trailing commas
            text = re.sub(r",\s*}", "}", text)
            text = re.sub(r",\s*]", "]", text)

            return json.loads(text)
        except:
            return []


# 📏 Split long text into chunks (for LLM token limits)
def chunk_text(text, max_length=4000):
    return [text[i:i + max_length] for i in range(0, len(text), max_length)]


# 🖨️ Simple logger
def log(message):
    print(f"[INFO] {message}")


# ⚠️ Warning logger
def warn(message):
    print(f"[WARNING] {message}")


# ❌ Error logger
def error(message):
    print(f"[ERROR] {message}")