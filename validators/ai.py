import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ai_review(content):
    prompt = f"""
You are a senior DevOps/SRE engineer.
Review the following infrastructure config and suggest:
- security improvements
- cost optimizations
- reliability improvements

Config:
{content}
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"AI Error: {str(e)}"
