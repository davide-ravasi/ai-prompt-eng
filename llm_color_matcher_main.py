from outils.llm_color_matcher import process_llm_color_matching
import os

def main():
    """
    Main function to handle LLM-based color name and hexadecimal matching from Excel files.
    """
    print("=== LLM Color Name and Hexadecimal Matcher ===")
    print("This tool uses AI to intelligently match color names with their hex codes.")
    print("It can handle synonyms, variations, and fuzzy matching!")
    print()
    
    # Get file paths from user
    print("Please provide the following information:")
    
    # Reference file (contains color names and hex codes)
    reference_file = input("Path to reference ODS file (with color names and hex codes): ").strip()
    if not os.path.exists(reference_file):
        print(f"Error: Reference file '{reference_file}' not found!")
        return
    
    # Target file (contains only color names)
    target_file = input("Path to target ODS file (with color names that need hex codes): ").strip()
    if not os.path.exists(target_file):
        print(f"Error: Target file '{target_file}' not found!")
        return
    
    # Output file
    output_file = input("Name for output file (default: llm_matched_colors.xlsx): ").strip()
    if not output_file:
        output_file = "llm_matched_colors.xlsx"
    
    # Column names (optional customization)
    print("\nColumn names (press Enter to use defaults):")
    color_column = input("Color column name (default: 'NAME'): ").strip() or "NAME"
    hex_column = input("Hex column name (default: 'HEXA1'): ").strip() or "HEXA1"
    
    # API Key (optional, will use environment variable if not provided)
    api_key = input("Google API Key (optional, will use GOOGLE_API_KEY env var if empty): ").strip()
    if not api_key:
        api_key = None
    
    print("\nProcessing with LLM...")
    print("This may take a while as the AI analyzes each color name...")
    
    # Process the color matching with LLM
    result_file = process_llm_color_matching(
        reference_file=reference_file,
        target_file=target_file,
        output_file=output_file,
        color_column=color_column,
        hex_column=hex_column,
        api_key=api_key
    )
    
    if result_file:
        print(f"\n✅ Success! Output file created: {result_file}")
        print("The file contains:")
        print("- Your color names")
        print("- Matched hex codes (empty where no match was found)")
        print("- Confidence levels for each match")
        print("- AI reasoning for each match")
        print("\nThis LLM approach can handle:")
        print("- Exact matches")
        print("- Synonyms (e.g., 'crimson' → 'red')")
        print("- Variations (e.g., 'navy blue' → 'blue')")
        print("- Fuzzy matching")
    else:
        print("\n❌ Error occurred during processing. Please check your files and API key.")

if __name__ == "__main__":
    main() 