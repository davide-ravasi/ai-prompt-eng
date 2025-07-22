# Prompt Engineering Guidelines for LLMs (Gemini, etc.)

This document summarizes best practices and actionable tips for crafting effective prompts for large language models (LLMs) like Google Gemini, with a focus on generating high-quality social media posts (e.g., for X/Twitter).

---

## 1. Define the Role and Task Clearly

- **State the model's role** (e.g., "You are an expert social media manager...").
- **Describe the task** in detail (e.g., "Your task is to generate a concise, impactful post tailored to the topic provided by the user.").

**Example:**

```
You are an expert social media manager, and you excel at crafting viral and highly engaging posts for X (formerly Twitter).
Your task is to generate a post that is concise, impactful, and tailored to the topic provided by the user.
```

---

## 2. Give Stylistic and Structural Instructions

- Specify tone, length, and style (e.g., "concise, impactful").
- Set rules for hashtags, emojis, and formatting (e.g., "Avoid using excessive hashtags and emojis (a few emojis are okay, but not too many). Use line breaks and empty lines to enhance readability.").

**Example:**

```
Avoid using excessive hashtags and emojis (a few emojis are okay, but not too many).
Keep the post short and focused, structure it in a clean, readable way, using line breaks and empty lines to enhance readability.
```

---

## 3. Use Few-Shot Examples (Demonstrations)

- **Provide several examples** of the desired output, each with a different topic and style.
- **Label examples clearly** (e.g., "Title:" and "Content:").
- **Separate examples with newlines** for clarity.
- **End with the new input and the label for the model to complete.**

**Example:**

```
Here are some examples of how to structure the post:
Title: The Future of AI
Content: The future of AI is here. We are on the brink of a new era where AI will transform the way we live and work. It will be the key to unlocking new opportunities and solving some of the world's most complex problems.

Title: Healthy Living
Content: Small daily habits can lead to big changes! Start your day with a glass of water, a stretch, and a positive mindset. Your future self will thank you.

Title: Remote Work Tips
Content: Working from home? Set clear boundaries, take regular breaks, and communicate openly with your team. Productivity and well-being go hand in hand!
```

---

## 4. Instruct the Model on How to Use Examples

- Tell the model to use the **style, tone, and structure** of the examples, but **not to copy their content**.

**Example:**

```
Please use the tone, language, structure, and style of the examples provided above to generate a post that is engaging and relevant to the topic provided by the user.
Don't use the content from the examples!
```

---

## 5. End the Prompt with the User's Input

- **Signal the model to generate new content** by ending with the user's topic and the label for completion.

**Example:**

```
Title: {user_topic}
Content:
```

---

## 6. Separate Data from Logic for Maintainability

- **Store examples in a separate JSON file** (e.g., `post-examples.json`) for easy updates.
- **Load and format examples dynamically** in your code.

**Python Example:**

```python
examples_string = ""
with open("post-examples.json", "r") as file:
    examples = json.load(file)
    for example in examples["examples"]:
        examples_string += f"Title: {example['title']}\n"
        examples_string += f"Content: {example['content']}\n\n"
```

---

## 7. General Tips for Good Prompt Engineering

- **Be explicit and unambiguous** in your instructions.
- **Use consistent labeling** in examples and the final prompt.
- **Vary your examples** to help the model generalize.
- **Keep prompts as short as possible, but as long as necessary.**
- **Test and iterate**: Try different prompt structures and see what works best for your use case.

---

## 8. Example Full Prompt (for Gemini)

```
You are an expert social media manager, and you excel at crafting viral and highly engaging posts for X (formerly Twitter).
Your task is to generate a post that is concise, impactful, and tailored to the topic provided by the user.
Avoid using excessive hashtags and emojis (a few emojis are okay, but not too many).
Keep the post short and focused, structure it in a clean, readable way, using line breaks and empty lines to enhance readability.

Here are some examples of how to structure the post:
{examples_string}
Please use the tone, language, structure, and style of the examples provided above to generate a post that is engaging and relevant to the topic provided by the user.
Don't use the content from the examples!
Title: {user_topic}
Content:
```

---

**By following these guidelines, you can craft effective prompts that guide LLMs to produce high-quality, on-brand social media content or other outputs.**
