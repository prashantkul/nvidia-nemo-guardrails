NeMo Guardrails Demo

This demo shows NeMo Guardrails handling:
- Prompt injection
- Jailbreaking
- PII detection
- Topicality (restrict to weather-related questions)

It uses a minimal Colang spec plus instructions, and runs several sample prompts.

## Prereqs
- Conda env `nemo-guardrails` is active (as you noted)
- Install: `pip install nemoguardrails openai` (or another supported chat model provider)
- Set `OPENAI_API_KEY` (if using OpenAI models)

## Original Demo (Weather Assistant)

### Configuration
- `config/config_original.yml`: Main configuration for the weather assistant.
- `config/rail_spec.co`: Defines the conversational flows and guardrails for the weather assistant.

### Run
- Quick run with canned prompts:
  `python main.py`
- Interactive mode:
  `python main.py --interactive`

### Notes
- This config constrains the assistant to a weather domain. Off-topic requests are refused.
- PII sharing is discouraged; the bot will warn and avoid storing or repeating it.
- Obvious prompt-injection/jailbreak attempts are refused. The Colang examples guide the model toward safe behavior, but effectiveness depends on the underlying model.

## RAG Demo (Company Policies Assistant)

This demo showcases Retrieval-Augmented Generation (RAG) using NeMo Guardrails to answer questions based on a provided knowledge base.

### Configuration
- `config/config.yml`: Main configuration for the RAG assistant.
- `config/rail_spec_rag.co`: Defines the conversational flows and guardrails for the RAG assistant.
- `config/kb_rag/my_document_rag.md`: The knowledge base document containing company policies.

### Setup
1. Ensure you have `faiss-cpu` installed:
   `pip install faiss-cpu`

### Run
- Quick run with a canned prompt:
  `python my_app_rag.py`

### Notes
- This demo uses a knowledge base to answer questions about company policies.
- The assistant is configured to only answer questions related to company policies.
