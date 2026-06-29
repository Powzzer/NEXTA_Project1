# NEXTA_Project1
# Gemini AI Logistics Extractor

A Python script that uses the Google GenAI SDK and Pydantic to parse messy logistics notes into a sorted Markdown table.

---

## AI Usage

### What I asked the AI to help with
* Setting up the initial data extraction using `gemini-2.5-flash` and Pydantic.
* Troubleshooting API client errors and setup.

### What parts of the code were generated or suggested by AI
* The code structure that links the Pydantic schema to the Gemini `response_schema` configuration.

### What I changed or added myself
* Kept the sample logistics text hardcoded for quick and easy testing.
* Sent the extracted JSON data into a sorted Pandas DataFrame.

### What errors or issues I fixed
* **API Key Security:** Removed the hardcoded API key and updated the code to read `GEMINI_API_KEY` from the system environment variables to prevent leaking credentials on GitHub.

### What I understand now
* How Structured Outputs force AI models to always return clean, consistent JSON data.
* How to use system environment variables to keep API keys safe.

---

## What the Project Does
This script converts unorganized, handwritten notes into structured data. It:
1. Extracts key info: Stop location, item, quantity, priority, and timeframes.
2. Sorts tasks automatically so that urgent jobs (`1-Critical`) appear at the top.
3. Prints the finalized data as a clean Markdown table.

---

## Sample Data Used
The script processes unstructured text logs like this:
> *"3x pipes to site B asap; deliver gloves (2 boxes) + 1 helmet to A tomorrow am; URGENT cement to site D; pickup empty pallets from C; H needs 5 vests by end of day"*

---

## Prerequisites
* Python 3.10 or higher
* A Gemini API Key

---

## How to Get a Gemini API Key
1. Go to [Google AI Studio](https://aistudio.google.com/).
2. Log in with your Google account.
3. Click the **Get API key** button.
4. Click **Create API key**, choose a project, and copy your new key string.

---

## How to Run in VS Code

### Step 1: Open the Project
1. Open VS Code.
2. Click **File > Open Folder...** and select your project folder.
3. Open your `organizer.py` file.

### Step 2: Open the Terminal
1. Open the built-in terminal using `` Ctrl + ` `` (backtick) or click **Terminal > New Terminal**.
2. Make sure the **Terminal** tab at the bottom is active.

### Step 3: Install Packages
Run this command in the terminal to install the required libraries:
```bash
pip install google-genai pandas pydantic tabulate
