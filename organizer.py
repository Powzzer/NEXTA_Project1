import os
import json
import pandas as pd
from google import genai
from google.genai import types
from pydantic import BaseModel, Field

# Initialize the Gemini Client (reads GEMINI_API_KEY from environment)
client = genai.Client()
# Define the structured schema for the output
class DeliveryJob(BaseModel):
    Stop: str = Field(description="The letter or identifier of the site (e.g., A, B, C)")
    Item: str = Field(description="The name of the item being delivered or picked up")
    Quantity: str = Field(description="The quantity or amount (e.g., 3x, 2 boxes)")
    Priority: str = Field(description="Must be exactly one of: 1-Critical, 2-High, 3-Medium, 4-Low")
    When: str = Field(description="The timeframe mentioned in the text")

class DeliveryPlan(BaseModel):
    jobs: list[DeliveryJob]

messy_text = "3x pipes to site B asap; deliver gloves (2 boxes) + 1 helmet to A tomorrow am; URGENT cement to site D; pickup empty pallets from C; H needs 5 vests by end of day"

# Call the model with structured JSON schema constraints
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=f"Extract the logistics details from this text into the requested layout: {messy_text}",
    config=types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=DeliveryPlan,
        temperature=0.1,
    ),
)

json_data = json.loads(response.text)
df = pd.DataFrame(json_data["jobs"])

df = df.sort_values(by="Priority")

COLOR_MAP = {
    "1-Critical": "\033[91m1-Critical\033[0m", # Red
    "2-High":     "\033[38;5;208m2-High\033[0m",     # True Orange    
    "3-Medium":   "\033[33m3-Medium\033[0m",   # Yellow
    "4-Low":      "\033[92m4-Low\033[0m"        # Green
}

df['Priority'] = df['Priority'].map(COLOR_MAP).fillna(df['Priority'])

print(df.to_markdown(index=False))