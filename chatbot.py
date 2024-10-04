import streamlit as st
from langchain_community.llms import Ollama

# Initialize the model
llm = Ollama(model="llama3")

# Streamlit app title
st.title("Sims 4 ChatBot")
st.write("Ask your questions or talk about anything relating to Sims 4 here :)")

def app():
    # Input field for user to enter their prompt
    prompt = st.text_area("Enter your prompt: ")
    
    # Generate response on button click
    if st.button("Generate"):
        if prompt:
            with st.spinner("Generating response..."):
                # Call the model to generate response
                response = llm(prompt)  # Standard method for calling model
                st.write(response)

# Call the app function to run the app
if __name__ == "__main__":
    app()
