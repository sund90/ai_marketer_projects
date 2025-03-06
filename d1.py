import streamlit as st

def main():
    st.title("Hello AI World!")
    st.write("Welcome to your first AI project.")
    
    if st.button("Click Me"):
        st.write("You clicked the button—congrats on launching your AI journey!")

if __name__ == "__main__":
    main()
