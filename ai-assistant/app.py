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


# data layer

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

#service layer
def build_ai_prompt(context: str):
    return "" \
    " You are a helpful company assistant. " \
    "Answeer user questions based on some sample data that you create" \
    "and return the response to the user. include some data in the response" \
    "these are the guardrailes: " \
    "- do not use negative words "\
    f"this is my context: {context}"

def get_ai_response(client: OpenAI, chat_history: list, context:str):
    #built the prompt
    ai_prompt = build_ai_prompt(context)
    ai_prompt_message= [
        {
            "role": "system",
            "content": ai_prompt
        }
    ]
    messages = chat_history + ai_prompt_message

        #call the open ai agent, get the response 
    ai_response = client.chat.completions.create(
        model="gpt-5-mini",
        messages=messages,
        temperature=1
    )

    return ai_response.choices[0].message.content

logs = load_logs("ai-assistant/ai_logs.json")

if "messages" not in st.session_state:
    st.session_state["messages"] = []
    for log in logs:
        st.session_state['messages'].append(
            {
                'role': log['role'],
                'content': log['content']
            }
        )
    if len(st.session_state['messages']) == 0:
        st.session_state['messages'].append(
            {
                'role' : 'assistant',
                'content' : "Hi , ask me a question"
            }
        )


for message in st.session_state['messages']:
    with st.chat_message(message['role']):
        st.markdown(message['content'])


user_input = st.chat_input("Ask me a question...")

if user_input:
    st.session_state['messages'].append(
        {
            "role": "user",
            "content": user_input
    }
    )
    with st.chat_message('user'):
        st.markdown(user_input)
    
    with st.chat_message("assistant"):
        with st.spinner("Thinking...."):
            import time
            time.sleep(2)
            ai_response = get_ai_response(clinet, st.session_state['messages'], "my context is healthcare")
            st.markdown(ai_response)


        st.session_state['messages'].append(
            {
                'role': 'assistant',
                'content': ai_response
            }
        )

    logs = load_logs("ai-assistant/ai_logs.json")
    logs.append({
        'user_message':user_input,
        'ai_response': ai_response
    })
    save_logs("ai-assistant/ai_logs.json", logs)