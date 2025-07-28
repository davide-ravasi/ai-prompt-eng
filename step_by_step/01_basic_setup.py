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
    return True
    

if __name__ == "__main__":
    print("Step 1: Basic Setup and Dependencies")
    print("=" * 50)
    
    # Check dependencies
    deps_ok = check_dependencies()
    
    if deps_ok:
        test_basic_functionality()
        setup_llm()
        print("\n✅ Step 1 completed successfully!")
        print("Ready to move to Step 2: LLM Setup")

    else:
        print("\n❌ Please install missing dependencies before continuing")
        print("Run: uv sync") 