import os
import openai 
from dotenv import load_dotenv
from typing import List

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def extract_genres_from_text(user_input : str) -> List[str]:
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Extract movie genres from user preferences."},
                {"role": "user", "content": user_input}
            ],
            temperature = 0.5,
            max_tokens = 50,
        )
        genres_text = response.choices[0].message.content
        return [g.strip() for g in genres_text.split(",")]
        return genres
    except Exception as e:
        print(f"Error when calling openai API key : {e}")
        return []