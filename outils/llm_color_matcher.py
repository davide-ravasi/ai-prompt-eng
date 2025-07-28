import google.generativeai as genai
import pandas as pd
import os
from typing import Dict, List, Optional, Tuple
import json

def setup_llm(api_key: str = None):
    """
    Setup the LLM with Google Gemini API.
    """
    if api_key:
        genai.configure(api_key=api_key)
    else:
        # Try to get from environment variable
        api_key = os.getenv("GOOGLE_API_KEY")
        if api_key:
            genai.configure(api_key=api_key)
        else:
            raise ValueError("Google API key not found. Please set GOOGLE_API_KEY environment variable or pass it as parameter.")

def create_color_matching_prompt(color_name: str, reference_colors: List[Dict[str, str]]) -> str:
    """
    Create a prompt for the LLM to match a color name with hex codes.
    """
    reference_text = "\n".join([f"- {color['name']}: {color['hex']}" for color in reference_colors])
    
    prompt = f"""
You are a color matching expert. I need you to find the best matching hex code for a color name.

Available reference colors:
{reference_text}

Target color name: "{color_name}"

Instructions:
1. Look for exact matches first
2. If no exact match, look for synonyms or similar color names
3. Consider common color variations (e.g., "navy blue" might match "blue")
4. If multiple matches are possible, choose the most likely one
5. If no reasonable match is found, return "NO_MATCH"

Respond with ONLY a JSON object in this format:
{{
    "hex_code": "the_hex_code_or_NO_MATCH",
    "confidence": "high/medium/low",
    "reasoning": "brief explanation of why this match was chosen"
}}

Examples:
- For "Red" → {{"hex_code": "#FF0000", "confidence": "high", "reasoning": "exact match"}}
- For "Crimson" → {{"hex_code": "#FF0000", "confidence": "medium", "reasoning": "crimson is a shade of red"}}
- For "XYZ" → {{"hex_code": "NO_MATCH", "confidence": "low", "reasoning": "no known color with this name"}}
"""
    return prompt

def match_color_with_llm(color_name: str, reference_colors: List[Dict[str, str]], model_name: str = "gemini-1.5-flash") -> Dict[str, str]:
    """
    Use LLM to match a color name with hex codes from reference data.
    """
    try:
        # Create the prompt
        prompt = create_color_matching_prompt(color_name, reference_colors)
        
        # Get the model
        model = genai.GenerativeModel(model_name)
        
        # Generate response
        response = model.generate_content(prompt)
        
        # Parse the JSON response
        try:
            result = json.loads(response.text.strip())
            return result
        except json.JSONDecodeError:
            # Fallback if JSON parsing fails
            return {
                "hex_code": "NO_MATCH",
                "confidence": "low", 
                "reasoning": "Failed to parse LLM response"
            }
            
    except Exception as e:
        print(f"Error matching color '{color_name}' with LLM: {e}")
        return {
            "hex_code": "NO_MATCH",
            "confidence": "low",
            "reasoning": f"Error: {str(e)}"
        }

def read_color_reference_file(file_path: str, color_column: str = "Color", hex_column: str = "Hex") -> List[Dict[str, str]]:
    """
    Read an Excel file containing color names and their corresponding hex codes.
    Returns a list of dictionaries for LLM processing.
    """
    try:
        df = pd.read_excel(file_path)
        
        reference_colors = []
        for _, row in df.iterrows():
            color_name = str(row[color_column]).strip()
            hex_code = str(row[hex_column]).strip()
            if color_name and hex_code and hex_code != 'nan':
                reference_colors.append({
                    "name": color_name.lower(),
                    "hex": hex_code
                })
        
        print(f"Loaded {len(reference_colors)} color mappings from {file_path}")
        return reference_colors
    
    except Exception as e:
        print(f"Error reading color reference file: {e}")
        return []

def read_target_document(file_path: str, color_column: str = "Color") -> List[str]:
    """
    Read the target document containing color names that need hex codes.
    """
    try:
        df = pd.read_excel(file_path)
        color_names = [str(name).strip() for name in df[color_column] if pd.notna(name)]
        print(f"Found {len(color_names)} color names in target document")
        return color_names
    
    except Exception as e:
        print(f"Error reading target document: {e}")
        return []

def match_colors_with_llm_and_create_output(target_colors: List[str], reference_colors: List[Dict[str, str]], 
                                          output_file: str = "llm_matched_colors.xlsx") -> str:
    """
    Match color names with hex codes using LLM and create output file.
    """
    try:
        print("Starting LLM-based color matching...")
        
        # Create output data
        output_data = []
        matches = 0
        
        for i, color in enumerate(target_colors, 1):
            print(f"Processing color {i}/{len(target_colors)}: {color}")
            
            # Use LLM to match the color
            llm_result = match_color_with_llm(color, reference_colors)
            
            hex_code = llm_result["hex_code"] if llm_result["hex_code"] != "NO_MATCH" else ""
            confidence = llm_result.get("confidence", "unknown")
            reasoning = llm_result.get("reasoning", "")
            
            if hex_code:
                matches += 1
            
            output_data.append({
                "Color": color,
                "Hex": hex_code,
                "Confidence": confidence,
                "Reasoning": reasoning
            })
        
        # Create DataFrame and save to Excel
        df_output = pd.DataFrame(output_data)
        df_output.to_excel(output_file, index=False)
        
        print(f"Created output file: {output_file}")
        print(f"LLM matched {matches} out of {len(target_colors)} colors")
        
        return output_file
    
    except Exception as e:
        print(f"Error creating output file: {e}")
        return ""

def process_llm_color_matching(reference_file: str, target_file: str, output_file: str = "llm_matched_colors.xlsx",
                             color_column: str = "Color", hex_column: str = "Hex", api_key: str = None) -> str:
    """
    Main function to process color matching using LLM between reference and target files.
    """
    print("Starting LLM-based color matching process...")
    
    # Setup LLM
    try:
        setup_llm(api_key)
        print("LLM setup successful")
    except Exception as e:
        print(f"Failed to setup LLM: {e}")
        return ""
    
    # Read reference file
    reference_colors = read_color_reference_file(reference_file, color_column, hex_column)
    if not reference_colors:
        print("Failed to read reference file. Exiting.")
        return ""
    
    # Read target file
    target_colors = read_target_document(target_file, color_column)
    if not target_colors:
        print("Failed to read target file. Exiting.")
        return ""
    
    # Match colors using LLM and create output
    output_path = match_colors_with_llm_and_create_output(target_colors, reference_colors, output_file)
    
    return output_path 