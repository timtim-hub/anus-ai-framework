#!/bin/bash

# Script to set up environment variables for ANUS AI Framework

# Check if .env file exists
if [ ! -f .env ]; then
    echo "Error: .env file not found!"
    echo "Please create a .env file first by copying the example:"
    echo "cp .env.example .env"
    exit 1
fi

# Source the environment variables
echo "Loading environment variables from .env file..."
export $(grep -v '^#' .env | xargs)

# Verify the API keys
if [ "$OPENAI_API_KEY" = "your_openai_api_key_here" ]; then
    echo "⚠️  Warning: You need to set your OPENAI_API_KEY in the .env file"
    echo "    Edit the .env file and replace 'your_openai_api_key_here' with your actual OpenAI API key"
    MISSING_KEYS=true
fi

if [ "$ANTHROPIC_API_KEY" = "your_anthropic_api_key_here" ]; then
    echo "⚠️  Warning: ANTHROPIC_API_KEY is not set in the .env file"
    echo "    This is optional unless you plan to use Claude models"
fi

# Display success message if all required keys are set
if [ "$MISSING_KEYS" != "true" ]; then
    echo "✅ Environment variables loaded successfully!"
    echo "You can now run the ANUS AI Framework"
    echo ""
    echo "To run the web interface: ./run_web_interface.sh"
fi 