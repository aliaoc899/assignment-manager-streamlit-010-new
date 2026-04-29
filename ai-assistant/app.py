import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI
from pathlib import Path
import json

load_dotenv()

st.set_page_config("AI Assistant- Open AI")

st.title("AI Assistant- Open AI")

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("Open AI Key was not found")
    st.stop()

clinet = OpenAI(api_key=api_key) # create an object from the open ai class and 
                    #                   intialize it with the api key


def load_orders_data(filepath: str):
    json_path = Path(filepath)
    if json_path.exists():
        with open(json_path, "r") as f:
            return json.load(f)
    else:
        return []
    


orders = load_orders_data("ai-assistant/orders.json")


# Chat logs loads and saving methods

def load_logs(filepth):
    json_path = Path(filepth)
    if json_path.exists():
        with open(json_path,"r") as f:
            return json.load(f)
    else:
        return []

def save_logs(filepath, logs):
    json_path = Path(filepath)
    with open(json_path, "w") as f:
        json.dump(logs, f)

if "messages" not in st.session_state:
    st.session_state["messages"] = []

logs = load_logs("ai-assistant/ai_logs.json")

for log in logs:
    st.session_state['messages'].append(
        {
            'role': log['role'],
            'content': log['context']
        }
    )

if len(st.session_state['messages']) == 0:
    st.session_state['messages'].append(
        {
            'role' : 'ai-assistent',
            'content' : "Hi , ask me a question"
        }
    )
