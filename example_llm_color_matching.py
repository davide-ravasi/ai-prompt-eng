from outils.llm_color_matcher import process_llm_color_matching
import pandas as pd
import os

def create_sample_files():
    """
    Create sample Excel files for LLM color matching demonstration.
    """
    # Create sample reference file (with color names and hex codes)
    reference_data = {
        "Color": ["Red", "Blue", "Green", "Yellow", "Purple", "Orange", "Pink", "Brown", "Black", "White"],
        "Hex": ["#FF0000", "#0000FF", "#00FF00", "#FFFF00", "#800080", "#FFA500", "#FFC0CB", "#A52A2A", "#000000", "#FFFFFF"]
    }
    df_ref = pd.DataFrame(reference_data)
    df_ref.to_excel("llm_sample_reference.xlsx", index=False)
    print("Created sample reference file: llm_sample_reference.xlsx")
    
    # Create sample target file with variations and synonyms to test LLM intelligence
    target_data = {
        "Color": [
            "Red",           # Exact match
            "Crimson",       # Synonym for red
            "Navy Blue",     # Variation of blue
            "Azure",         # Synonym for blue
            "Lime",          # Synonym for green
            "Gold",          # Similar to yellow
            "Violet",        # Synonym for purple
            "Peach",         # Similar to orange/pink
            "Beige",         # Similar to brown
            "Gray",          # Not in reference
            "Magenta",       # Not in reference
            "Teal"           # Not in reference
        ]
    }
    df_target = pd.DataFrame(target_data)
    df_target.to_excel("llm_sample_target.xlsx", index=False)
    print("Created sample target file: llm_sample_target.xlsx")
    print("This file contains color variations to test LLM intelligence!")

def run_llm_example():
    """
    Run an example of the LLM-based color matching process.
    """
    print("=== LLM Color Matching Example ===")
    print("This example demonstrates how AI can handle color synonyms and variations!")
    print()
    
    # Create sample files if they don't exist
    if not os.path.exists("llm_sample_reference.xlsx"):
        create_sample_files()
    
    print("Sample files created. The target file contains:")
    print("- Exact matches (Red)")
    print("- Synonyms (Crimson → Red, Azure → Blue)")
    print("- Variations (Navy Blue → Blue, Lime → Green)")
    print("- Similar colors (Gold → Yellow, Peach → Orange/Pink)")
    print("- Unknown colors (Gray, Magenta, Teal)")
    print()
    
    # Check if API key is available
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("⚠️  Warning: GOOGLE_API_KEY environment variable not set.")
        print("You can still run this example, but you'll need to provide an API key when prompted.")
        print()
    
    print("Running LLM-based color matching process...")
    print("This will take a moment as the AI analyzes each color...")
    print()
    
    # Process the color matching with LLM
    result_file = process_llm_color_matching(
        reference_file="llm_sample_reference.xlsx",
        target_file="llm_sample_target.xlsx",
        output_file="llm_example_output.xlsx"
    )
    
    if result_file:
        print(f"\n✅ LLM example completed! Check {result_file} for results.")
        
        # Show the results
        df_result = pd.read_excel(result_file)
        print("\nResults:")
        print("=" * 80)
        for _, row in df_result.iterrows():
            color = row["Color"]
            hex_code = row["Hex"]
            confidence = row["Confidence"]
            reasoning = row["Reasoning"]
            
            status = "✅" if hex_code else "❌"
            print(f"{status} {color:12} → {hex_code:8} ({confidence:6}) - {reasoning}")
        
        print("\n" + "=" * 80)
        print("The LLM approach provides:")
        print("- Intelligent matching beyond exact text matches")
        print("- Confidence levels for each match")
        print("- Reasoning for why each match was chosen")
        print("- Handling of synonyms and color variations")
        
    else:
        print("\n❌ Error in LLM example processing.")
        print("Make sure you have a valid Google API key set up.")

if __name__ == "__main__":
    run_llm_example() 