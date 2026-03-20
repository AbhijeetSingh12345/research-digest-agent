# import requests
# from bs4 import BeautifulSoup

# def fetch_url(url):
#     try:
#         res = requests.get(url, timeout=5)
#         soup = BeautifulSoup(res.text, "html.parser")
#         text = soup.get_text(separator=" ", strip=True)

#         if not text or len(text) < 100:
#             return None

#         return {
#             "source": url,
#             "text": text,
#             "length": len(text)
#         }
#     except:
#         return None

from bs4 import BeautifulSoup
import requests

def fetch_url(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        res = requests.get(url, headers=headers, timeout=10)

        soup = BeautifulSoup(res.text, "html.parser")
        text = soup.get_text(separator=". ", strip=True)

        if not text or len(text) < 100:
            return None

        return {
            "source": url,
            "text": text,
            "length": len(text)
        }

    except:
        return None


def load_urls(file_path):
    with open(file_path, "r") as f:
        return [line.strip() for line in f.readlines()]