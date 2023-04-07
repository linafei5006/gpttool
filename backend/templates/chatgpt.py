import openai
import os

openai.api_key = os.getenv("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")

def get_response_from_gpt(text):
    response = openai.Completion.create(
        engine="davinci",
        prompt=text,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    return response.choices[0].text.strip()
