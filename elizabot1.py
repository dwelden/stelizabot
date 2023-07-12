import streamlit as st
import eliza

# A demonstrator for Streamlit's chat elements
# using a Python version of ELIZA, the early natural language processing 
# computer program created from 1964 to 1966 at MIT by Joseph Weizenbaum
# (see https://en.wikipedia.org/wiki/ELIZA)
#
# The code for this version of the Eliza chatbot can be found here:
#   https://github.com/wadetb/eliza/tree/master
# It is the work of Wade Brainerd and is licensed under the MIT license

st.title("Eliza Bot")

# Create a 'therapist' who will answer your questions
therapist = eliza.Eliza()
therapist.load('doctor.txt')

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
else:
    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("How can I help?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    response = therapist.respond(prompt)
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})

