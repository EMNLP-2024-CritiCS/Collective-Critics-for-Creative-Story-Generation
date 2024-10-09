#!/bin/bash

# Set the OpenAI API key. Replace "openai-api-key" with your actual key.
export OPENAI_API_KEY="openai-api-key"

# Run the CritiCS app. Uncomment the following line to run it.
streamlit run home.py

# Test the script to generate the plan and story.
# python scripts/plan/generate.py
# python scripts/story/generate.py