NeMo Guardrails Demo

This demo showcases NeMo Guardrails handling:
- Prompt injection
- Jailbreaking
- PII detection
- Topicality (restricting to weather-related questions)

It utilizes a minimal Colang specification and instructions, running several sample prompts.

## Prerequisites
- Ensure your Conda environment `nemo-guardrails` is active.
- Install necessary packages: `pip install nemoguardrails openai` (or another supported chat model provider).
- Set your `OPENAI_API_KEY` environment variable (if using OpenAI models).

## Original Demo (Weather Assistant)

### Configuration
- `config/config.yml`: Main configuration for the weather assistant.
- `config/rail_spec.co`: Defines the conversational flows and guardrails for the weather assistant.

### How to Run
- **Quick run with canned prompts:**
  `python main.py`
- **Interactive mode:**
  `python main.py --interactive`

### Notes
- This configuration constrains the assistant to a weather domain; off-topic requests are refused.
- PII sharing is discouraged; the bot will warn and avoid storing or repeating it.
- Obvious prompt-injection/jailbreak attempts are refused. The Colang examples guide the model toward safe behavior, but effectiveness depends on the underlying model.

## RAG Demo (Company Policies Assistant)

This demo showcases Retrieval-Augmented Generation (RAG) using NeMo Guardrails to answer questions based on a provided knowledge base.

### Configuration
- `config/config_rag.yml`: Main configuration for the RAG assistant.
- `config/rail_spec_rag.co`: Defines the conversational flows and guardrails for the RAG assistant.
- `config/kb_rag/my_document_rag.md`: The knowledge base document containing company policies.

### Setup
- No specific embedding search provider installation is required. By default, NeMo Guardrails uses `FastEmbed` for embeddings and `Annoy` for search functionality.

### How to Run
- **Quick run with a canned prompt:**
  `python my_app_rag.py`

### Notes
- This demo uses a knowledge base to answer questions about company policies.
- The assistant is configured to only answer questions related to company policies.
