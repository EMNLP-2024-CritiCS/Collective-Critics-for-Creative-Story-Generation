#!/bin/bash

# Set the OpenAI API key. Replace "openai-api-key" with the actual key.
export OPENAI_API_KEY="openai-api-key"

# Run the 'plan' and 'story' steps to set up the servers.
python start_servers.py --step plan
python start_servers.py --step story

# Close the servers once you're done. This script keeps running in the background, so make sure to stop it when needed.
# python close_servers.py