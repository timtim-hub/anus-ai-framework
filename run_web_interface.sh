#!/bin/bash

# Activate the virtual environment
source venv/bin/activate

# Run the Streamlit web interface
echo "Starting ANUS AI Framework Web Interface..."
echo "Press Ctrl+C to quit"
streamlit run anus/ui/web_interface.py 