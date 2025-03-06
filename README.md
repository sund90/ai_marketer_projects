Day 1: Environment Setup & “Hello AI World”
Objective: Familiarize with Python environment, set up Streamlit skeleton, get comfortable with the local LLM in LM Studio.
Key Concepts:
Python project structure
Virtual environments (venv or conda)
Basic Streamlit app
Familiarity with local LLM (LM Studio)
Tasks:
Install and verify you have all required Python libraries:
pip install streamlit transformers torch torchvision torchaudio scikit-learn
(Adjust for Apple Silicon if needed.)
Create a minimal Streamlit app (hello_ai.py) with a single button that prints “Hello AI World”.
Sample Code: hello_ai.py
import streamlit as st

def main():
    st.title("Hello AI World!")
    st.write("Welcome to your first AI project.")
    
    if st.button("Click Me"):
        st.write("You clicked the button—congrats on launching your AI journey!")

if __name__ == "__main__":
    main()
Run:
streamlit run hello_ai.py
What You’ll Learn:
How to create and run a simple Streamlit app.
Basic Python script structure.
Setting the stage for building larger apps.
Knowledge Base Update:
Document what you did, any errors faced, and how you resolved them in a markdown or text file (e.g., Day1_Learnings.md).
