import json
from dotenv import load_dotenv
import google.generativeai as genai
import os

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def generate_x_post(user_topic: str) -> str:
    """
    Calls the Gemini LLM to generate an X (Twitter) post based on a user-provided topic.
    Provides context to the LLM using distinct roles.

    Args:
        user_topic (str): The topic or content the user wants the post to be about.

    Returns:
        str: The generated X post.
    """
    print("Generating X post...")
    print("User topic: ", user_topic)

    exemples_string = ""
    with open("post-examples.json", "r") as file:
        exemples = json.load(file)
        for exemple in exemples["exemples"]:
            exemples_string += f"Title: {exemple['title']}\n"
            exemples_string += f"Content: {exemple['content']}\n\n"

    try:
        model = genai.GenerativeModel("gemini-2.0-flash")
        # Combine system instructions and user topic into a single prompt
        prompt = (
            "You are an expert social media manager, and you excel at crafting viral and highly engaging posts for X (formerly Twitter).\n"
            "Your task is to generate a post that is concise, impactful, and tailored to the topic provided by the user.\n"
            "Avoid using excessive hashtags and emojis (a few emojis are okay, but not too many).\n"
            "Keep the post short and focused, structure it in a clean, readable way, using line breaks and empty lines to enhance readability.\n\n"
            "Here are some examples of how to structure the post:\n"
            f"{exemples_string}"
            "Please use the tone, language, structure, and style of the examples provided above to generate a post that is engaging and relevant to the topic provided by the user.\n"
            "Don't use the content from the examples!\n"
            f"Title: {user_topic}\n"
            "Content:"
        )

        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        print(f"Error: {e}")
        return f"An error occurred while generating the post: {e}"

def main():
    """
    Main function to get user input, generate an X post, and print it.
    """
    print("Hello from first-python! Let's create an X post.")
    user_input = input("What should the post be about? ")

    print("\nGenerating post, please wait...")
    x_post = generate_x_post(user_input)

    print("\n--- Generated X post ---")
    print(x_post)
    print("------------------------")


if __name__ == "__main__":
    main()
