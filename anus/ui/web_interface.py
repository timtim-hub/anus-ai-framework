"""
Anus - Autonomous Networked Utility System
Web Interface powered by Streamlit
"""

import streamlit as st
from anus.core.orchestrator import AgentOrchestrator
import os
import yaml

def load_config():
    """Load the configuration file"""
    config_path = os.path.join(os.getcwd(), "config.yaml")
    if os.path.exists(config_path):
        with open(config_path, "r") as f:
            return yaml.safe_load(f)
    return {}

def main():
    """Main function for the web interface"""
    st.set_page_config(
        page_title="ANUS AI Framework",
        page_icon="🍑",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    
    # Header
    st.title("🍑 ANUS AI Framework")
    st.subheader("Autonomous Networked Utility System")
    
    # Sidebar
    st.sidebar.title("Configuration")
    
    # Load config
    config = load_config()
    
    # Mode selection
    mode = st.sidebar.radio("Agent Mode", ["Single Agent", "Multi-Agent"])
    
    # Main content area
    st.markdown("""
    Welcome to the ANUS AI Framework web interface. This interface allows you to
    interact with the AI agent system through a user-friendly web interface.
    """)
    
    # Input area
    st.subheader("Task Input")
    user_input = st.text_area("Enter your task or question:", height=100)
    
    # Action buttons
    col1, col2, col3 = st.columns(3)
    with col1:
        run_button = st.button("Run Task", type="primary")
    with col2:
        clear_button = st.button("Clear")
    with col3:
        help_button = st.button("Help")
    
    # If run button is clicked
    if run_button and user_input:
        with st.spinner("ANUS is processing your request..."):
            try:
                # Initialize the agent orchestrator
                agent_mode = "multi" if mode == "Multi-Agent" else "single"
                orchestrator = AgentOrchestrator(config_path="config.yaml")
                
                # Execute the task
                result = orchestrator.execute_task(user_input, mode=agent_mode)
                
                # Display the result
                st.subheader("Task Result")
                st.success("Task completed successfully!")
                st.markdown(result)
                
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
                st.info("Make sure your config.yaml file is properly set up with your API keys.")
    
    # If clear button is clicked
    if clear_button:
        st.experimental_rerun()
    
    # If help button is clicked
    if help_button:
        st.info("""
        ## How to use ANUS AI
        
        1. Enter your task or question in the text area
        2. Select the agent mode (Single or Multi-Agent)
        3. Click 'Run Task' to execute
        
        ### Example Tasks
        
        - "Find information about climate change"
        - "Generate a Python script to visualize stock data"
        - "Analyze this text: [paste text here]"
        - "What is the capital of France?"
        """)
    
    # Footer
    st.markdown("---")
    st.markdown("ANUS AI Framework - An Autonomous Networked Utility System")
    st.markdown("GitHub Repository: [nikmcfly/ANUS](https://github.com/nikmcfly/ANUS)")

if __name__ == "__main__":
    main() 