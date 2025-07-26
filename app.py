import streamlit as st
from dotenv import load_dotenv
import os

from langchain.agents import initialize_agent
from langchain_openai import ChatOpenAI
from tools import tools

# Load environment variables
load_dotenv()

# Get API Key from environment
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    st.error("OPENAI_API_KEY not found in environment. Please add it to your .env or system environment.")
    st.stop()

# Initialize LLM
llm = ChatOpenAI(model="gpt-4o", temperature=0)

# Initialize agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True,
)

# --- Streamlit App ---
st.set_page_config(page_title="Reflexion Agent", page_icon="🤖")
st.title("🤖 Reflexion Agent with OpenAI")

query = st.text_area("Enter your question", height=100, placeholder="e.g. When was SpaceX's last launch and how many days ago was that?")
submit = st.button("Ask")

if submit and query:
    with st.spinner("Thinking..."):
        response = agent.invoke(query)
        st.markdown("### 🔍 Answer")
        st.write(response)
