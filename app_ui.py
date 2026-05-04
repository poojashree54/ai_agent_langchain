import streamlit as st
from app.agent import create_agent

st.set_page_config(page_title="AI Agent", page_icon="🤖")

st.title("Smart AI Agent")
st.write("Ask questions or perform calculations")

agent = create_agent()

if "history" not in st.session_state:
    st.session_state.history = []

query = st.text_input("Enter your question:")

if query:
    with st.spinner("Thinking..."):
        response = agent.run(query)

    st.session_state.history.append(("You", query))
    st.session_state.history.append(("AI", response))

for role, text in st.session_state.history:
    if role == "You":
        st.markdown(f"**You:** {text}")
    else:
        st.markdown(f"**AI:** {text}")