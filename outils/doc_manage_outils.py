import requests

def get_content_from_url(url: str) -> str:
    """
    Get the content of the url.
    """
    try:
        return requests.get(url).text
    except Exception as e:
        print(f"Error getting content from url: {e}")
        return ""

def generate_document(text: str) -> str:
    try:
        with open("summary.md", "w") as f:
            f.write(text)
        return "summary.md"
    except Exception as e:
        print(f"Error generating document: {e}")
        return text
