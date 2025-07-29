# LLM Color Name and Hexadecimal Matcher

This tool uses **Artificial Intelligence (LLM)** to intelligently match color names with their corresponding hexadecimal codes from Excel files. It goes beyond simple text matching to handle synonyms, variations, and fuzzy matching.

## 🤖 What makes the LLM approach special?

### Traditional vs LLM Approach

| Feature               | Traditional Matching | LLM Matching              |
| --------------------- | -------------------- | ------------------------- |
| **Exact matches**     | ✅ Perfect           | ✅ Perfect                |
| **Case sensitivity**  | ❌ Issues            | ✅ Handled                |
| **Synonyms**          | ❌ No                | ✅ Yes (crimson → red)    |
| **Variations**        | ❌ No                | ✅ Yes (navy blue → blue) |
| **Fuzzy matching**    | ❌ No                | ✅ Yes                    |
| **Reasoning**         | ❌ No                | ✅ Yes                    |
| **Confidence levels** | ❌ No                | ✅ Yes                    |

### Examples of LLM Intelligence

**Input:** "Crimson"  
**Traditional:** No match found  
**LLM:** `#FF0000` (high confidence) - "crimson is a shade of red"

**Input:** "Navy Blue"  
**Traditional:** No match found  
**LLM:** `#0000FF` (medium confidence) - "navy blue is a variation of blue"

**Input:** "Azure"  
**Traditional:** No match found  
**LLM:** `#0000FF` (high confidence) - "azure is a synonym for blue"

## Setup

1. **Install dependencies:**

   ```bash
   uv sync
   ```

2. **Set up Google API key:**

   ```bash
   # Option 1: Environment variable
   export GOOGLE_API_KEY="your_api_key_here"

   # Option 2: .env file
   echo "GOOGLE_API_KEY=your_api_key_here" >> .env
   ```

## Usage

### Interactive LLM Mode

Run the LLM-based color matcher:

```bash
python llm_color_matcher_main.py
```

The script will prompt you for:

- Path to your reference Excel file
- Path to your target Excel file
- Output file name
- Column names (optional)
- Google API key (optional, uses env var if not provided)

### Example with Sample Data

Test the LLM capabilities with sample data:

```bash
python example_llm_color_matching.py
```

This creates sample files with color variations and demonstrates the AI's intelligence.

### Programmatic Usage

```python
from outils.llm_color_matcher import process_llm_color_matching

result_file = process_llm_color_matching(
    reference_file="your_reference.xlsx",
    target_file="your_target.xlsx",
    output_file="llm_output.xlsx",
    color_column="Color",
    hex_column="Hex",
    api_key="your_api_key"  # optional
)
```

## Output Format

The LLM approach creates a richer output with additional columns:

| Color     | Hex     | Confidence | Reasoning                        |
| --------- | ------- | ---------- | -------------------------------- |
| Red       | #FF0000 | high       | exact match                      |
| Crimson   | #FF0000 | high       | crimson is a shade of red        |
| Navy Blue | #0000FF | medium     | navy blue is a variation of blue |
| Gray      |         | low        | no known color with this name    |

## File Format Requirements

### Reference File Format

```
| Color  | Hex     |
|--------|---------|
| Red    | #FF0000 |
| Blue   | #0000FF |
| Green  | #00FF00 |
```

### Target File Format

```
| Color      |
|------------|
| Red        |
| Crimson    |
| Navy Blue  |
| Azure      |
```

## Advanced Features

### 1. Intelligent Matching

- **Exact matches:** Perfect when color names are identical
- **Synonyms:** Handles color synonyms (crimson → red, azure → blue)
- **Variations:** Understands color variations (navy blue → blue, lime → green)
- **Similar colors:** Finds close matches (gold → yellow, peach → orange)

### 2. Confidence Levels

- **High:** Exact match or very close synonym
- **Medium:** Reasonable variation or similar color
- **Low:** Uncertain match or no match found

### 3. Reasoning

Each match includes an explanation of why the AI chose that particular hex code, making the process transparent and auditable.

### 4. Error Handling

- Graceful handling of API errors
- Fallback responses for parsing issues
- Clear error messages for debugging

## Cost Considerations

The LLM approach uses Google's Gemini API, which has associated costs:

- **Free tier:** 15 requests per minute
- **Paid tier:** $0.0005 per 1K characters input + $0.0015 per 1K characters output

For typical color matching tasks, costs are minimal (usually under $0.01 per batch).

## When to Use Each Approach

### Use Traditional Matching When:

- ✅ Color names are standardized and consistent
- ✅ You need fast processing
- ✅ You want to avoid API costs
- ✅ Exact matches are sufficient

### Use LLM Matching When:

- ✅ Color names have variations or synonyms
- ✅ You need intelligent matching
- ✅ You want confidence levels and reasoning
- ✅ You're dealing with user-generated color names
- ✅ You need to handle fuzzy matching

## Troubleshooting

### API Key Issues

```
Error: Google API key not found
```

**Solution:** Set the `GOOGLE_API_KEY` environment variable or provide it when prompted.

### Rate Limiting

```
Error: Rate limit exceeded
```

**Solution:** The free tier has 15 requests per minute. Wait a moment and try again, or upgrade to a paid plan.

### Parsing Errors

```
Error: Failed to parse LLM response
```

**Solution:** This is rare but can happen. The tool will mark the color as "NO_MATCH" and continue processing.

### No Matches Found

If the LLM isn't finding expected matches:

1. Check that your reference file contains the base colors
2. Verify color names are spelled correctly
3. Consider adding more color variations to your reference file

## Example Workflow

1. **Prepare your files:**

   - Reference file: 100 color names with hex codes
   - Target file: 50 color names (some with variations)

2. **Run LLM matching:**

   ```bash
   python llm_color_matcher_main.py
   ```

3. **Review results:**

   - Check confidence levels
   - Read reasoning for each match
   - Verify unexpected matches

4. **Refine if needed:**
   - Add missing colors to reference file
   - Adjust color names for better matching

The LLM approach transforms color matching from a simple text comparison into an intelligent, context-aware process that can handle real-world variations in color naming!
