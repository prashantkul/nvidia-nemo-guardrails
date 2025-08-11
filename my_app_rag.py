import os
from dotenv import load_dotenv
from nemoguardrails import RailsConfig, LLMRails

load_dotenv()

# Load the configuration from the config folder
config = RailsConfig.from_path("config/config_rag.yml")

# Create the LLMRails instance
rails = LLMRails(config)

response = rails.generate(messages=[{
    "role": "user",
    "content": "What are the company policies?"
}])
print(f"Bot: {response['content']}")
