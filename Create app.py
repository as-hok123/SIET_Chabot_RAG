import streamlit as st
from rag_engine import load_base, ask_rag
st.set_page_config(page_title = "SIET_chatbot",layout = "centered")
st.title("shridevi Institute of Engineering and Technology- chatBOt")
st.caotion("Ask anything about college information...")
st.caption("created by msd")

@st.cache_resource
def intiate_rag():
   return load_base("01_College_Information.pdf")

index, embed_model,chunks = initiate_rag()  
