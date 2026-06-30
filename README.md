# Order Organizer

A Python script that uses the Google GenAI SDK and Pydantic to parse messy logistics related text or order notes into a sorted Markdown table.

---

## AI Usage

**What I asked the AI to help with:**
* Identify the libraries required for such a task.
* Setting up the initial working code.
* How to use gemini-2.5-flash and Pydantic.
* Troubleshooting various errors.
* General help.

**What parts of the code were generated or suggested by AI:**
* The code structure that links the Pydantic schema to the Gemini response_schema configuration.

**What I changed or added myself:**
* Kept the sample messy text hardcoded for quick testing.
* Sent the extracted JSON data into a sorted Pandas DataFrame.
* Tested the output and ensured that the messy text got processed correctly, even with different examples.
* Specified the priority labels.

**What errors or issues I fixed:**
* API Key Security: Removed the hardcoded API key and updated the code to read GEMINI_API_KEY from the source to prevent leaking my own API key on GitHub after I push it.
* Minor inconsistencies in the output.

**What I understand now:**
* How to structure the output of AI models.
* How to link Google's Gemini inside VSCode and use it to process prompts.
* The meaning of "temprature" with regards to LLMs.

---

## What the Project Does
This script converts unorganized, messy text into structured data. It:
1. Extracts key info: Stop location, item, quantity, priority, and timeframes.
2. Sorts tasks automatically so that urgent jobs (1-Critical) appear at the top.
3. Prints the finalized data as a clean table.

---

## Sample Data Used
The example provided:
> "3x pipes to site B asap; deliver gloves (2 boxes) + 1 helmet to A tomorrow am; URGENT cement to site D; pickup empty pallets from C; H needs 5 vests by end of day"

---

## Prerequisites
* Python 3.10 or higher
* A Gemini API Key

---

## How to Get a Gemini API Key
1. Go to https://aistudio.google.com/
2. Log in with your Google account.
3. Click the Get API key button.
4. Copy the long string of characters.

---

## How to Run in VS Code

**Step 1: Open the Project**
1. Open VS Code.
2. Click File > Open Folder and select your project folder.
3. Open your organizer.py file.

**Step 2: Open the Terminal**
1. Open the built-in terminal using Ctrl + ` (backtick) or click Terminal > New Terminal.
2. Make sure the Terminal tab at the bottom is active.

**Step 3: Install Packages**
Run this command in the terminal to install the required libraries:

```
pip install google-genai pandas pydantic tabulate
```

**Step 4: Set Your API Key**
Check the top-right corner of your terminal panel to see if it is using PowerShell, CMD, or Bash, then run the matching command below:

* For PowerShell:
```
$env:GEMINI_API_KEY="your_copied_api_key_here"
```

* For Command Prompt (CMD):
```
set GEMINI_API_KEY=your_copied_api_key_here
```

* For Bash / Zsh (Mac/Linux):
```
export GEMINI_API_KEY="your_copied_api_key_here"
```

**Step 5: Run the Code**
Run the script by typing:

```
python organizer.py
```

## Expected Output

```
| Stop   | Item    | Quantity   | Priority   | When           |
|:-------|:--------|:-----------|:-----------|:---------------|
| B      | pipes   | 3x         | 1-Critical | asap           |
| D      | cement  | 1          | 1-Critical | URGENT         |
| H      | vests   | 5          | 2-High     | by end of day  |
| A      | gloves  | 2 boxes    | 3-Medium   | tomorrow am    |
| A      | helmet  | 1          | 3-Medium   | tomorrow am    |
| C      | pallets | empty      | 4-Low      | unspecified    |
```
