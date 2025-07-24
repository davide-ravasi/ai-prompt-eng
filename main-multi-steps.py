from dotenv import load_dotenv
import google.generativeai as genai
import os
from outils.prompt_outils import clean_content, generate_summary, format_text_to_markdown
from outils.doc_manage_outils import get_content_from_url, generate_document

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def main():
    """
    Main function to get user url, generate an X post with the content of the url, and print it.
    """
    print("Hello from first-python! Let's create a summary with a content from a url.")
    user_url = input("What is the url of the content you want to summarize? ")

    # Get the content of the url
    content = get_content_from_url(user_url)
    print("This is the HTML content:")

    # Clean the content
    cleaned_content = clean_content(content)

    # Generate a summary of the content
    summary_content = generate_summary(cleaned_content)

    # Format the content in a markdown format
    markdown_content = format_text_to_markdown(summary_content)

    # Generate a document with the content
    document_path = generate_document(markdown_content)

    print("This is the path of the created document:")
    print(document_path)


if __name__ == "__main__":
    main()

# IDEAS

# - add a function that generate a filename from the article title