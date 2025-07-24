import google.generativeai as genai

def clean_content(content: str) -> str:
    try:
        model = genai.GenerativeModel("gemini-2.0-flash")
        response = model.generate_content(f"Extract the text from the following HTML content and remove all the html tags and replace characters unicodes by their corresponding characters. Remove all the footer informations, header, and other informations that are not the content of the article. This is the content: {content}")
        return response.text
    except Exception as e:
        print(f"Error cleaning content: {e}")
        return content

def generate_summary(content: str) -> str:
    try:
        model = genai.GenerativeModel("gemini-2.0-flash")
        response = model.generate_content(f"Generate a summary of the following content: {content}")
        return response.text
    except Exception as e:
        print(f"Error generating summary: {e}")
        return content

def format_text_to_markdown(text: str) -> str:
    try:
        model = genai.GenerativeModel("gemini-2.0-flash")
        response = model.generate_content(f"Format the following text to a markdown format: {text}")
        return response.text
    except Exception as e:
        print(f"Error formatting text to markdown: {e}")
        return text