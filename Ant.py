from google import genai
from decouple import config

client = genai.Client(
    api_key=config("ANTHROPIC_API_KEY")
)

response = client.models.generate_content(
    model=config("ANTHROPIC_MODEL"),
    contents="Tell me about virat"
)

print(response.text)