#!/bin/bash

# This bash script runs the evaluation with GPT-4 using a Python script
# Usage: ./run_evaluation.sh

# Set default values for the variables
START_INDEX=1
END_INDEX=3
ROOT_DIR_A="./story/A"  # Path to Story A directory
ROOT_DIR_B="./story/B"  # Path to Story B directory
CRITERIA="Interesting,Coherence,Creative,Closer"  # Evaluation criteria
API_KEY="openai-api-key"  # OpenAI API Key

# Display the values to confirm before running the script
echo "Running evaluation with the following parameters:"
echo "Start Index: $START_INDEX"
echo "End Index: $END_INDEX"
echo "Story A Directory: $ROOT_DIR_A"
echo "Story B Directory: $ROOT_DIR_B"
echo "Evaluation Criteria: $CRITERIA"
echo "OpenAI API Key: $API_KEY"

# Run the Python script with the provided arguments
python evaluation_gpt4.py "$START_INDEX" "$END_INDEX" "$ROOT_DIR_A" "$ROOT_DIR_B" "$CRITERIA" "$API_KEY"