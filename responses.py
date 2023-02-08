import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")


async def get_response(user_message, channel, client):
    model_engine = "text-davinci-003"
    prompt = f"User: {user_message}"

    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message
