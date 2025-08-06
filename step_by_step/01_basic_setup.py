# Step 1: Basic Setup and Dependencies
# This file shows the basic imports and setup needed for the LLM color matcher

import os
import json
import google.generativeai as genai
import pandas as pd
from dotenv import load_dotenv

# Load environment variables (for API keys)
load_dotenv()

def check_dependencies():
    """
    Check if all required dependencies are available.
    """
    print("=== Checking Dependencies ===")
    
    # Check if pandas is available
    try:
        print("✅ pandas is available")
    except ImportError:
        print("❌ pandas is not installed")
        return False
    
    # Check if we can import Google Generative AI
    try:
        import google.generativeai as genai
        print("✅ google-generativeai is available")
    except ImportError:
        print("❌ google-generativeai is not installed")
        return False
    
    # Check if API key is available
    api_key = os.getenv("GOOGLE_API_KEY")
    if api_key:
        print("✅ Google API key found in environment")
    else:
        print("⚠️  Google API key not found in environment")
        print("   You can set it with: export GOOGLE_API_KEY='your_key_here'")
    
    return True

def test_basic_functionality():
    """
    Test basic functionality to make sure everything works.
    """
    print("\n=== Testing Basic Functionality ===")
    
    # Test pandas
    test_data = {
        "Color": ["Red", "Blue", "Green"],
        "Hex": ["#FF0000", "#0000FF", "#00FF00"]
    }
    df = pd.DataFrame(test_data)
    print("✅ Created test DataFrame:")
    print(df)
    
    # Test file operations
    try:
        df.to_excel("test_output.xlsx", index=False)
        print("✅ Successfully created test Excel file")
        
        # Clean up
        os.remove("test_output.xlsx")
        print("✅ Successfully cleaned up test file")
    except Exception as e:
        print(f"❌ Error with Excel operations: {e}")

def setup_llm(api_key: str = None):
    """
    Setup the LLM with Google Gemini API.
    """
    print("\n=== Setting up Google Gemini LLM ===")

    if api_key:
       print(f"✅ Using provided API key")
    else:
       api_key = os.getenv("GOOGLE_API_KEY")
       if api_key:
           print("Using API key from environments variables")
       else:
           print("❌ No API key found in environment")
           print("   You can set it with: export GOOGLE_API_KEY='your_key_here'")
           return False

    # genai.configure(api_key=api_key)
    try:
        genai.configure(api_key=api_key)
        print("✅ Google Gemini API key configured")
        return True
    except Exception as e:
        print(f"❌ Error configuring Google Gemini API key: {e}")
        return False

 

    #try catch to configure the api key
    # search in the other tutorial

def test_basic_llm_comunication():
    print("\n=== Testing Basic LLM Communication ===")

    try:
         model = genai.GenerativeModel("gemini-2.5-flash-lite")
         print(f"✅ Using model: {model.model_name}")
         prompt = "Hello! Can you respond with just 'Hello from Gemini'?"
         print(f"✅ Sending Prompt: {prompt}")
         response = model.generate_content(prompt)
         print(f"✅ LLM response: {response.text}")
    except Exception as e:
        print(f"❌ Error testing LLM communication: {e}")
        return False

    return True

def create_llm_prompt():
    print("\n=== Creating LLM Prompt ===")
    print(f"✅ Add some colors to decode----")
    user_input = input("Enter the colors to decode: ")
    print(f"✅ You entered: {user_input}")
    prompt = (
        "You are an expert color decoder. You are given a list of colors and you need to decode them. "
        "The colors are in hex format. "
        "The color are one or more words separated by a space. "
        "The response need to be in a json format with the following format: "
        "{"
        "  \"colors\": ["
        "    {"
        "      \"color_name\": \"<color_name>\","
        "      \"hex_code\": \"<hex_code>\""
        "    }"
        "  ]"
        "}"
        "Respond with ONLY valid JSON, no code block markers, no explanations."
        "check if there are more than one color in the response, if there are, return a list of colors."
        "check for duplicates, if there are, remove them."
        f"Colors to decode: {user_input}"
    )

    try:
        model = genai.GenerativeModel("gemini-2.5-flash-lite")
        print(f"✅ Using model: {model.model_name}")
        response = model.generate_content(prompt)
        print(f"✅ Response: {response.text}")
    except Exception as e:
        print(f"❌ Error creating LLM prompt: {e}")
        return False
    
    return response.text

def parse_json_response(json_response: str):
    print("\n=== Texting LLM Prompt ===")
    print(f"✅ JSON Response: {json_response}")
    try:
        json_response = json.loads(json_response)
        print(f"✅ JSON Response: {json_response}")
        print(f"✅ JSON Response: {json_response['colors']}")
    except Exception as e:
        print(f"❌ Error testing LLM prompt JSON: {e}")
        return False

def read_excel_file(excel_file: str):
    print("\n=== Reading Excel Files ===")
    print(f"✅ Reading Excel Files")

    # Check if the file exists
    if not os.path.exists(excel_file):
        print(f"❌ The file {excel_file} does not exist.")
        return False

    #excel_file = "docs/database_colors/colors.xlsx"
    # reference colors = "docs/database_colors/reference_colors.xlsx"
    try: 
        df = pd.read_excel(excel_file)
        print(f"✅ Successfully loaded Excel file")
        print(f"✅ Shape: {df.shape[0]} rows, {df.shape[1]} columns")
        print(f"✅ Columns: {list(df.columns)}")
        print(f"✅ First 3 rows:")
        print(df.head(3))
        return df
    except Exception as e:
        print(f"❌ Error reading Excel file: {e}")
        return False

def validate_excel_structure(df: pd.DataFrame, columns: list[str]):
    """
    Validate that the Excel file has the expected columns.
    
    Args:
        df: DataFrame to validate
        columns: List of column names that must exist
    
    Returns:
        bool: True if all columns exist, False otherwise
    """
    print(f"\n=== Validating Excel Structure ===")
    
    if df is None:
        print("❌ DataFrame is None")
        return False
    
    if not isinstance(columns, list):
        print("❌ Columns parameter must be a list")
        return False
    
    if len(columns) == 0:
        print("❌ No columns specified for validation")
        return False
    
    print(f"🔍 Checking for required columns: {columns}")
    print(f"📋 Available columns: {list(df.columns)}")
    
    missing_columns = []
    found_columns = []
    
    for column in columns:
        if column in df.columns:
            found_columns.append(column)
            print(f"✅ Found column: {column}")
        else:
            missing_columns.append(column)
            print(f"❌ Missing column: {column}")
    
    if missing_columns:
        print(f"❌ Validation failed: {len(missing_columns)} missing columns")
        return False
    else:
        print(f"✅ Validation successful: All {len(found_columns)} required columns found")
        return True


if __name__ == "__main__":
    print("Step 3: Reading Excel Files")
    print("=" * 50)
    
    # Check dependencies
    deps_ok = check_dependencies()
    
    if deps_ok:
        test_basic_functionality()
        setup_llm()
        #test_basic_llm_comunication()

        #json_response = create_llm_prompt()
        #parse_json_response(json_response)
        #print("give me the excel file")

        excel_source_file = input("Enter the excel source colors file: ")
        print(f"✅ You entered: {excel_source_file}")
        df = read_excel_file(excel_source_file)
        validate_excel_structure(df, ["COLOR NAME", "celHexa1", "celHexa2"])

        excel_destination_file = input("Enter the excel destination colors file: ")
        print(f"✅ You entered: {excel_destination_file}")
        df = read_excel_file(excel_destination_file)
        validate_excel_structure(df, ["COLOR NAME", "HEXA 1", "HEXA 2"])
        print("\n✅ Step 2 completed successfully!")
        print("Ready to move to Step 3: Reading Excel Files")

    else:
        print("\n❌ Please install missing dependencies before continuing")
        print("Run: uv sync") 